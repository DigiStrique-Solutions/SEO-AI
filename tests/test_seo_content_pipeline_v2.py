"""Deterministic tests for the version-two SEO content contract."""

import importlib.util
import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "seo_content_pipeline_v2.py"
SPEC = importlib.util.spec_from_file_location("seo_content_pipeline_v2", MODULE_PATH)
pipeline = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pipeline
SPEC.loader.exec_module(pipeline)


def packet(intent="informational"):
    """Return a source-backed packet fixture."""
    return {
        "schema_version": 2,
        "website": "https://example.com",
        "target_reader": "office shoppers",
        "primary_query": "office shoes",
        "search_intent": intent,
        "article_type": "how_to",
        "desired_action": "browse shoes",
        "sources": [
            {
                "source_id": "product-1",
                "source_type": "product_page",
                "source_ref": "https://example.com/one",
                "extracted_facts": ["Leather upper"],
                "verified_url": True,
                "concrete_attributes": ["material: leather"],
            },
            {
                "source_id": "product-2",
                "source_type": "shopify",
                "source_ref": "gid://product/2",
                "extracted_facts": ["Rubber sole"],
                "verified_url": True,
                "concrete_attributes": ["sole: rubber"],
            },
        ],
        "claims": [
            {
                "claim_id": "claim-1",
                "text": "The shoe has a leather upper.",
                "claim_type": "material",
                "source_ids": ["product-1"],
                "commercially_material": True,
            }
        ],
        "missing_evidence": [],
        "internal_links": ["https://example.com/office"],
        "structure": {},
    }


def test_commercial_packet_requires_two_products():
    """Commercial writing cannot proceed from one generic source."""
    value = packet("commercial")
    value["sources"] = value["sources"][:1]
    findings = pipeline.validate_content_packet_v2(value)
    assert "insufficient_product_evidence" in {item["code"] for item in findings}


def test_brand_dna_cannot_support_material_claim():
    """Brand narrative is not product evidence for a material claim."""
    value = packet()
    value["sources"] = [
        {
            "source_id": "brand",
            "source_type": "brand_dna",
            "source_ref": "brand.md",
            "extracted_facts": ["Premium voice"],
        }
    ]
    value["claims"][0]["source_ids"] = ["brand"]
    findings = pipeline.validate_content_packet_v2(value)
    assert "sensitive_claim_source_type" in {item["code"] for item in findings}


def test_intent_structure_does_not_force_faq_or_toc():
    """A short valid outline is accepted without boilerplate utility sections."""
    outline = {"schema_version": 2, "title": "Office shoes", "sections": [
        {"heading": "Match the commute", "purpose": "Fit the use case", "kind": "substantive"}
    ]}
    assert pipeline.validate_outline_v2(packet(), outline) == []


def test_process_language_and_unmapped_claim_are_span_level_failures():
    """Internal workflow text and unsupported product language block export."""
    markdown = "# Office shoes\n\nThe source used for this article says leather.\n"
    report = pipeline.validate_draft_v2(packet(), {"sections": []}, markdown, {"references": []})
    codes = {item["code"] for item in report["findings"]}
    assert {"process_language_leak", "unmapped_sensitive_claim"} <= codes


def test_batch_similarity_ignores_utility_headings_but_catches_template_order():
    """Legitimate labels are ignored while duplicated substantive templates fail."""
    first = "# A\n\n## Quick Answer\n\nA.\n\n## Fit the commute\n\nStart with the route."
    second = "# B\n\n## FAQ\n\nB.\n\n## Fit the commute\n\nStart with the route."
    report = pipeline.batch_similarity_report([first, second])
    assert report["score"] >= report["threshold"]


