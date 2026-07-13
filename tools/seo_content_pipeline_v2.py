#!/usr/bin/env python3
"""Offline schema-v2 gates shared by evaluation and the legacy CLI adapter."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

SCHEMA_VERSION = 2
UTILITY_HEADINGS = {
    "quick answer",
    "table of contents",
    "contents",
    "faq",
    "faqs",
    "related reading",
    "related posts",
    "next step",
    "next steps",
}
PRODUCT_SOURCE_TYPES = {"product_page", "shopify", "merchant_center"}
FORBIDDEN_SENSITIVE_SOURCES = {"brand_dna", "youtube_video"}
SENSITIVE_CLAIMS = {
    "price": ("price", "₹", "inr", "rs."),
    "availability": ("available", "in stock", "out of stock"),
    "material": ("leather", "suede", "material"),
    "comfort": ("comfortable", "comfort", "cushion", "footbed", "arch support"),
    "dimensions": ("heel height", "strap drop", "dimension", "width"),
    "reviews": ("review", "rating", "customers say"),
    "performance": ("waterproof", "durable", "long-lasting"),
}
PROCESS_PATTERNS = (
    r"\b(?:system|writing) prompt\b",
    r"\b(?:agent|model) instructions\b",
    r"\bauthenticity log\b",
    r"\b(?:load|loaded|using) (?:the )?skill\b",
    r"\btool (?:call|output|use)\b",
    r"\bthe source used for this (?:brief|article)\b",
    r"\binternal brief\b",
)


def load_json(path):
    """Load a UTF-8 JSON document."""
    return json.loads(Path(path).read_text(encoding="utf-8"))


def packet_hash(packet):
    """Return the reproducibility hash for a packet."""
    value = json.dumps(packet, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(value.encode()).hexdigest()


def _finding(code, message, affected_text="", blocking=True, overridable=False):
    return {
        "code": code,
        "message": message,
        "affected_text": affected_text,
        "blocking": blocking,
        "overridable": overridable,
    }


def validate_content_packet_v2(packet):
    """Validate source sufficiency without depending on writing skills."""
    findings = []
    required = (
        "website",
        "target_reader",
        "primary_query",
        "search_intent",
        "article_type",
        "desired_action",
    )
    if packet.get("schema_version") != SCHEMA_VERSION:
        findings.append(_finding("schema_version", "Content packet must use schema_version 2."))
    for field in required:
        if not packet.get(field):
            findings.append(_finding("missing_packet_field", f"Missing packet field: {field}"))
    sources = {source.get("source_id"): source for source in packet.get("sources", [])}
    if not sources:
        findings.append(_finding("no_sources", "At least one approved source is required."))
    if not packet.get("internal_links"):
        findings.append(_finding("no_internal_links", "At least one relevant internal link is required."))
    for item in packet.get("missing_evidence", []):
        if item.get("blocking", True):
            findings.append(
                _finding("blocking_missing_evidence", item.get("description", "Missing evidence"))
            )
    if packet.get("search_intent") in {"commercial", "transactional", "mixed"}:
        products = [
            source
            for source in sources.values()
            if source.get("source_type") in PRODUCT_SOURCE_TYPES
            and source.get("verified_url")
            and source.get("concrete_attributes")
        ]
        if len(products) < 2:
            findings.append(
                _finding(
                    "insufficient_product_evidence",
                    "Commercial ecommerce content needs two verified product records.",
                )
            )
    for claim in packet.get("claims", []):
        claim_sources = [sources.get(item) for item in claim.get("source_ids", [])]
        if not claim_sources or any(item is None for item in claim_sources):
            findings.append(_finding("claim_unknown_source", claim.get("text", "")))
            continue
        if claim.get("commercially_material") or claim.get("claim_type") in SENSITIVE_CLAIMS:
            source_types = {item.get("source_type") for item in claim_sources}
            if source_types <= FORBIDDEN_SENSITIVE_SOURCES:
                findings.append(_finding("sensitive_claim_source_type", claim.get("text", "")))
    return findings


def validate_outline_v2(packet, outline):
    """Validate intent-driven structure without fixed article anatomy."""
    findings = []
    sections = outline.get("sections", [])
    kinds = [section.get("kind", "substantive") for section in sections]
    structure = packet.get("structure", {})
    if "faq" in kinds and not (structure.get("faq_allowed") or packet.get("approved_questions")):
        findings.append(_finding("unsupported_faq", "FAQ lacks SERP, PAA, or customer evidence."))
    if structure.get("quick_answer_required") and "quick_answer" not in kinds:
        findings.append(_finding("missing_quick_answer", "This direct query requires a quick answer."))
    substantive_count = kinds.count("substantive")
    toc_required = structure.get("toc_required") or structure.get("user_requested_toc")
    if (toc_required or substantive_count >= 7) and "toc" not in kinds:
        findings.append(_finding("missing_toc", "This outline requires navigation."))
    return findings


def _exact_mapped_quotes(markdown, claim_map, packet):
    claim_ids = {claim.get("claim_id") for claim in packet.get("claims", [])}
    source_ids = {source.get("source_id") for source in packet.get("sources", [])}
    valid = []
    findings = []
    for reference in claim_map.get("references", []):
        quote = reference.get("quote", "")
        if quote not in markdown:
            findings.append(_finding("claim_quote_missing", "Mapped quote is not in the draft.", quote))
        elif reference.get("claim_id") not in claim_ids or not set(
            reference.get("source_ids", [])
        ) <= source_ids:
            findings.append(_finding("claim_map_unknown_reference", "Unknown claim or source.", quote))
        else:
            valid.append(quote.lower())
    return valid, findings


def style_pattern_risk(markdown):
    """Return an editorial pattern heuristic, not an authorship probability."""
    clean = re.sub(r"(?m)^#{1,6}\s+", "", markdown).lower()
    phrases = (
        "in today's digital landscape",
        "when it comes to",
        "at its core",
        "game changer",
        "in conclusion",
    )
    features = [phrase for phrase in phrases if phrase in clean]
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", markdown) if part.strip()]
    starts = []
    for paragraph in paragraphs:
        match = re.search(r"[A-Za-z][A-Za-z']*", paragraph)
        if match:
            starts.append(match.group(0).lower())
    ratio = max(Counter(starts).values(), default=0) / len(starts) if len(starts) >= 4 else 0
    if ratio >= 0.45:
        features.append("repeated_paragraph_openings")
    score = min(100, len(features) * 8 + max(0, ratio - 0.3) * 40)
    return {
        "score": round(score, 2),
        "features": features,
        "note": "Editorial style-pattern score; not an authorship probability.",
    }


def validate_draft_v2(packet, outline, markdown, claim_map):
    """Run deterministic, span-level factual and structural gates."""
    findings = validate_content_packet_v2(packet) + validate_outline_v2(packet, outline)
    h1_count = len(re.findall(r"(?m)^#\s+\S", markdown))
    if h1_count != 1:
        findings.append(_finding("single_h1", f"Expected one H1, found {h1_count}."))
    if packet.get("internal_links") and not re.search(r"\[[^]]+\]\((?:/|https?://)", markdown):
        findings.append(_finding("missing_internal_link", "No approved internal link appears."))
    for pattern in PROCESS_PATTERNS:
        match = re.search(pattern, markdown, re.IGNORECASE)
        if match:
            findings.append(_finding("process_language_leak", "Internal workflow language leaked.", match.group(0)))
    for restricted in packet.get("restricted_claims", []):
        if restricted.lower() in markdown.lower():
            findings.append(
                _finding("restricted_claim", "The draft contains a packet-restricted claim.", restricted)
            )
    valid_quotes, map_findings = _exact_mapped_quotes(markdown, claim_map, packet)
    findings.extend(map_findings)
    lower = markdown.lower()
    if re.search(r"\b(?:best|top)\b", lower) and not any(
        re.search(r"\b(?:best|top)\b", quote) for quote in valid_quotes
    ):
        findings.append(
            _finding(
                "unsupported_best_top_claim",
                "Best or top language has no mapped criteria and evidence.",
                "best/top",
            )
        )
    for claim_type, tokens in SENSITIVE_CLAIMS.items():
        for token in tokens:
            if token in lower and not any(token in quote for quote in valid_quotes):
                findings.append(_finding("unmapped_sensitive_claim", claim_type, token))
                break
    risk = style_pattern_risk(markdown)
    if risk["score"] >= 20:
        findings.append(
            _finding(
                "style_pattern_risk",
                f"Style-pattern score {risk['score']} requires review.",
                blocking=False,
                overridable=True,
            )
        )
    factual_blockers = [item for item in findings if item["blocking"]]
    return {
        "schema_version": 2,
        "ok": not factual_blockers,
        "export_allowed": not factual_blockers and risk["score"] < 20,
        "next_status": "correcting" if factual_blockers else "export_ready",
        "findings": findings,
        "style_pattern_risk": risk,
    }


def _substantive_headings(markdown):
    values = []
    for heading in re.findall(r"(?m)^##\s+(.+?)\s*$", markdown):
        normalized = re.sub(r"[^a-z0-9 ]", "", heading.lower()).strip()
        if normalized not in UTILITY_HEADINGS:
            values.append(normalized)
    return values


def batch_similarity_report(drafts):
    """Compare substantive structure while ignoring legitimate utility labels."""
    documents = []
    for markdown in drafts:
        headings = _substantive_headings(markdown)
        openings = []
        for paragraph in re.split(r"\n\s*\n", markdown):
            text = re.sub(r"^[#>*\-\s]+", "", paragraph).strip().lower()
            words = re.findall(r"[a-z][a-z']*", text)
            if words:
                openings.append(" ".join(words[:5]))
        phrases = Counter(re.findall(r"\b[a-z]+(?:\s+[a-z]+){3}\b", markdown.lower()))
        documents.append({"headings": headings, "openings": openings, "phrases": phrases})
    scores = []
    for index, left in enumerate(documents):
        for right in documents[index + 1 :]:
            left_h, right_h = set(left["headings"]), set(right["headings"])
            union = left_h | right_h
            heading_score = len(left_h & right_h) / len(union) if union else 0
            order_score = 1 if left["headings"] == right["headings"] and left["headings"] else 0
            opening_union = set(left["openings"]) | set(right["openings"])
            opening_score = (
                len(set(left["openings"]) & set(right["openings"])) / len(opening_union)
                if opening_union
                else 0
            )
            repeated_phrases = set(left["phrases"]) & set(right["phrases"])
            phrase_score = min(1, len(repeated_phrases) / 5)
            scores.append(heading_score * 45 + order_score * 20 + opening_score * 20 + phrase_score * 15)
    score = sum(scores) / len(scores) if scores else 0
    return {
        "score": round(score, 2),
        "draft_count": len(drafts),
        "pair_count": len(scores),
        "threshold": 35,
        "ok": score < 35,
    }


def evaluate_corpus(cases):
    """Calculate release-gate coverage without inventing manual detector results."""
    if len(cases) != 40:
        return {"ok": False, "errors": [f"Expected 40 cases, found {len(cases)}."]}
    required = {
        "case_id",
        "category",
        "prompt",
        "content_packet",
        "model",
        "prompt_version",
        "generated_article",
        "claim_map",
        "deterministic_gate_results",
        "human_scores",
        "zerogpt",
    }
    errors = []
    for case in cases:
        missing = sorted(required - set(case))
        if missing:
            errors.append(f"{case.get('case_id', 'unknown')}: missing {', '.join(missing)}")
    deterministic_checked = 0
    deterministic_passed = 0
    for case in cases:
        if case.get("category") != "failure_case":
            continue
        expected = set(case.get("prompt", {}).get("expected_findings", []))
        article = case.get("generated_article", {}).get("inline_markdown", "")
        outline = case.get("prompt", {}).get(
            "outline", {"schema_version": 2, "title": "Failure fixture", "sections": []}
        )
        report = validate_draft_v2(
            case.get("content_packet", {}),
            outline,
            article,
            case.get("claim_map", {}),
        )
        actual = {finding["code"] for finding in report["findings"]}
        if "batch_similarity" in expected:
            batch = batch_similarity_report([article, article])
            if not batch["ok"]:
                actual.add("batch_similarity")
        deterministic_checked += 1
        missing_expected = expected - actual
        if missing_expected:
            errors.append(
                f"{case['case_id']}: missing expected findings {sorted(missing_expected)}"
            )
        else:
            deterministic_passed += 1
    completed_detector = [case for case in cases if case["zerogpt"].get("score") is not None]
    below = [case for case in completed_detector if case["zerogpt"]["score"] < 20]
    detector_failures = [case for case in completed_detector if case["zerogpt"]["score"] >= 20]
    routed_detector_failures = [
        case for case in detector_failures if case["zerogpt"].get("review_routed") is True
    ]
    completed_human = [case for case in cases if case["human_scores"].get("edit_effort")]
    publishable = [
        case for case in completed_human if case["human_scores"]["edit_effort"] in {"none", "minor"}
    ]
    deterministic_ready = deterministic_checked == 10 and deterministic_passed == 10
    detector_routing_ready = len(routed_detector_failures) == len(detector_failures)
    human_ready = len(completed_human) == 40 and len(publishable) >= 34
    return {
        "ok": not errors and len(completed_detector) == 40 and human_ready,
        "errors": errors,
        "case_count": len(cases),
        "deterministic_failure_cases": {
            "checked": deterministic_checked,
            "passed": deterministic_passed,
        },
        "manual_detector_complete": len(completed_detector),
        "below_20_percent": len(below),
        "below_20_rate": round(len(below) / len(completed_detector), 4)
        if completed_detector
        else None,
        "detector_failures_routed": len(routed_detector_failures),
        "human_rubrics_complete": len(completed_human),
        "publishable_minor_edits": len(publishable),
        "release_ready": (
            len(completed_detector) == 40
            and len(below) >= 32
            and detector_routing_ready
            and deterministic_ready
            and human_ready
            and not errors
        ),
    }