def test_corpus_release_gate_requires_all_manual_detector_results():
    """A detector KPI is not reported as passed while measurements are missing."""
    cases = [
        {
            "case_id": f"case-{index}",
            "category": "failure",
            "prompt": {},
            "content_packet": {},
            "model": "pending",
            "prompt_version": "seo-content-v1",
            "generated_article": {},
            "claim_map": {},
            "deterministic_gate_results": {},
            "human_scores": {},
            "zerogpt": {"score": None},
        }
        for index in range(40)
    ]
    report = pipeline.evaluate_corpus(cases)
    assert report["release_ready"] is False
    assert report["manual_detector_complete"] == 0


def test_write_blog_cli_defaults_to_schema_v2():
    """New CLI runs use code gates and require an explicit legacy switch."""
    harness_path = ROOT / "tools" / "seo_audit_harness.py"
    spec = importlib.util.spec_from_file_location("seo_audit_harness_v2_test", harness_path)
    harness = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = harness
    spec.loader.exec_module(harness)
    args = harness.build_parser().parse_args(
        [
            "write-blog",
            "--brand-dir",
            "brands/example",
            "--keyword",
            "office shoes",
            "--draft-file",
            "draft.md",
            "--content-output",
            "final.md",
            "--authenticity",
            "auth.json",
        ]
    )
    assert args.legacy_compatibility is False


def test_schema_v2_export_preserves_exact_markdown():
    """The offline export writes the validated Markdown byte for byte."""
    harness_path = ROOT / "tools" / "seo_audit_harness.py"
    spec = importlib.util.spec_from_file_location("seo_audit_harness_export_test", harness_path)
    harness = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = harness
    spec.loader.exec_module(harness)
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        markdown = "# Office shoes\n\nThe shoe has a leather upper.\n\n[Browse](https://example.com/office)\n"
        outline = {"schema_version": 2, "title": "Office shoes", "sections": [
            {"heading": "Fit", "purpose": "Use case", "kind": "substantive"}
        ]}
        claim_map = {"schema_version": 2, "references": [
            {
                "quote": "The shoe has a leather upper.",
                "claim_id": "claim-1",
                "source_ids": ["product-1"],
            }
        ]}
        paths = {
            "draft": base / "draft.md",
            "packet": base / "packet.json",
            "outline": base / "outline.json",
            "claim_map": base / "claim-map.json",
            "auth": base / "auth.json",
            "output": base / "output.md",
        }
        paths["draft"].write_text(markdown, encoding="utf-8")
        paths["packet"].write_text(json.dumps(packet("commercial")), encoding="utf-8")
        paths["outline"].write_text(json.dumps(outline), encoding="utf-8")
        paths["claim_map"].write_text(json.dumps(claim_map), encoding="utf-8")
        paths["auth"].write_text(json.dumps({"detector_notes": []}), encoding="utf-8")
        result = harness.write_blog_v2_with_gates(
            "",
            paths["draft"],
            paths["output"],
            paths["auth"],
            paths["packet"],
            paths["outline"],
            paths["claim_map"],
        )
        assert result["ok"] is True
        assert paths["output"].read_text(encoding="utf-8") == markdown


def test_cross_repo_contract_fixture_is_identical():
    """Offline and production repositories share one serialized contract fixture."""
    local = ROOT / "tests" / "fixtures" / "seo_content_contract_v2.json"
    production = (
        Path("/Users/poojan/Desktop/projects-new/strique/strique-ai-server")
        / "tests"
        / "fixtures"
        / "seo_content_contract_v2.json"
    )
    assert local.read_bytes() == production.read_bytes()


def test_local_writing_skill_changes_require_eval_updates():
    """The CI guard couples local writing behavior to versioned evaluation changes."""
    guard_path = ROOT / "tools" / "check_seo_eval_change.py"
    spec = importlib.util.spec_from_file_location("check_seo_eval_change_test", guard_path)
    guard = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(guard)
    assert guard.validate([".agents/skills/content-seo-authenticity/SKILL.md"])
    assert not guard.validate(
        [
            ".agents/skills/content-seo-authenticity/SKILL.md",
            "evals/seo-content-v2/cases.json",
        ]
    )
