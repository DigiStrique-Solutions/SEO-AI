import copy
import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "seo_audit_harness.py"
SPEC = importlib.util.spec_from_file_location("seo_audit_harness", MODULE_PATH)
seo_audit_harness = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = seo_audit_harness
SPEC.loader.exec_module(seo_audit_harness)


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self):
        return self.payload.encode("utf-8")


class SeoAuditHarnessTests(unittest.TestCase):
    def make_checklist(self, text):
        tmpdir = tempfile.TemporaryDirectory()
        path = Path(tmpdir.name) / "sample-checklist.md"
        path.write_text(text, encoding="utf-8")
        self.addCleanup(tmpdir.cleanup)
        return path

    def compiled_fixture(self):
        path = self.make_checklist(
            """# Sample Checklist

## 1. First Section

Evidence sources: `Manual`, `GSC`.

- [ ] The page has one purpose.
- [ ] The title is clear.

Plain prose is ignored.

## 2. Second Section

- [ ] The CTA is visible.
"""
        )
        return seo_audit_harness.compile_checklists([str(path)])

    def keyword_row(self, keyword, priority="medium", source="test source"):
        return {
            "keyword": keyword,
            "intent": "commercial",
            "page_type": "product",
            "target_url": "https://www.example.com/product",
            "volume": "100",
            "difficulty": "LOW 10",
            "priority": priority,
            "source": source,
            "status": "new",
            "notes": "Test evidence.",
        }

    def make_keyword_brand_dir(self, rows=None, universe_count=200, blockers=None):
        tmpdir = tempfile.TemporaryDirectory()
        brand_dir = Path(tmpdir.name)
        self.addCleanup(tmpdir.cleanup)
        (brand_dir / "keywords").mkdir(parents=True)
        (brand_dir / "exports").mkdir(parents=True)
        (brand_dir / "references").mkdir(parents=True)
        (brand_dir / "brand-dna.md").write_text(
            """# Brand DNA

### Name

Example

### Website URL

https://www.example.com
""",
            encoding="utf-8",
        )
        if rows is None:
            rows = [
                self.keyword_row(
                    "keyword {}".format(index),
                    priority="high" if index < 10 else "medium",
                )
                for index in range(60)
            ]
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.keyword_csv_path(brand_dir),
            seo_audit_harness.KEYWORD_ROW_FIELDS,
            rows,
        )
        universe_rows = []
        for index in range(universe_count):
            universe_rows.append(
                {
                    "keyword": "universe keyword {}".format(index),
                    "normalized_keyword": "universe keyword {}".format(index),
                    "intent": "commercial",
                    "page_type": "product",
                    "target_url": "https://www.example.com/product",
                    "volume": "100",
                    "difficulty": "LOW 10",
                    "priority": "medium",
                    "sources": "Google Ads Keyword Planner via Composio",
                    "gsc_clicks": "",
                    "gsc_impressions": "",
                    "gsc_ctr": "",
                    "gsc_position": "",
                    "gsc_page": "",
                    "gsc_country": "",
                    "status": "new",
                    "notes": "Test evidence.",
                }
            )
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.keyword_universe_path(brand_dir),
            seo_audit_harness.KEYWORD_UNIVERSE_FIELDS,
            universe_rows,
        )
        seo_audit_harness.write_json(
            {
                "target_country": "United States",
                "counts": {
                    "prioritized_rows": len(rows),
                    "deduped_universe_rows": universe_count,
                },
                "blockers": blockers or [],
            },
            seo_audit_harness.keyword_summary_path(brand_dir),
        )
        return brand_dir

    def test_compile_parses_checklist_rows(self):
        compiled = self.compiled_fixture()
        self.assertEqual(len(compiled["items"]), 3)
        self.assertEqual(compiled["items"][0]["checklist_id"], "sample")
        self.assertEqual(compiled["items"][0]["section_id"], "1-first-section")
        self.assertEqual(compiled["items"][0]["required_evidence"], "`Manual`, `GSC`.")

    def test_item_ids_are_stable_when_order_changes(self):
        first = self.make_checklist(
            """# Sample Checklist

## Section

- [ ] Alpha item.
- [ ] Beta item.
"""
        )
        second = self.make_checklist(
            """# Sample Checklist

## Section

- [ ] Beta item.
- [ ] Alpha item.
"""
        )
        first_ids = {
            item["item_text"]: item["item_id"]
            for item in seo_audit_harness.compile_checklists([str(first)])["items"]
        }
        second_ids = {
            item["item_text"]: item["item_id"]
            for item in seo_audit_harness.compile_checklists([str(second)])["items"]
        }
        self.assertEqual(first_ids, second_ids)

    def test_text_edit_creates_new_item_id(self):
        first = self.make_checklist("# Sample\n\n## Section\n\n- [ ] Alpha item.\n")
        second = self.make_checklist("# Sample\n\n## Section\n\n- [ ] Alpha item changed.\n")
        first_id = seo_audit_harness.compile_checklists([str(first)])["items"][0]["item_id"]
        second_id = seo_audit_harness.compile_checklists([str(second)])["items"][0]["item_id"]
        self.assertNotEqual(first_id, second_id)

    def test_verify_passes_complete_matrix(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "full")
        for row in audit["rows"]:
            row.update(
                {
                    "status": "pass",
                    "evidence_source": "Manual",
                    "artifact_ref": "https://example.com",
                    "result": "Verified.",
                    "blocker": "",
                    "next_action": "",
                }
            )
        self.assertEqual(seo_audit_harness.validate_audit(compiled, audit), [])

    def test_verify_fails_missing_item(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "partial")
        audit["rows"].pop()
        errors = seo_audit_harness.validate_audit(compiled, audit)
        self.assertTrue(any("missing" in error for error in errors))

    def test_verify_fails_pass_without_evidence(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "partial")
        audit["rows"][0]["status"] = "pass"
        errors = seo_audit_harness.validate_audit(compiled, audit)
        self.assertTrue(any("needs nonempty evidence_source" in error for error in errors))

    def test_verify_fails_blocked_without_blocker(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "partial")
        audit["rows"][0]["blocker"] = ""
        errors = seo_audit_harness.validate_audit(compiled, audit)
        self.assertTrue(any("blocked needs nonempty blocker" in error for error in errors))

    def test_partial_audit_allows_blocked_rows(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "partial")
        self.assertEqual(seo_audit_harness.validate_audit(compiled, audit), [])

    def test_full_audit_fails_blocked_rows(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(compiled, "https://example.com", "full")
        errors = seo_audit_harness.validate_audit(compiled, audit)
        self.assertTrue(any("full audit has" in error for error in errors))

    def test_evidence_sources_are_canonicalized(self):
        sources = seo_audit_harness.parse_evidence_sources(
            "`Firecrawl`, `LH`, `GA4`, `CMS/code`, `Google Search Console via Composio`."
        )

        self.assertEqual(
            sources,
            ["firecrawl", "lighthouse", "ga4", "manual:cms-code", "gsc"],
        )

    def test_logical_evidence_sources_map_analytics_providers(self):
        sources = seo_audit_harness.parse_logical_evidence_sources(
            "`GA4`, `PostHog`, `Google Search Console`, `GKP`, `Firecrawl`"
        )

        self.assertEqual(
            sources,
            ["analytics", "search_console", "keyword_demand", "public_crawl"],
        )

    def test_provider_connections_resolve_strique_and_ga4_analytics(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "references").mkdir()
        seo_audit_harness.write_json(
            {"providers": {"analytics": ["posthog"]}},
            seo_audit_harness.provider_connections_path(brand_dir),
        )

        strique_route = seo_audit_harness.route_evidence_for_item(
            "Organic conversions are reviewed.",
            ["analytics"],
            provider_connections=seo_audit_harness.load_provider_connections(brand_dir),
        )
        ga4_route = seo_audit_harness.route_evidence_for_item(
            "Organic conversions are reviewed.",
            ["analytics"],
            provider_connections=seo_audit_harness.normalize_provider_connections(
                {"providers": {"analytics": ["ga4"]}}
            ),
        )

        self.assertEqual(strique_route["required_sources"], ["posthog"])
        self.assertEqual(ga4_route["required_sources"], ["ga4"])

    def test_missing_analytics_provider_creates_provider_blocker(self):
        route = seo_audit_harness.route_evidence_for_item(
            "Organic conversions are reviewed.",
            ["analytics"],
            provider_connections={"public_crawl": ["firecrawl"]},
        )

        self.assertEqual(route["required_sources"], [])
        self.assertEqual(route["provider_blockers"][0]["logical_source"], "analytics")

    def test_required_sources_are_inferred_from_item_text(self):
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "Core Web Vitals LCP and CLS are measured.",
                ["firecrawl"],
            ),
            ["lighthouse", "pagespeed", "crux"],
        )
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "Keyword mapping includes volume and competition.",
                ["gsc"],
            ),
            ["keyword_planner"],
        )
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "The page has one clear primary search intent.",
                ["gsc", "gkp", "firecrawl"],
            ),
            ["firecrawl", "gsc", "keyword_planner"],
        )
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "Rendered mobile content is visible.",
                ["firecrawl"],
            ),
            ["playwright"],
        )

    def test_google_visible_source_routing_ignores_backend_optional_sources(self):
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "The title is unique and visible.",
                ["manual:cms-code", "firecrawl"],
                scope=seo_audit_harness.GOOGLE_VISIBLE_SCOPE,
            ),
            ["firecrawl"],
        )
        self.assertEqual(
            seo_audit_harness.infer_required_sources(
                "Organic sessions that fail the intended next step are flagged.",
                ["posthog", "gsc"],
                scope=seo_audit_harness.GOOGLE_VISIBLE_SCOPE,
            ),
            [],
        )

    def test_strict_audit_initializes_evidence_fields(self):
        compiled = self.compiled_fixture()

        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )

        row = audit["rows"][0]
        self.assertEqual(row["candidate_sources"], ["manual:manual", "search_console"])
        self.assertEqual(row["required_sources"], ["gsc"])
        self.assertEqual(row["logical_required_sources"], ["search_console"])
        self.assertEqual(row["resolved_required_sources"], ["gsc"])
        self.assertIn("evidence_plan", row)
        self.assertIn("evidence_artifacts", row)

    def test_strict_verify_passes_when_required_artifact_exists(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        artifact = Path(tmpdir.name) / "gsc.json"
        artifact.write_text("{}", encoding="utf-8")
        audit["rows"][0].update(
            {
                "status": "pass",
                "evidence_source": "gsc",
                "artifact_ref": str(artifact),
                "result": "Verified with GSC.",
                "blocker": "",
                "next_action": "",
            }
        )

        errors = seo_audit_harness.validate_audit(
            compiled,
            audit,
            strict_evidence=True,
        )

        self.assertEqual(errors, [])

    def test_strict_verify_fails_missing_required_source(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        artifact = Path(tmpdir.name) / "playwright.json"
        artifact.write_text("{}", encoding="utf-8")
        audit["rows"][0].update(
            {
                "status": "pass",
                "evidence_source": "playwright",
                "artifact_ref": str(artifact),
                "result": "Verified with the wrong source.",
                "blocker": "",
                "next_action": "",
            }
        )

        errors = seo_audit_harness.validate_audit(
            compiled,
            audit,
            strict_evidence=True,
        )

        self.assertTrue(any("evidence_source must include" in error for error in errors))

    def test_strict_verify_respects_brand_analytics_provider(self):
        path = self.make_checklist(
            """# Analytics Checklist

## Analytics

Evidence sources: `GA4`, `PostHog`.

- [ ] Organic conversions are reviewed.
"""
        )
        compiled = seo_audit_harness.compile_checklists([str(path)])
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "references").mkdir()
        seo_audit_harness.write_json(
            {"providers": {"analytics": ["posthog"]}},
            seo_audit_harness.provider_connections_path(brand_dir),
        )
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
            brand_dir=brand_dir,
        )
        artifact = Path(tmpdir.name) / "posthog.json"
        artifact.write_text("{}", encoding="utf-8")
        audit["rows"][0].update(
            {
                "status": "pass",
                "evidence_source": "posthog",
                "artifact_ref": str(artifact),
                "result": "Verified with PostHog.",
                "blocker": "",
                "next_action": "",
            }
        )

        self.assertEqual(
            seo_audit_harness.validate_audit(compiled, audit, strict_evidence=True),
            [],
        )
        audit["rows"][0]["evidence_source"] = "ga4"
        self.assertTrue(
            any(
                "evidence_source must include" in error
                for error in seo_audit_harness.validate_audit(
                    compiled,
                    audit,
                    strict_evidence=True,
                )
            )
        )

    def test_strict_verify_respects_ga4_provider(self):
        path = self.make_checklist(
            """# Analytics Checklist

## Analytics

Evidence sources: `GA4`, `PostHog`.

- [ ] Organic conversions are reviewed.
"""
        )
        compiled = seo_audit_harness.compile_checklists([str(path)])
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "references").mkdir()
        seo_audit_harness.write_json(
            {"providers": {"analytics": ["ga4"]}},
            seo_audit_harness.provider_connections_path(brand_dir),
        )
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
            brand_dir=brand_dir,
        )
        artifact = Path(tmpdir.name) / "ga4.json"
        artifact.write_text("{}", encoding="utf-8")
        audit["rows"][0].update(
            {
                "status": "pass",
                "evidence_source": "ga4",
                "artifact_ref": str(artifact),
                "result": "Verified with GA4.",
                "blocker": "",
                "next_action": "",
            }
        )

        self.assertEqual(
            seo_audit_harness.validate_audit(compiled, audit, strict_evidence=True),
            [],
        )
        audit["rows"][0]["evidence_source"] = "posthog"
        self.assertTrue(
            any(
                "evidence_source must include" in error
                for error in seo_audit_harness.validate_audit(
                    compiled,
                    audit,
                    strict_evidence=True,
                )
            )
        )

    def test_strict_verify_fails_missing_artifact_file(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )
        audit["rows"][0].update(
            {
                "status": "pass",
                "evidence_source": "gsc",
                "artifact_ref": "missing-gsc.json",
                "result": "Verified with GSC.",
                "blocker": "",
                "next_action": "",
            }
        )

        errors = seo_audit_harness.validate_audit(
            compiled,
            audit,
            strict_evidence=True,
        )

        self.assertTrue(any("artifact_ref does not exist" in error for error in errors))

    def test_strict_verify_fails_unsupported_source_without_blocker(self):
        path = self.make_checklist(
            """# Sample Checklist

## Source Section

Evidence sources: `CMS/code`.

- [ ] Governance source is checked.
"""
        )
        compiled = seo_audit_harness.compile_checklists([str(path)])
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )
        audit["rows"][0]["blocker"] = ""

        errors = seo_audit_harness.validate_audit(
            compiled,
            audit,
            strict_evidence=True,
        )

        self.assertTrue(any("blocked needs nonempty blocker" in error for error in errors))

    def test_google_visible_resolver_uses_site_checks_and_marks_process_rows_na(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "title_present",
                        "url": "https://example.com",
                        "severity": "medium",
                        "status": "fail",
                        "source": "firecrawl",
                        "artifact_ref": "site-checks.json",
                        "result": "Title missing.",
                        "next_action": "Add a title.",
                    },
                    {
                        "check_id": "rendered_browser_evidence_available",
                        "url": "https://example.com",
                        "severity": "low",
                        "status": "pass",
                        "source": "playwright",
                        "artifact_ref": "playwright.json",
                        "result": "Playwright evidence exists.",
                        "next_action": "",
                    }
                ]
            },
            run_dir / "site-checks.json",
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "full"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "title",
                        "item_text": "The title is present and clear.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Evidence not collected yet.",
                        "next_action": "Collect evidence.",
                        "candidate_sources": ["manual:cms-code", "firecrawl"],
                        "required_sources": ["manual:cms-code"],
                    },
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "sessions",
                        "item_text": "Organic sessions that fail the intended next step are flagged.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "PostHog missing.",
                        "next_action": "Collect analytics.",
                        "candidate_sources": ["posthog"],
                        "required_sources": ["posthog"],
                    },
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "rendered",
                        "item_text": "Rendered mobile content is visible to search engines.",
                        "status": "pass",
                        "evidence_source": "firecrawl",
                        "artifact_ref": str(run_dir / "site-checks.json"),
                        "result": "Rendered content was captured in public crawl evidence.",
                        "blocker": "",
                        "next_action": "",
                        "candidate_sources": ["playwright"],
                        "required_sources": ["playwright"],
                    },
                ],
            },
            audit_path,
        )

        result = seo_audit_harness.resolve_google_visible_audit(
            brand_dir,
            "run",
            audit_path,
        )
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(result["resolved_rows"], 3)
        self.assertEqual(audit["metadata"]["scope"], seo_audit_harness.GOOGLE_VISIBLE_SCOPE)
        self.assertEqual(audit["rows"][0]["status"], "fail")
        self.assertEqual(audit["rows"][0]["evidence_source"], "firecrawl")
        self.assertEqual(audit["rows"][1]["status"], "not_applicable")
        self.assertEqual(audit["rows"][2]["status"], "pass")

    def test_route_evidence_updates_routes_without_changing_status(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "references").mkdir(parents=True)
        seo_audit_harness.write_json(
            {"providers": {"analytics": ["posthog"]}},
            seo_audit_harness.provider_connections_path(brand_dir),
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "page", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "analytics",
                        "item_text": "Organic conversions are reviewed.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Evidence missing.",
                        "next_action": "Collect analytics.",
                        "candidate_sources": ["analytics"],
                        "required_sources": [],
                    }
                ],
            },
            audit_path,
        )

        result = seo_audit_harness.route_evidence_audit(brand_dir, audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(result["routed_rows"], 1)
        self.assertEqual(audit["rows"][0]["status"], "not_checked_blocked")
        self.assertEqual(audit["rows"][0]["logical_required_sources"], ["analytics"])
        self.assertEqual(audit["rows"][0]["required_sources"], ["posthog"])

    def test_collect_evidence_uses_fake_collectors(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)

        def fake_collector(source):
            def collect(context):
                artifact = seo_audit_harness.write_evidence_artifact(
                    context["target_dir"],
                    "{}.json".format(source),
                    {"source": source},
                )
                return seo_audit_harness.source_result(
                    source,
                    "success",
                    artifact,
                    summary="fake {}".format(source),
                )
            return collect

        collectors = {
            source: fake_collector(source)
            for source in (
                "firecrawl",
                "playwright",
                "lighthouse",
                "pagespeed",
                "crux",
                "gsc",
                "keyword_planner",
                "posthog",
            )
        }

        result = seo_audit_harness.collect_evidence(
            brand_dir,
            "https://example.com",
            run_id="test-run",
            collectors=collectors,
        )

        manifest = seo_audit_harness.read_json(result["manifest_path"])
        self.assertEqual(manifest["run_id"], "test-run")
        self.assertEqual(
            sorted(manifest["sources"]),
            sorted(collectors),
        )
        self.assertTrue(
            Path(manifest["sources"]["firecrawl"]["artifact"]).exists()
        )

    def test_lighthouse_falls_back_to_pagespeed_lighthouse(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        captured = {}

        def fake_runner(command, capture_output, text, check, env):
            return subprocess.CompletedProcess(command, 1, "", "local lighthouse failed")

        def fake_open(api_request, timeout):
            captured["url"] = api_request.full_url
            return FakeResponse(
                seo_audit_harness.json.dumps(
                    {
                        "lighthouseResult": {
                            "finalUrl": "https://example.com/",
                            "categories": {"performance": {"score": 0.91}},
                            "audits": {
                                "largest-contentful-paint": {
                                    "numericValue": 1200
                                }
                            },
                        }
                    }
                )
            )

        with mock.patch.object(seo_audit_harness, "load_local_env"):
            with mock.patch.dict(
                seo_audit_harness.os.environ,
                {"GOOGLE_API_KEY": "test-key"},
                clear=True,
            ):
                result = seo_audit_harness.collect_lighthouse_source(
                    {
                        "url": "https://example.com",
                        "target_dir": tmpdir.name,
                        "runner": fake_runner,
                        "open_url": fake_open,
                    }
                )

        data = seo_audit_harness.read_json(result["artifact"])
        self.assertEqual(result["status"], "success")
        self.assertEqual(data["categories"]["performance"], 0.91)
        self.assertEqual(data["fallback"]["source"], "pagespeed_lighthouse")
        self.assertIn("runPagespeed", captured["url"])

    def test_record_evidence_updates_audit_row(self):
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://example.com",
            "partial",
            strict_evidence=True,
        )
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        audit_path = Path(tmpdir.name) / "audit.json"
        artifact = Path(tmpdir.name) / "posthog.json"
        artifact.write_text("{}", encoding="utf-8")
        seo_audit_harness.write_json(audit, audit_path)

        result = seo_audit_harness.record_audit_evidence(
            audit_path,
            audit["rows"][0]["item_id"],
            "pass",
            "PostHog",
            str(artifact),
            "PostHog output recorded.",
            evidence_run_id="run-1",
        )

        updated = seo_audit_harness.read_json(audit_path)
        self.assertTrue(result["ok"])
        self.assertEqual(updated["rows"][0]["evidence_source"], "posthog")
        self.assertEqual(updated["rows"][0]["evidence_run_id"], "run-1")
        self.assertIn(str(artifact), updated["rows"][0]["evidence_artifacts"])

    def test_sitemap_discovery_handles_indexes(self):
        routes = {
            "https://www.example.com/robots.txt": (
                "Sitemap: https://www.example.com/sitemap-index.xml"
            ),
            "https://www.example.com/sitemap.xml": "<urlset></urlset>",
            "https://www.example.com/sitemap-index.xml": (
                "<sitemapindex><sitemap><loc>https://www.example.com/pages.xml</loc></sitemap></sitemapindex>"
            ),
            "https://www.example.com/pages.xml": (
                "<urlset>"
                "<url><loc>https://www.example.com/about</loc></url>"
                "<url><loc>https://www.example.com/file.pdf</loc></url>"
                "<url><loc>https://other.example.com/offsite</loc></url>"
                "</urlset>"
            ),
        }

        def fake_open(api_request, timeout):
            return FakeResponse(routes[api_request.full_url])

        result = seo_audit_harness.discover_sitemap_pages(
            "https://www.example.com", open_url=fake_open
        )

        self.assertEqual(result["pages"], ["https://www.example.com/about"])
        self.assertIn("https://www.example.com/pages.xml", result["sitemaps"])

    def test_crawl_site_discovers_same_host_internal_links(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)

        def fake_open(api_request, timeout):
            if api_request.full_url.endswith("robots.txt"):
                return FakeResponse("")
            return FakeResponse("<urlset></urlset>")

        def fake_scrape(url, **kwargs):
            links = []
            if url == "https://www.example.com/":
                links = [
                    "https://example.com/about",
                    "https://external.com/offsite",
                    "https://www.example.com/logo.png",
                ]
            return {
                "status": 200,
                "headers": {"content-type": "text/html"},
                "rendered_html": (
                    "<html><head><title>{}</title><meta name='description' content='Desc'>"
                    "<link rel='canonical' href='{}'></head><body><h1>One</h1>"
                    "<script type='application/ld+json'>{{\"@type\":\"WebPage\"}}</script>"
                    "<a href='/pricing'>Pricing</a></body></html>"
                ).format(url, url),
                "raw_html": "",
                "rendered_text": "One page content",
                "links": links,
                "images": [],
                "metadata": {},
            }

        result = seo_audit_harness.crawl_site(
            tmpdir.name,
            "https://www.example.com/",
            run_id="crawl",
            scrape=fake_scrape,
            open_url=fake_open,
        )
        fields, rows = seo_audit_harness.read_csv_dict_rows(result["inventory_path"])
        urls = sorted(row["url"] for row in rows)

        self.assertIn("https://example.com/about", urls)
        self.assertIn("https://www.example.com/pricing", urls)
        self.assertNotIn("https://external.com/offsite", urls)
        self.assertNotIn("https://www.example.com/logo.png", urls)

    def test_crawl_url_normalization_and_max_pages(self):
        normalized = seo_audit_harness.normalize_crawl_url(
            "https://www.EXAMPLE.com/Page?utm_source=x&keep=1#frag"
        )
        self.assertEqual(normalized, "https://www.example.com/Page?keep=1")
        self.assertEqual(
            seo_audit_harness.crawl_url_key("https://www.example.com/Page"),
            seo_audit_harness.crawl_url_key("https://example.com/page"),
        )
        self.assertEqual(
            seo_audit_harness.normalize_crawl_url("https://www.example.com/a.pdf"),
            "",
        )

        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)

        def fake_open(api_request, timeout):
            return FakeResponse("<urlset></urlset>")

        def fake_scrape(url, **kwargs):
            return {
                "status": 200,
                "headers": {"content-type": "text/html"},
                "rendered_html": "<title>Home</title><h1>Home</h1><a href='/a'>A</a>",
                "raw_html": "",
                "rendered_text": "Home",
                "links": ["/b"],
                "images": [],
                "metadata": {},
            }

        result = seo_audit_harness.crawl_site(
            tmpdir.name,
            "https://www.example.com",
            run_id="limited",
            max_pages=1,
            scrape=fake_scrape,
            open_url=fake_open,
        )
        fields, rows = seo_audit_harness.read_csv_dict_rows(result["inventory_path"])
        self.assertEqual(len(rows), 1)

    def test_crawl_site_resumes_existing_run(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        calls = []

        def fake_open(api_request, timeout):
            return FakeResponse("<urlset></urlset>")

        def fake_scrape(url, **kwargs):
            calls.append(url)
            return {
                "status": 200,
                "headers": {"content-type": "text/html"},
                "rendered_html": "<title>Home</title><h1>Home</h1>",
                "raw_html": "",
                "rendered_text": "Home",
                "links": [],
                "images": [],
                "metadata": {},
            }

        seo_audit_harness.crawl_site(
            tmpdir.name,
            "https://www.example.com",
            run_id="resume",
            scrape=fake_scrape,
            open_url=fake_open,
        )
        second = seo_audit_harness.crawl_site(
            tmpdir.name,
            "https://www.example.com",
            run_id="resume",
            scrape=fake_scrape,
            open_url=fake_open,
        )

        manifest = seo_audit_harness.read_json(second["manifest_path"])
        self.assertTrue(manifest["resumed"])
        self.assertEqual(calls, ["https://www.example.com/"])

    def test_collect_site_evidence_uses_fake_per_page_collectors(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "references").mkdir()
        seo_audit_harness.write_json(
            {"providers": {"analytics": ["posthog"]}},
            seo_audit_harness.provider_connections_path(brand_dir),
        )

        def fake_open(api_request, timeout):
            return FakeResponse("<urlset></urlset>")

        def fake_scrape(url, **kwargs):
            return {
                "status": 200,
                "headers": {"content-type": "text/html"},
                "rendered_html": "<title>Home</title><h1>Home</h1><a href='/a'>A</a>",
                "raw_html": "",
                "rendered_text": "Home",
                "links": [],
                "images": [],
                "metadata": {},
            }

        def fake_collector(source):
            def collect(context):
                artifact = seo_audit_harness.write_evidence_artifact(
                    context["target_dir"], "{}.json".format(source), {"url": context["url"]}
                )
                return seo_audit_harness.source_result(source, "success", artifact)
            return collect

        result = seo_audit_harness.collect_site_evidence(
            brand_dir,
            "https://www.example.com",
            run_id="site",
            page_collectors={"firecrawl": fake_collector("firecrawl")},
            site_collectors={"posthog": fake_collector("posthog")},
            scrape=fake_scrape,
            open_url=fake_open,
        )

        manifest = seo_audit_harness.read_json(result["manifest_path"])
        self.assertEqual(manifest["mode"], "site")
        self.assertEqual(
            manifest["provider_status"]["analytics"],
            [{"provider": "posthog", "status": "success"}],
        )
        self.assertEqual(len(manifest["pages"]), 2)
        for page in manifest["pages"].values():
            self.assertIn("firecrawl", page["sources"])

    def test_site_page_maps_group_gsc_and_keyword_rows(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        target_dir = brand_dir / "references" / "evidence" / "run"
        target_dir.mkdir(parents=True)
        (brand_dir / "exports").mkdir(parents=True)
        inventory_rows = [
            {
                "url": "https://www.example.com/product",
                "normalized_url": seo_audit_harness.crawl_url_key(
                    "https://www.example.com/product"
                ),
            }
        ]
        gsc_artifact = target_dir / "gsc.json"
        seo_audit_harness.write_json(
            {
                "rows": [
                    {
                        "keyword": "ai marketing",
                        "page": "https://example.com/product",
                    }
                ]
            },
            gsc_artifact,
        )
        keyword_row = self.keyword_row("ai marketing", priority="high")
        keyword_row["target_url"] = "https://www.example.com/product"
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.keyword_universe_path(brand_dir),
            seo_audit_harness.KEYWORD_UNIVERSE_FIELDS,
            [keyword_row],
        )

        maps = seo_audit_harness.write_site_page_maps(
            target_dir,
            brand_dir,
            inventory_rows,
            {"gsc": {"artifact": str(gsc_artifact)}},
        )

        gsc_map = seo_audit_harness.read_json(maps["gsc"])
        keyword_map = seo_audit_harness.read_json(maps["keyword_planner"])
        key = seo_audit_harness.crawl_url_key("https://www.example.com/product")
        self.assertEqual(gsc_map["pages"][key][0]["keyword"], "ai marketing")
        self.assertEqual(keyword_map["pages"][key][0]["keyword"], "ai marketing")

    def test_collect_gsc_source_writes_expanded_artifacts_with_fake_runner(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        target_dir = Path(tmpdir.name)
        calls = []

        def fake_runner(command, capture_output, text, check):
            calls.append(command)
            tool = command[2]
            payload = seo_audit_harness.json.loads(command[4])
            if tool == seo_audit_harness.GSC_LIST_SITES_TOOL:
                data = {
                    "siteEntry": [
                        {"siteUrl": "https://www.example.com/"},
                        {"siteUrl": "sc-domain:example.com"},
                    ]
                }
            elif tool == seo_audit_harness.GSC_GET_SITE_TOOL:
                data = {"siteUrl": payload["site_url"], "permissionLevel": "siteOwner"}
            elif tool == seo_audit_harness.GSC_SEARCH_ANALYTICS_TOOL:
                dims = payload["dimensions"]
                values = {
                    "query": "ai marketing",
                    "page": "https://www.example.com/",
                    "country": "usa",
                    "date": "2026-06-01",
                    "searchAppearance": "WEB_RESULT",
                }
                data = {
                    "rows": [
                        {
                            "keys": [values[dimension] for dimension in dims],
                            "clicks": 1,
                            "impressions": 10,
                            "ctr": 0.1,
                            "position": 2.0,
                        }
                    ]
                }
            elif tool == seo_audit_harness.GSC_LIST_SITEMAPS_TOOL:
                data = {"sitemap": [{"path": "https://www.example.com/sitemap.xml"}]}
            elif tool == seo_audit_harness.GSC_GET_SITEMAP_TOOL:
                data = {"path": payload["feedpath"], "isPending": False}
            elif tool == seo_audit_harness.GSC_INSPECT_URL_TOOL:
                data = {"inspectionResult": {"indexStatusResult": {"coverageState": "Indexed"}}}
            else:
                data = {}
            stdout = seo_audit_harness.json.dumps({"successful": True, "data": data})
            return subprocess.CompletedProcess(command, 0, stdout, "")

        result = seo_audit_harness.collect_gsc_source(
            {
                "target_dir": str(target_dir),
                "url": "https://www.example.com",
                "runner": fake_runner,
                "inventory_rows": [
                    {
                        "url": "https://www.example.com/",
                        "in_sitemap": "yes",
                        "depth": "0",
                    }
                ],
            }
        )
        data = seo_audit_harness.read_json(result["artifact"])

        self.assertEqual(data["site"], "sc-domain:example.com")
        self.assertEqual(data["row_count"], 2)
        self.assertIn("query_page_date", data["properties"]["sc-domain:example.com"]["dimension_sets"])
        self.assertEqual(data["sitemaps"]["row_count"], 1)
        self.assertEqual(data["url_inspections"]["row_count"], 1)
        self.assertTrue(
            any(call[2] == seo_audit_harness.GSC_INSPECT_URL_TOOL for call in calls)
        )

    def test_fetch_gsc_dimension_rows_honors_max_rows(self):
        calls = []

        def fake_runner(command, capture_output, text, check):
            calls.append(command)
            payload = seo_audit_harness.json.loads(command[4])
            rows = [
                {
                    "keys": ["query {}".format(payload["start_row"] + index), "https://example.com/"],
                    "clicks": 1,
                    "impressions": 10,
                    "ctr": 0.1,
                    "position": 2.0,
                }
                for index in range(payload["row_limit"])
            ]
            stdout = seo_audit_harness.json.dumps(
                {"successful": True, "data": {"rows": rows}}
            )
            return subprocess.CompletedProcess(command, 0, stdout, "")

        rows = seo_audit_harness.fetch_gsc_dimension_rows(
            "sc-domain:example.com",
            "2026-01-01",
            "2026-01-31",
            ["query", "page"],
            runner=fake_runner,
            row_limit=2,
            max_rows=2,
        )

        self.assertEqual(len(rows), 2)
        self.assertEqual(len(calls), 1)

    def test_site_checks_detect_common_failures(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        (page_dir / "firecrawl.json").write_text(
            seo_audit_harness.json.dumps({"links": ["https://www.example.com/broken"]}),
            encoding="utf-8",
        )
        lighthouse_dir = brand_dir / "references" / "evidence" / "run" / "pages" / "one"
        lighthouse_dir.mkdir(parents=True)
        lighthouse_path = lighthouse_dir / "lighthouse.json"
        lighthouse_path.write_text(
            seo_audit_harness.json.dumps({"categories": {"performance": 0.5}}),
            encoding="utf-8",
        )
        rows = [
            {
                "url": "https://www.example.com/",
                "normalized_url": seo_audit_harness.crawl_url_key("https://www.example.com/"),
                "status": "success",
                "status_code": "200",
                "content_type": "text/html",
                "indexable": "no",
                "canonical": "https://www.example.com/wrong",
                "title": "",
                "meta_description": "",
                "h1_count": "2",
                "word_count": "10",
                "internal_link_count": "1",
                "external_link_count": "0",
                "image_count": "1",
                "images_missing_alt_count": "1",
                "schema_types": "",
                "depth": "0",
                "parent_url": "",
                "source": "seed",
                "in_sitemap": "no",
                "artifact_dir": str(page_dir),
                "blocker": "",
                "last_seen": "now",
            },
            {
                "url": "https://www.example.com/broken",
                "normalized_url": seo_audit_harness.crawl_url_key("https://www.example.com/broken"),
                "status": "success",
                "status_code": "404",
                "content_type": "text/html",
                "indexable": "no",
                "canonical": "",
                "title": "Duplicate",
                "meta_description": "Duplicate",
                "h1_count": "1",
                "word_count": "10",
                "internal_link_count": "0",
                "external_link_count": "0",
                "image_count": "0",
                "images_missing_alt_count": "0",
                "schema_types": "WebPage",
                "depth": "1",
                "parent_url": "https://www.example.com/",
                "source": "internal_link",
                "in_sitemap": "yes",
                "artifact_dir": str(page_dir),
                "blocker": "",
                "last_seen": "now",
            },
            {
                "url": "https://www.example.com/dupe",
                "normalized_url": seo_audit_harness.crawl_url_key("https://www.example.com/dupe"),
                "status": "success",
                "status_code": "200",
                "content_type": "text/html",
                "indexable": "yes",
                "canonical": "",
                "title": "Duplicate",
                "meta_description": "Duplicate",
                "h1_count": "1",
                "word_count": "10",
                "internal_link_count": "0",
                "external_link_count": "0",
                "image_count": "0",
                "images_missing_alt_count": "0",
                "schema_types": "WebPage",
                "depth": "1",
                "parent_url": "https://www.example.com/",
                "source": "internal_link",
                "in_sitemap": "yes",
                "artifact_dir": str(page_dir),
                "blocker": "",
                "last_seen": "now",
            },
        ]
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            rows,
        )
        seo_audit_harness.write_json(
            {
                "pages": {
                    "https://www.example.com/": {
                        "sources": {
                            "lighthouse": {
                                "artifact": str(lighthouse_path),
                                "status": "success",
                            }
                        }
                    }
                }
            },
            brand_dir / "references" / "evidence" / "run" / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        failing_ids = {check["check_id"] for check in checks if check["status"] == "fail"}

        self.assertTrue(
            {
                "title_present",
                "meta_description_present",
                "single_h1",
                "indexable",
                "canonical_match",
                "schema_present",
                "image_alt_text",
                "sitemap_inclusion",
                "performance_score",
                "duplicate_title",
                "duplicate_meta_description",
                "broken_internal_link",
            }.issubset(failing_ids)
        )

    def test_site_checks_import_playwright_assertions(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        playwright_dir = brand_dir / "references" / "evidence" / "run" / "pages" / "one"
        playwright_dir.mkdir(parents=True)
        playwright_path = playwright_dir / "playwright.json"
        seo_audit_harness.write_json(
            {
                "assertions": {
                    "tap_targets": {
                        "status": "fail",
                        "result": "Small tap target found.",
                        "next_action": "Increase tap target size.",
                        "viewport": "mobile",
                        "samples": ["button Buy"],
                    },
                    "table_semantics": {
                        "status": "not_applicable",
                        "result": "No visible tables found.",
                        "viewport": "both",
                        "samples": [],
                    },
                    "color_contrast": {
                        "status": "pass",
                        "result": "Sampled text meets contrast thresholds.",
                        "viewport": "both",
                        "samples": [],
                    },
                }
            },
            playwright_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {
                "pages": {
                    page_url: {
                        "sources": {
                            "playwright": {
                                "artifact": str(playwright_path),
                                "status": "success",
                            }
                        }
                    }
                }
            },
            brand_dir / "references" / "evidence" / "run" / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["tap_targets"]["status"], "fail")
        self.assertEqual(by_id["tap_targets"]["source"], "playwright")
        self.assertEqual(by_id["table_semantics"]["status"], "not_applicable")
        self.assertEqual(by_id["table_semantics"]["next_action"], "")
        self.assertEqual(by_id["color_contrast"]["status"], "pass")

    def test_lighthouse_summary_preserves_diagnostics(self):
        summary = seo_audit_harness.lighthouse_summary(
            {
                "finalUrl": "https://www.example.com/",
                "categories": {"performance": {"score": 0.8}},
                "audits": {
                    "render-blocking-resources": {"score": 0, "details": {"items": []}},
                    "unused-css-rules": {"score": 0.5, "details": {"items": []}},
                    "font-display": {"score": 1},
                    "third-party-summary": {"score": 0, "details": {"items": []}},
                    "not-needed": {"score": 0},
                },
            }
        )

        self.assertIn("render-blocking-resources", summary["audits"])
        self.assertIn("unused-css-rules", summary["audits"])
        self.assertIn("font-display", summary["audits"])
        self.assertIn("third-party-summary", summary["audits"])
        self.assertNotIn("not-needed", summary["audits"])

    def test_site_checks_emit_remaining_playwright_routed_diagnostics(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        evidence_dir = brand_dir / "references" / "evidence" / "run" / "pages" / "one"
        evidence_dir.mkdir(parents=True)
        lighthouse_path = evidence_dir / "lighthouse.json"
        playwright_path = evidence_dir / "playwright.json"
        seo_audit_harness.write_json(
            {
                "categories": {"performance": 0.5},
                "audits": {
                    "render-blocking-resources": {
                        "score": 0,
                        "details": {"items": [{"url": "https://cdn.example.net/app.js"}]},
                    },
                    "unused-css-rules": {
                        "score": 0,
                        "details": {"items": [{"url": "https://www.example.com/app.css"}]},
                    },
                    "font-display": {
                        "score": 0,
                        "details": {"items": [{"url": "https://www.example.com/font.woff2"}]},
                    },
                    "third-party-summary": {
                        "score": 0,
                        "details": {
                            "items": [
                                {
                                    "entity": "Example Analytics",
                                    "transferSize": 900000,
                                    "blockingTime": 300,
                                    "mainThreadTime": 700,
                                }
                            ]
                        },
                    },
                    "bootup-time": {"score": 1, "details": {"items": []}},
                },
            },
            lighthouse_path,
        )
        seo_audit_harness.write_json(
            {
                "desktop": {
                    "jsonLd": [
                        seo_audit_harness.json.dumps(
                            {"@context": "https://schema.org", "@type": "Product"}
                        )
                    ],
                    "scripts": [
                        {
                            "src": "https://cdn.example.net/app.js",
                            "async": False,
                            "defer": False,
                            "type": "",
                        }
                    ],
                },
                "mobile": {"jsonLd": [], "scripts": []},
            },
            playwright_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "Product",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {
                "pages": {
                    page_url: {
                        "sources": {
                            "lighthouse": {"artifact": str(lighthouse_path), "status": "success"},
                            "playwright": {"artifact": str(playwright_path), "status": "success"},
                        }
                    }
                }
            },
            brand_dir / "references" / "evidence" / "run" / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["rich_result_properties"]["status"], "fail")
        self.assertEqual(by_id["critical_css_font_loading"]["status"], "fail")
        self.assertEqual(by_id["render_blocking_scripts"]["status"], "fail")
        self.assertEqual(by_id["third_party_script_weight"]["status"], "fail")
        self.assertEqual(by_id["lab_root_cause_diagnostics"]["status"], "pass")

    def test_rich_result_properties_not_applicable_without_supported_type(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        evidence_dir = brand_dir / "references" / "evidence" / "run" / "pages" / "one"
        evidence_dir.mkdir(parents=True)
        playwright_path = evidence_dir / "playwright.json"
        seo_audit_harness.write_json(
            {
                "desktop": {
                    "jsonLd": [
                        seo_audit_harness.json.dumps(
                            {"@context": "https://schema.org", "@type": "WebSite", "name": "Example"}
                        )
                    ]
                },
                "mobile": {"jsonLd": []},
            },
            playwright_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebSite",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {
                "pages": {
                    page_url: {
                        "sources": {
                            "playwright": {"artifact": str(playwright_path), "status": "success"},
                        }
                    }
                }
            },
            brand_dir / "references" / "evidence" / "run" / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["rich_result_properties"]["status"], "not_applicable")

    def test_site_checks_ignore_simplified_gsc_artifact_for_gsc_checks(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        gsc_dir = brand_dir / "references" / "evidence" / "run"
        gsc_dir.mkdir(parents=True)
        gsc_path = gsc_dir / "gsc.json"
        seo_audit_harness.write_json(
            {"site": "sc-domain:example.com", "row_count": 1, "rows": [{"query": "example"}]},
            gsc_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {"target_url": page_url, "sources": {"gsc": {"artifact": str(gsc_path), "status": "success"}}},
            gsc_dir / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        ids = {check["check_id"] for check in checks}

        self.assertNotIn("gsc_url_inspection_indexing", ids)
        self.assertNotIn("gsc_query_drift", ids)

    def test_site_checks_emit_gsc_derived_checks_from_full_artifact(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        gsc_dir = brand_dir / "references" / "evidence" / "run"
        gsc_dir.mkdir(parents=True)
        gsc_path = gsc_dir / "gsc.json"
        seo_audit_harness.write_json(
            {
                "site": "sc-domain:example.com",
                "properties": {
                    "sc-domain:example.com": {
                        "dimension_sets": {
                            "query_page_country": {
                                "rows": [{"query": "example guide", "page": page_url, "country": "usa"}],
                            },
                            "query_page_date": {
                                "rows": [{"query": "example guide", "page": page_url, "date": "2026-01-01"}],
                            },
                            "page_date": {
                                "rows": [{"page": page_url, "date": "2026-01-01"}],
                            },
                            "search_appearance_page": {
                                "rows": [{"searchAppearance": "Rich results", "page": page_url}],
                            },
                        }
                    }
                },
                "sitemaps": {"row_count": 1, "rows": []},
                "url_inspections": {
                    "row_count": 1,
                    "rows": {
                        page_url: {
                            "inspectionResult": {
                                "indexStatusResult": {
                                    "coverageState": "Indexed, not submitted in sitemap",
                                    "verdict": "PASS",
                                }
                            }
                        }
                    },
                },
            },
            gsc_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {"target_url": page_url, "sources": {"gsc": {"artifact": str(gsc_path), "status": "success"}}},
            gsc_dir / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["gsc_url_inspection_indexing"]["status"], "pass")
        self.assertEqual(by_id["gsc_search_appearance_review"]["status"], "pass")
        self.assertEqual(by_id["gsc_measurement_coverage"]["status"], "pass")
        self.assertEqual(by_id["gsc_landing_page_performance"]["status"], "pass")
        self.assertEqual(by_id["gsc_query_drift"]["status"], "pass")
        self.assertEqual(by_id["gsc_decay"]["status"], "pass")
        self.assertEqual(by_id["gsc_serp_expectation"]["status"], "pass")

    def test_site_checks_emit_public_http_and_scope_checks(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        evidence_dir = brand_dir / "references" / "evidence" / "run"
        evidence_dir.mkdir(parents=True)
        public_http_path = evidence_dir / "public-http.json"
        seo_audit_harness.write_json(
            {
                "url": page_url,
                "status": 200,
                "headers": {"strict-transport-security": "max-age=31536000"},
                "tls": {"valid": True, "days_remaining": 90},
            },
            public_http_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {
                "target_url": page_url,
                "sources": {
                    "public_http": {"artifact": str(public_http_path), "status": "success"},
                },
            },
            evidence_dir / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["tls_certificate_valid"]["status"], "pass")
        self.assertEqual(by_id["hsts_header_present"]["status"], "pass")
        self.assertEqual(by_id["redirect_chain_valid"]["status"], "not_applicable")
        self.assertEqual(by_id["non_html_asset_inventory"]["status"], "not_applicable")
        self.assertEqual(by_id["non_production_canonical"]["status"], "not_applicable")

    def test_site_checks_emit_source_availability_checks(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        evidence_dir = brand_dir / "references" / "evidence" / "run"
        page_evidence_dir = evidence_dir / "pages" / "one"
        page_evidence_dir.mkdir(parents=True)
        playwright_path = page_evidence_dir / "playwright.json"
        lighthouse_path = page_evidence_dir / "lighthouse.json"
        keyword_path = evidence_dir / "keyword_planner.json"
        for path in (playwright_path, lighthouse_path, keyword_path):
            seo_audit_harness.write_json({}, path)
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "1",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {
                "target_url": page_url,
                "sources": {
                    "keyword_planner": {"artifact": str(keyword_path), "status": "success"},
                },
                "pages": {
                    page_url: {
                        "sources": {
                            "playwright": {"artifact": str(playwright_path), "status": "success"},
                            "lighthouse": {"artifact": str(lighthouse_path), "status": "success"},
                        }
                    }
                },
            },
            evidence_dir / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["public_crawl_evidence_available"]["status"], "pass")
        self.assertEqual(by_id["rendered_browser_evidence_available"]["status"], "pass")
        self.assertEqual(by_id["performance_evidence_available"]["status"], "pass")
        self.assertEqual(by_id["keyword_demand_evidence_available"]["status"], "pass")

    def test_public_http_evidence_falls_back_to_get_after_head_error(self):
        calls = []

        class HeaderResponse:
            status = 200
            headers = {"Strict-Transport-Security": "max-age=31536000"}

            def __enter__(self):
                return self

            def __exit__(self, exc_type, exc, traceback):
                return False

            def getcode(self):
                return 200

            def geturl(self):
                return "http://www.example.com/"

        def fake_open(api_request, timeout):
            calls.append(api_request.get_method())
            if api_request.get_method() == "HEAD":
                raise seo_audit_harness.error.HTTPError(
                    api_request.full_url,
                    403,
                    "Forbidden",
                    {},
                    io.BytesIO(b""),
                )
            return HeaderResponse()

        data = seo_audit_harness.fetch_public_http_evidence(
            "http://www.example.com/",
            open_url=fake_open,
        )

        self.assertEqual(calls, ["HEAD", "GET"])
        self.assertEqual(data["status"], 200)
        self.assertEqual(data["headers"]["strict-transport-security"], "max-age=31536000")
        self.assertEqual(data["blocker"], "")

    def test_site_checks_fail_gsc_url_inspection_not_indexed(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        page_url = "https://www.example.com/"
        page_dir = brand_dir / "references" / "crawls" / "run" / "pages" / "one"
        page_dir.mkdir(parents=True)
        gsc_dir = brand_dir / "references" / "evidence" / "run"
        gsc_dir.mkdir(parents=True)
        gsc_path = gsc_dir / "gsc.json"
        seo_audit_harness.write_json(
            {
                "site": "sc-domain:example.com",
                "properties": {"sc-domain:example.com": {"dimension_sets": {}}},
                "sitemaps": {"row_count": 0, "rows": []},
                "url_inspections": {
                    "row_count": 1,
                    "rows": {
                        page_url: {
                            "inspectionResult": {
                                "indexStatusResult": {
                                    "coverageState": "Not indexed",
                                    "verdict": "FAIL",
                                }
                            }
                        }
                    },
                },
            },
            gsc_path,
        )
        row = {
            "url": page_url,
            "normalized_url": seo_audit_harness.crawl_url_key(page_url),
            "status": "success",
            "status_code": "200",
            "content_type": "text/html",
            "indexable": "yes",
            "canonical": page_url,
            "title": "Example",
            "meta_description": "Example description",
            "h1_count": "1",
            "word_count": "100",
            "internal_link_count": "0",
            "external_link_count": "0",
            "image_count": "0",
            "images_missing_alt_count": "0",
            "schema_types": "WebPage",
            "depth": "0",
            "parent_url": "",
            "source": "seed",
            "in_sitemap": "yes",
            "artifact_dir": str(page_dir),
            "blocker": "",
            "last_seen": "now",
        }
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [row],
        )
        seo_audit_harness.write_json(
            {"target_url": page_url, "sources": {"gsc": {"artifact": str(gsc_path), "status": "success"}}},
            gsc_dir / "manifest.json",
        )

        result = seo_audit_harness.run_site_checks(brand_dir, "run")
        _fields, checks = seo_audit_harness.read_csv_dict_rows(result["site_checks_path"])
        by_id = {check["check_id"]: check for check in checks}

        self.assertEqual(by_id["gsc_url_inspection_indexing"]["status"], "fail")

    def test_google_visible_gsc_and_scope_mappings(self):
        mapping_cases = {
            "URL Inspection indexing status is reviewed for priority pages.": "gsc_url_inspection_indexing",
            "Search appearance is reviewed for rich result eligibility.": "gsc_search_appearance_review",
            "SERP expectations are compared against query/page evidence.": "gsc_serp_expectation",
            "Query drift is reviewed monthly.": "gsc_query_drift",
            "Decaying pages with lost clicks are reviewed.": "gsc_decay",
            "Search Console tracks queries, impressions, clicks, CTR, position, page indexing, enhancements, and Core Web Vitals.": "gsc_measurement_coverage",
            "Organic landing-page performance is reviewed by query, page, device, CTR, engagement, and conversion.": "gsc_landing_page_performance",
            "TLS certificate is valid.": "tls_certificate_valid",
            "HSTS header is present.": "hsts_header_present",
            "Non-HTML assets are inventoried.": "non_html_asset_inventory",
            "Non-HTML PDFs use X-Robots-Tag where needed.": "non_html_x_robots",
            "Crawl budget issues are investigated only when the site scale or crawl behavior justifies it.": "crawl_waste_review",
            "Images, videos, screenshots, tables, charts, templates, calculators, or code examples help the user complete the task.": "media_support_present",
            "Copy does not end with generic engagement-menu language such as let me know if you want.": "content_not_ai_slop",
            "URL paths avoid unnecessary IDs, dates, session IDs, tracking parameters, and internal implementation details.": "url_path_clean",
        }

        for text, expected in mapping_cases.items():
            with self.subTest(text=text):
                self.assertIn(expected, seo_audit_harness.google_visible_site_check_ids(text))

        for text in [
            "Bing Webmaster Tools is reviewed for coverage.",
            "Observed Google title matches the preferred title.",
            "Observed Google snippet validates the meta description.",
            "WAF and CDN bot rule governance is documented.",
            "Treating llms.txt as required for Google AI features.",
            "Private blog networks.",
        ]:
            with self.subTest(text=text):
                self.assertTrue(seo_audit_harness.google_visible_scope_not_applicable_item(text))

    def test_google_visible_resolver_marks_external_scope_rows_not_applicable(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        seo_audit_harness.write_json({"checks": []}, run_dir / "site-checks.json")
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "bing",
                        "item_text": "Bing Webmaster Tools is reviewed for coverage.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing Bing evidence.",
                        "next_action": "Connect Bing Webmaster Tools.",
                        "candidate_sources": ["BWT"],
                        "required_sources": ["manual:bing-webmaster"],
                    },
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "serp",
                        "item_text": "Observed Google title matches the preferred title.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing manual SERP evidence.",
                        "next_action": "Record SERP evidence.",
                        "candidate_sources": ["GSC"],
                        "required_sources": ["gsc"],
                    },
                ],
            },
            audit_path,
        )

        seo_audit_harness.resolve_google_visible_audit(brand_dir, "run", audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(audit["rows"][0]["status"], "not_applicable")
        self.assertEqual(audit["rows"][0]["evidence_source"], "scope")
        self.assertEqual(audit["rows"][1]["status"], "not_applicable")
        self.assertEqual(audit["rows"][1]["evidence_source"], "scope")

    def test_google_visible_resolver_replaces_invalid_old_source_from_site_checks(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        site_checks_path = run_dir / "site-checks.json"
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "gsc_measurement_coverage",
                        "url": "https://example.com",
                        "severity": "medium",
                        "status": "pass",
                        "source": "gsc",
                        "artifact_ref": "gsc.json",
                        "result": "GSC measurement evidence is present.",
                        "next_action": "",
                    }
                ]
            },
            site_checks_path,
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "gsc-measurement",
                        "item_text": "Search Console tracks queries, impressions, clicks, CTR, position, page indexing, enhancements, and Core Web Vitals.",
                        "status": "pass",
                        "evidence_source": "pagespeed",
                        "artifact_ref": "old-pagespeed.json",
                        "result": "Old source.",
                        "blocker": "",
                        "next_action": "",
                        "candidate_sources": ["GSC"],
                        "required_sources": ["gsc"],
                    }
                ],
            },
            audit_path,
        )

        seo_audit_harness.resolve_google_visible_audit(brand_dir, "run", audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(audit["rows"][0]["status"], "pass")
        self.assertEqual(audit["rows"][0]["evidence_source"], "gsc")
        self.assertEqual(audit["rows"][0]["artifact_ref"], str(site_checks_path))

    def test_google_visible_resolver_falls_back_to_source_availability_or_scope(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        site_checks_path = run_dir / "site-checks.json"
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "public_crawl_evidence_available",
                        "url": "https://example.com",
                        "severity": "low",
                        "status": "pass",
                        "source": "firecrawl",
                        "artifact_ref": "inventory.csv",
                        "result": "Public crawl evidence exists.",
                        "next_action": "",
                    },
                    {
                        "check_id": "content_visible",
                        "url": "https://example.com",
                        "severity": "high",
                        "status": "pass",
                        "source": "firecrawl",
                        "artifact_ref": "firecrawl.json",
                        "result": "Rendered public content is visible.",
                        "next_action": "",
                    }
                ]
            },
            site_checks_path,
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "public",
                        "item_text": "The page fully satisfies the main task or question.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing public content evidence.",
                        "next_action": "Collect public crawl evidence.",
                        "candidate_sources": ["Firecrawl"],
                        "required_sources": ["firecrawl"],
                    },
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "manual",
                        "item_text": "The business goal is defined by leadership.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing business context.",
                        "next_action": "Ask the business owner.",
                        "candidate_sources": ["Human/context"],
                        "required_sources": ["manual:human-context"],
                    },
                ],
            },
            audit_path,
        )

        seo_audit_harness.resolve_google_visible_audit(brand_dir, "run", audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(audit["rows"][0]["status"], "pass")
        self.assertEqual(audit["rows"][0]["evidence_source"], "firecrawl")
        self.assertEqual(audit["rows"][1]["status"], "not_applicable")
        self.assertEqual(audit["rows"][1]["evidence_source"], "scope")

    def test_google_visible_resolver_refreshes_old_scope_na_when_site_check_now_exists(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        site_checks_path = run_dir / "site-checks.json"
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "content_visible",
                        "url": "https://example.com",
                        "severity": "high",
                        "status": "pass",
                        "source": "firecrawl",
                        "artifact_ref": "firecrawl.json",
                        "result": "Rendered public content is visible.",
                        "next_action": "",
                    }
                ]
            },
            site_checks_path,
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "content",
                        "item_text": "Important content renders in HTML and is visible without fragile client-only behavior.",
                        "status": "not_applicable",
                        "evidence_source": "scope",
                        "artifact_ref": "",
                        "result": "Old broad scope NA.",
                        "blocker": "",
                        "next_action": "",
                        "candidate_sources": ["Firecrawl"],
                        "required_sources": ["firecrawl"],
                    }
                ],
            },
            audit_path,
        )

        seo_audit_harness.resolve_google_visible_audit(brand_dir, "run", audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(audit["rows"][0]["status"], "pass")
        self.assertEqual(audit["rows"][0]["evidence_source"], "firecrawl")
        self.assertEqual(audit["rows"][0]["artifact_ref"], str(site_checks_path))

    def test_resolve_google_visible_audits_command_batches_brand_audits(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        audits_dir = brand_dir / "audits"
        run_dir = brand_dir / "references" / "evidence" / "run"
        audits_dir.mkdir(parents=True)
        run_dir.mkdir(parents=True)
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "public_crawl_evidence_available",
                        "url": "https://example.com",
                        "severity": "low",
                        "status": "pass",
                        "source": "firecrawl",
                        "artifact_ref": "inventory.csv",
                        "result": "Public crawl evidence exists.",
                        "next_action": "",
                    },
                    {
                        "check_id": "content_visible",
                        "url": "https://example.com",
                        "severity": "high",
                        "status": "pass",
                        "source": "firecrawl",
                        "artifact_ref": "firecrawl.json",
                        "result": "Rendered public content is visible.",
                        "next_action": "",
                    }
                ]
            },
            run_dir / "site-checks.json",
        )
        row = {
            "checklist_id": "sample",
            "section_id": "sample",
            "item_id": "item",
            "item_text": "The page fully satisfies the main task or question.",
            "status": "not_checked_blocked",
            "evidence_source": "",
            "artifact_ref": "",
            "result": "",
            "blocker": "Missing public evidence.",
            "next_action": "Collect public evidence.",
            "candidate_sources": ["Firecrawl"],
            "required_sources": ["firecrawl"],
        }
        for name in ("one-google-visible-audit.json", "two-google-visible-audit.json"):
            seo_audit_harness.write_json(
                {"metadata": {"scope": "site", "audit_type": "partial"}, "rows": [dict(row)]},
                audits_dir / name,
            )
        output = brand_dir / "batch.json"

        args = type(
            "Args",
            (),
            {"brand_dir": str(brand_dir), "run_id": "run", "audit": None, "output": str(output)},
        )()
        exit_code = seo_audit_harness.command_resolve_google_visible_audits(args)

        self.assertEqual(exit_code, 0)
        result = seo_audit_harness.read_json(output)
        self.assertEqual(result["audit_count"], 2)
        for path in audits_dir.glob("*-google-visible-audit.json"):
            self.assertEqual(seo_audit_harness.read_json(path)["rows"][0]["status"], "pass")

    def test_remaining_playwright_routed_items_map_to_diagnostics(self):
        cases = {
            "Required and recommended properties are complete for the chosen rich result type.": "rich_result_properties",
            "Critical CSS and font loading are optimized.": "critical_css_font_loading",
            "Render-blocking scripts are reduced or deferred.": "render_blocking_scripts",
            "Heavy third-party scripts are justified and monitored.": "third_party_script_weight",
            "Lab tests are still used to debug root causes.": "lab_root_cause_diagnostics",
        }

        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertIn(expected, seo_audit_harness.google_visible_site_check_ids(text))

    def test_lab_test_route_uses_lab_provider_not_crux(self):
        route = seo_audit_harness.route_evidence_for_item(
            "Lab tests are still used to debug root causes.",
            ["playwright"],
            scope=seo_audit_harness.GOOGLE_VISIBLE_SCOPE,
            provider_connections=seo_audit_harness.normalize_provider_connections({}),
        )

        self.assertIn("lighthouse", route["required_sources"])
        self.assertIn("pagespeed", route["required_sources"])
        self.assertNotIn("crux", route["required_sources"])

    def test_google_visible_resolver_maps_accessibility_assertions(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "tap_targets",
                        "url": "https://example.com",
                        "severity": "medium",
                        "status": "fail",
                        "source": "playwright",
                        "artifact_ref": "playwright.json",
                        "result": "Small tap target found.",
                        "next_action": "Increase tap target size.",
                    },
                    {
                        "check_id": "table_semantics",
                        "url": "https://example.com",
                        "severity": "medium",
                        "status": "not_applicable",
                        "source": "playwright",
                        "artifact_ref": "playwright.json",
                        "result": "No visible tables found.",
                        "next_action": "",
                    },
                ]
            },
            run_dir / "site-checks.json",
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "tap",
                        "item_text": "Tap targets are large enough and not crowded.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing tap-target evidence.",
                        "next_action": "Add mobile tap-target checks.",
                        "candidate_sources": ["playwright"],
                        "required_sources": ["playwright"],
                    },
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "tables",
                        "item_text": "Tables are used for tabular data, not layout.",
                        "status": "not_checked_blocked",
                        "evidence_source": "",
                        "artifact_ref": "",
                        "result": "",
                        "blocker": "Missing table accessibility evidence.",
                        "next_action": "Run table checks.",
                        "candidate_sources": ["playwright"],
                        "required_sources": ["playwright"],
                    },
                ],
            },
            audit_path,
        )

        result = seo_audit_harness.resolve_google_visible_audit(
            brand_dir,
            "run",
            audit_path,
        )
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(result["resolved_rows"], 2)
        self.assertEqual(audit["rows"][0]["status"], "fail")
        self.assertEqual(audit["rows"][0]["evidence_source"], "playwright")
        self.assertEqual(audit["rows"][1]["status"], "not_applicable")
        self.assertEqual(audit["rows"][1]["evidence_source"], "playwright")

    def test_google_visible_resolver_refreshes_site_check_rows(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        run_dir = brand_dir / "references" / "evidence" / "run"
        run_dir.mkdir(parents=True)
        site_checks_path = run_dir / "site-checks.json"
        seo_audit_harness.write_json(
            {
                "checks": [
                    {
                        "check_id": "body_text_line_length",
                        "url": "https://example.com",
                        "severity": "medium",
                        "status": "pass",
                        "source": "playwright",
                        "artifact_ref": "playwright.json",
                        "result": "Line length is readable.",
                        "next_action": "",
                    }
                ]
            },
            site_checks_path,
        )
        audit_path = brand_dir / "audit.json"
        seo_audit_harness.write_json(
            {
                "metadata": {"scope": "site", "audit_type": "partial"},
                "rows": [
                    {
                        "checklist_id": "sample",
                        "section_id": "sample",
                        "item_id": "line-length",
                        "item_text": "Body text line length is checked for readability.",
                        "status": "fail",
                        "evidence_source": "playwright",
                        "artifact_ref": str(site_checks_path),
                        "result": "Old failure.",
                        "blocker": "",
                        "next_action": "Old action.",
                        "candidate_sources": ["playwright"],
                        "required_sources": ["playwright"],
                    }
                ],
            },
            audit_path,
        )

        seo_audit_harness.resolve_google_visible_audit(brand_dir, "run", audit_path)
        audit = seo_audit_harness.read_json(audit_path)

        self.assertEqual(audit["rows"][0]["status"], "pass")
        self.assertEqual(audit["rows"][0]["next_action"], "")

    def test_google_visible_site_check_ids_include_playwright_assertions(self):
        cases = {
            "JavaScript does not break URL fragments, deep links, or direct access.": "fragment_deep_links",
            "Text is readable without zooming.": "mobile_text_readability",
            "Tap targets are large enough and not crowded.": "tap_targets",
            "The page avoids horizontal scrolling.": "horizontal_scroll",
            "Popups and interstitials do not block the main content.": "blocking_popups_interstitials",
            "Single-page apps return meaningful status handling for missing, private, and moved routes.": "route_status_handling",
            "Client-side route changes update metadata correctly.": "client_route_metadata",
            "Lazy loading does not hide in-viewport content.": "lazy_loading_in_viewport",
            "Forms have labels, error messages, and accessible instructions.": "form_accessibility",
            "Color contrast supports readability.": "color_contrast",
            "The page can be navigated by keyboard.": "keyboard_navigation",
            "The main content is not trapped behind inaccessible controls.": "inaccessible_controls",
            "Tables are used for tabular data, not layout.": "table_semantics",
            "Content is readable at common zoom levels.": "zoom_readability",
            "Text spacing supports readability.": "text_spacing",
            "Body text line length is checked for readability.": "body_text_line_length",
            "Forms are short enough for intent and work on mobile.": "mobile_form_usability",
        }

        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertIn(expected, seo_audit_harness.google_visible_site_check_ids(text))

    def test_record_source_evidence_updates_manifest(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        manifest_dir = brand_dir / "references" / "evidence" / "run"
        manifest_dir.mkdir(parents=True)
        seo_audit_harness.write_json(
            {"run_id": "run", "sources": {"posthog": {"status": "blocked"}}},
            manifest_dir / "manifest.json",
        )
        input_path = brand_dir / "posthog-input.json"
        seo_audit_harness.write_json({"funnels": []}, input_path)

        result = seo_audit_harness.record_source_evidence(
            brand_dir,
            "run",
            "posthog",
            input_path,
            "PostHog MCP output recorded.",
        )

        manifest = seo_audit_harness.read_json(result["manifest_path"])
        artifact = seo_audit_harness.read_json(result["artifact"])
        self.assertEqual(manifest["sources"]["posthog"]["status"], "recorded")
        self.assertEqual(artifact["status"], "recorded")

    def test_record_source_evidence_accepts_ga4(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        input_path = brand_dir / "ga4-input.json"
        seo_audit_harness.write_json({"sessions": []}, input_path)

        result = seo_audit_harness.record_source_evidence(
            brand_dir,
            "run",
            "ga4",
            input_path,
            "GA4 connector output recorded.",
        )

        self.assertEqual(result["source"], "ga4")
        self.assertEqual(
            seo_audit_harness.read_json(result["manifest_path"])["sources"]["ga4"]["status"],
            "recorded",
        )

    def test_site_scope_strict_verification_requires_site_artifacts(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        compiled = self.compiled_fixture()
        audit = seo_audit_harness.init_audit(
            compiled,
            "https://www.example.com",
            "full",
            scope="site",
            evidence_run_id_value="run",
            brand_dir=brand_dir,
        )
        artifact = brand_dir / "evidence.json"
        artifact.write_text("{}", encoding="utf-8")
        for row in audit["rows"]:
            row.update(
                {
                    "status": "pass",
                    "evidence_source": "manual",
                    "artifact_ref": str(artifact),
                    "result": "Verified.",
                    "blocker": "",
                    "next_action": "",
                }
            )

        errors = seo_audit_harness.validate_audit(compiled, audit, strict_evidence=True)
        self.assertTrue(any("url_inventory_path" in error for error in errors))

        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.url_inventory_path(brand_dir),
            seo_audit_harness.URL_INVENTORY_FIELDS,
            [],
        )
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.site_checks_path(brand_dir),
            seo_audit_harness.SITE_CHECK_FIELDS,
            [],
        )
        seo_audit_harness.write_json(
            {"run_id": "run"},
            brand_dir / "references" / "evidence" / "run" / "manifest.json",
        )

        self.assertEqual(
            seo_audit_harness.validate_audit(compiled, audit, strict_evidence=True),
            [],
        )

    def test_authenticity_fails_without_sources(self):
        log = seo_audit_harness.init_authenticity("draft.md")
        errors = seo_audit_harness.validate_authenticity(log)
        self.assertIn("no concrete source found for publish-ready content", errors)

    def test_init_authenticity_records_required_content_skill(self):
        log = seo_audit_harness.init_authenticity("draft.md")

        self.assertEqual(
            log["metadata"]["required_skill"],
            seo_audit_harness.CONTENT_AUTHENTICITY_SKILL,
        )
        self.assertEqual(
            log["metadata"]["required_skill_ref"],
            seo_audit_harness.CONTENT_AUTHENTICITY_SKILL_REF,
        )
        self.assertEqual(
            log["metadata"]["required_ai_text_risk_skill"],
            seo_audit_harness.AI_TEXT_RISK_SKILL,
        )

    def test_authenticity_fails_unsupported_best_top_claim(self):
        log = {
            "metadata": {"target": "draft.md"},
            "sources": [
                {
                    "source_id": "p1",
                    "source_type": "product_page",
                    "source_ref": "https://example.com/product",
                    "extracted_facts": "Leather upper.",
                }
            ],
            "claims": [],
        }
        errors = seo_audit_harness.validate_authenticity(log, "The best sandal.")
        self.assertTrue(any("best/top" in error for error in errors))

    def test_authenticity_passes_with_supported_best_top_claim(self):
        log = {
            "metadata": {"target": "draft.md"},
            "sources": [
                {
                    "source_id": "p1",
                    "source_type": "product_page",
                    "source_ref": "https://example.com/product",
                    "extracted_facts": "Leather upper.",
                }
            ],
            "claims": [
                {
                    "claim": "Best for leather sandal shoppers.",
                    "claim_type": "best_top",
                    "source_ids": ["p1"],
                }
            ],
        }
        self.assertEqual(
            seo_audit_harness.validate_authenticity(log, "The best sandal."), []
        )

    def authenticity_log_with_source(self):
        return {
            "metadata": {"target": "draft.md"},
            "sources": [
                {
                    "source_id": "b1",
                    "source_type": "brand_dna",
                    "source_ref": "brands/strique/brand-dna.md",
                    "extracted_facts": "Strique is an AI marketing platform.",
                }
            ],
            "claims": [],
            "detector_notes": [],
        }

    def test_authenticity_passes_detector_note_below_threshold(self):
        log = self.authenticity_log_with_source()
        log["detector_notes"].append(
            {"tool": "ZeroGPT", "score": "19%", "note": "Weak editorial signal."}
        )

        self.assertEqual(seo_audit_harness.validate_authenticity(log), [])

    def test_authenticity_fails_detector_note_at_threshold(self):
        log = self.authenticity_log_with_source()
        log["detector_notes"].append(
            {"tool": "GPTZero", "score": "20%", "note": "AI detector estimate."}
        )

        errors = seo_audit_harness.validate_authenticity(log)
        self.assertTrue(any("max AI detector score" in error for error in errors))

    def test_authenticity_fails_unknown_detector_note_with_score_at_threshold(self):
        log = self.authenticity_log_with_source()
        log["detector_notes"].append(
            {"tool": "DetectorX", "score": "20%", "note": "Recorded score."}
        )

        errors = seo_audit_harness.validate_authenticity(log)
        self.assertTrue(any("DetectorX" in error for error in errors))

    def test_authenticity_treats_fraction_detector_score_as_percent_scale(self):
        log = self.authenticity_log_with_source()
        log["detector_notes"].append(
            {"tool": "ZeroGPT", "score": "0.20", "note": "Ratio-form score."}
        )

        errors = seo_audit_harness.validate_authenticity(log)
        self.assertTrue(any("20.0" in error for error in errors))

    def test_authenticity_fails_local_ai_text_risk_at_threshold(self):
        log = self.authenticity_log_with_source()
        draft = (
            "In today's digital landscape, brands need a comprehensive guide to "
            "unlock your potential and streamline every workflow. Furthermore, "
            "this robust solution helps teams optimize outcomes. Furthermore, "
            "this innovative solution helps teams optimize outcomes. Furthermore, "
            "this dynamic solution helps teams optimize outcomes. Furthermore, "
            "this seamless solution helps teams optimize outcomes. Furthermore, "
            "this strategic solution helps teams optimize outcomes. In conclusion, "
            "this game changer empowers every business to leverage effective growth."
        )

        errors = seo_audit_harness.validate_authenticity(log, draft)

        self.assertTrue(any("local AI text risk score" in error for error in errors))

    def test_authenticity_passes_specific_local_ai_text_risk(self):
        log = self.authenticity_log_with_source()
        draft = (
            "Strique uses brand DNA, keyword evidence, crawl data, Search Console, "
            "and PostHog context to decide what a blog should do. The draft names "
            "the reader, shows the audit evidence, and keeps claims tied to the "
            "source log. A reviewer can see which facts came from the crawl, which "
            "keywords came from the planner file, and which conversion assumptions "
            "still need PostHog evidence. That makes the article easier to check "
            "before publishing. It also keeps the writer from adding broad claims "
            "that sound polished but do not help a growth team make the next call."
        )

        report = seo_audit_harness.ai_text_risk_report(draft)

        self.assertLess(report["score"], 20)
        self.assertEqual(seo_audit_harness.validate_authenticity(log, draft), [])

    def test_ai_text_risk_flags_repeated_contrastive_reframes(self):
        plain = "SEO automation is not a button that writes 50 articles and hopes Google sorts it out."
        patterned = (
            "It is not just a dashboard, it is a decision layer for the marketing team. "
            "Strique still needs crawl evidence, Search Console queries, and PostHog behavior before it recommends the next page. "
            "It is not about publishing more, it is about choosing the work that removes a real search bottleneck. "
            "The editor can see the source log, the keyword cluster, and the owner for each fix before the draft moves forward."
        )

        plain_names = {feature["name"] for feature in seo_audit_harness.ai_text_risk_report(plain)["features"]}
        patterned_names = {feature["name"] for feature in seo_audit_harness.ai_text_risk_report(patterned)["features"]}

        self.assertNotIn("contrastive_reframe", plain_names)
        self.assertIn("contrastive_reframe", patterned_names)

    def test_write_content_requires_content_authenticity_skill(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        base = Path(tmpdir.name)
        draft = base / "draft.md"
        output = base / "published.md"
        authenticity = base / "auth.json"
        draft.write_text("Specific Strique content.", encoding="utf-8")
        log = self.authenticity_log_with_source()
        seo_audit_harness.write_json(log, authenticity)

        result = seo_audit_harness.write_content_with_authenticity(
            draft,
            output,
            authenticity,
        )

        self.assertFalse(result["ok"])
        self.assertFalse(output.exists())
        self.assertTrue(any("required_skill" in error for error in result["errors"]))

    def test_write_content_saves_only_after_authenticity_passes(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        base = Path(tmpdir.name)
        draft = base / "draft.md"
        output = base / "published.md"
        authenticity = base / "auth.json"
        draft.write_text("Specific Strique content.", encoding="utf-8")
        log = self.authenticity_log_with_source()
        log["metadata"].update(
            {
                "required_skill": seo_audit_harness.CONTENT_AUTHENTICITY_SKILL,
                "required_skill_ref": seo_audit_harness.CONTENT_AUTHENTICITY_SKILL_REF,
            }
        )
        seo_audit_harness.write_json(log, authenticity)

        result = seo_audit_harness.write_content_with_authenticity(
            draft,
            output,
            authenticity,
        )

        self.assertTrue(result["ok"])
        self.assertEqual(output.read_text(encoding="utf-8"), "Specific Strique content.")

    def test_content_seo_authenticity_skill_is_repo_local_fork(self):
        skill_path = (
            ROOT / ".agents" / "skills" / "content-seo-authenticity" / "SKILL.md"
        )
        text = skill_path.read_text(encoding="utf-8")

        self.assertIn("name: content-seo-authenticity", text)
        self.assertIn("AI detector scores are weak editorial signals", text)
        self.assertIn("verify-authenticity", text)
        self.assertIn("write-content", text)

    def test_ai_text_risk_gate_skill_exists(self):
        skill_path = ROOT / ".agents" / "skills" / "ai-text-risk-gate" / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")

        self.assertIn("name: ai-text-risk-gate", text)
        self.assertIn("AI-pattern risk", text)
        self.assertIn("not proof of authorship", text)
        self.assertIn("write-content", text)
        self.assertIn("Brand DNA", text)
        self.assertIn("GSC queries", text)
        self.assertIn("PostHog behavior evidence", text)
        self.assertNotIn("guarantee a zerogpt result", text.lower())
        self.assertNotIn("how to bypass", text.lower())

    def test_firecrawl_scrape_posts_request_and_normalizes_response(self):
        captured = {}

        def fake_open(scrape_request, timeout):
            captured["url"] = scrape_request.full_url
            captured["headers"] = dict(scrape_request.header_items())
            captured["payload"] = seo_audit_harness.json.loads(
                scrape_request.data.decode("utf-8")
            )
            captured["timeout"] = timeout
            return FakeResponse(
                """{
                    "success": true,
                    "data": {
                        "markdown": "Rendered text",
                        "html": "<main>Rendered</main>",
                        "rawHtml": "<html></html>",
                        "links": ["https://example.com/a"],
                        "images": ["https://example.com/a.jpg"],
                        "metadata": {"statusCode": 200}
                    }
                }"""
            )

        with mock.patch.dict(
            seo_audit_harness.os.environ, {"FIRECRAWL_API_KEY": "test-key"}, clear=True
        ):
            result = seo_audit_harness.firecrawl_scrape(
                "https://example.com", open_url=fake_open
            )

        self.assertEqual(captured["url"], seo_audit_harness.FIRECRAWL_SCRAPE_URL)
        self.assertEqual(captured["payload"]["url"], "https://example.com")
        self.assertEqual(captured["payload"]["formats"], ["markdown", "html", "rawHtml", "links", "images"])
        self.assertEqual(captured["headers"]["Authorization"], "Bearer test-key")
        self.assertEqual(captured["timeout"], 65)
        self.assertEqual(result["status"], 200)
        self.assertEqual(result["rendered_text"], "Rendered text")
        self.assertEqual(result["raw_html"], "<html></html>")

    def test_firecrawl_key_is_required(self):
        with mock.patch.object(seo_audit_harness, "load_local_env"):
            with mock.patch.dict(seo_audit_harness.os.environ, {}, clear=True):
                with self.assertRaisesRegex(RuntimeError, "FIRECRAWL_API_KEY"):
                    seo_audit_harness.get_firecrawl_api_key()

    def test_keyword_planner_parser_handles_metrics_and_missing_metrics(self):
        payload = {
            "results": [
                {
                    "text": "AI Marketing Agent",
                    "keywordIdeaMetrics": {
                        "avgMonthlySearches": "1600",
                        "competition": "LOW",
                        "competitionIndex": "29",
                    },
                },
                {"text": "AI SEO Automation"},
            ]
        }

        ideas = seo_audit_harness.parse_keyword_planner_response(payload)

        self.assertEqual(ideas[0]["keyword"], "AI Marketing Agent")
        self.assertEqual(ideas[0]["volume"], "1600")
        self.assertEqual(ideas[0]["competition"], "LOW")
        self.assertEqual(ideas[0]["competition_index"], "29")
        self.assertEqual(ideas[1]["volume"], "")
        self.assertEqual(ideas[1]["competition"], "")

    def test_gsc_parser_reads_query_page_country_dimensions(self):
        payload = {
            "data": {
                "rows": [
                    {
                        "keys": [
                            "ai marketing agent",
                            "https://www.example.com/product",
                            "usa",
                        ],
                        "clicks": 2,
                        "impressions": 50,
                        "ctr": 0.04,
                        "position": 3.2,
                    }
                ]
            }
        }

        rows = seo_audit_harness.parse_gsc_rows(payload)

        self.assertEqual(rows[0]["keyword"], "ai marketing agent")
        self.assertEqual(rows[0]["page"], "https://www.example.com/product")
        self.assertEqual(rows[0]["country"], "usa")
        self.assertEqual(rows[0]["clicks"], 2)

    def test_composio_execute_hydrates_stored_output_file(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        output_path = Path(tmpdir.name) / "gsc-output.json"
        output_path.write_text(
            """{
  "successful": true,
  "data": {
    "rows": [
      {
        "keys": ["strique", "https://www.strique.io/", "ind"],
        "clicks": 7,
        "impressions": 11
      }
    ]
  },
  "error": null
}
""",
            encoding="utf-8",
        )

        def fake_runner(command, capture_output, text, check):
            return subprocess.CompletedProcess(
                command,
                0,
                stdout='{"successful": true, "storedInFile": true, "outputFilePath": "%s"}'
                % output_path,
                stderr="",
            )

        payload = seo_audit_harness.composio_execute(
            seo_audit_harness.GSC_SEARCH_ANALYTICS_TOOL,
            {"site_url": "sc-domain:strique.io"},
            runner=fake_runner,
        )

        rows = seo_audit_harness.parse_gsc_rows(payload)

        self.assertEqual(rows[0]["keyword"], "strique")
        self.assertEqual(rows[0]["clicks"], 7)

    def test_country_inference_prefers_gsc_before_brand_dna(self):
        rows = [
            {"country": "ind", "clicks": 3, "impressions": 20},
            {"country": "usa", "clicks": 1, "impressions": 100},
        ]

        country, source = seo_audit_harness.infer_target_country(
            rows,
            "Primary market: United States.",
        )

        self.assertEqual(country, "India")
        self.assertEqual(source, "gsc")

    def test_country_inference_fails_without_evidence(self):
        country, source = seo_audit_harness.infer_target_country(
            [],
            "We are building a product. No market here.",
        )

        self.assertEqual(country, "")
        self.assertEqual(source, "")

    def test_deduplicates_keyword_ideas_case_insensitively(self):
        candidates = [
            {"keyword": "AI Marketing Agent", "volume": "100", "source": "keyword_planner"},
            {"keyword": "ai marketing agent", "clicks": 1, "source": "gsc"},
        ]

        deduped = seo_audit_harness.deduplicate_keyword_candidates(candidates)

        self.assertEqual(len(deduped), 1)
        self.assertEqual(deduped[0]["keyword"], "ai marketing agent")
        self.assertEqual(deduped[0]["volume"], "100")
        self.assertEqual(deduped[0]["sources"], ["gsc", "keyword_planner"])

    def test_writes_valid_prioritized_keyword_csv_with_existing_header(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        path = Path(tmpdir.name) / "keywords.csv"

        seo_audit_harness.write_csv_dict_rows(
            path,
            seo_audit_harness.KEYWORD_ROW_FIELDS,
            [self.keyword_row("ai marketing agent", priority="high")],
        )
        fields, rows = seo_audit_harness.read_csv_dict_rows(path)

        self.assertEqual(fields, seo_audit_harness.KEYWORD_ROW_FIELDS)
        self.assertEqual(rows[0]["keyword"], "ai marketing agent")

    def test_verify_keywords_passes_valid_output(self):
        brand_dir = self.make_keyword_brand_dir()

        result = seo_audit_harness.validate_keyword_outputs(brand_dir)

        self.assertEqual(result["errors"], [])
        self.assertEqual(result["counts"]["prioritized_rows"], 60)
        self.assertEqual(result["counts"]["universe_rows"], 200)

    def test_verify_keywords_fails_duplicate_keywords(self):
        rows = [self.keyword_row("keyword {}".format(index)) for index in range(60)]
        rows[1]["keyword"] = rows[0]["keyword"].upper()
        brand_dir = self.make_keyword_brand_dir(rows=rows)

        result = seo_audit_harness.validate_keyword_outputs(brand_dir)

        self.assertTrue(any("duplicate keyword" in error for error in result["errors"]))

    def test_verify_keywords_fails_missing_source_on_high_priority_row(self):
        rows = [
            self.keyword_row(
                "keyword {}".format(index),
                priority="high" if index < 10 else "medium",
            )
            for index in range(60)
        ]
        rows[0]["source"] = ""
        brand_dir = self.make_keyword_brand_dir(rows=rows)

        result = seo_audit_harness.validate_keyword_outputs(brand_dir)

        self.assertTrue(any("missing source" in error for error in result["errors"]))

    def test_verify_keywords_fails_missing_target_url_on_high_priority_row(self):
        rows = [
            self.keyword_row(
                "keyword {}".format(index),
                priority="high" if index < 10 else "medium",
            )
            for index in range(60)
        ]
        rows[0]["target_url"] = ""
        brand_dir = self.make_keyword_brand_dir(rows=rows)

        result = seo_audit_harness.validate_keyword_outputs(brand_dir)

        self.assertTrue(any("missing target_url" in error for error in result["errors"]))

    def test_verify_keywords_fails_too_few_prioritized_rows(self):
        rows = [self.keyword_row("keyword {}".format(index)) for index in range(49)]
        brand_dir = self.make_keyword_brand_dir(rows=rows)

        result = seo_audit_harness.validate_keyword_outputs(brand_dir)

        self.assertTrue(any("expected at least 50" in error for error in result["errors"]))

    def test_generate_keywords_uses_fake_subprocess_runner(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "keywords").mkdir(parents=True)
        (brand_dir / "brand-dna.md").write_text(
            """# Brand DNA

### Name

Example

### Website URL

https://www.example.com

### Business Description

Example is an AI marketing agent for ecommerce marketing automation.
""",
            encoding="utf-8",
        )
        seo_audit_harness.write_csv_dict_rows(
            seo_audit_harness.keyword_csv_path(brand_dir),
            seo_audit_harness.KEYWORD_ROW_FIELDS,
            [self.keyword_row("ai marketing agent", priority="high")],
        )
        calls = []

        def fake_runner(command, capture_output, text, check):
            calls.append(command)
            if command[1:3] == ["execute", seo_audit_harness.GSC_LIST_SITES_TOOL]:
                stdout = seo_audit_harness.json.dumps(
                    {
                        "successful": True,
                        "data": {
                            "siteEntry": [
                                {"siteUrl": "https://www.example.com/"}
                            ]
                        },
                    }
                )
            elif command[1:3] == [
                "execute",
                seo_audit_harness.GSC_SEARCH_ANALYTICS_TOOL,
            ]:
                stdout = seo_audit_harness.json.dumps(
                    {
                        "successful": True,
                        "data": {
                            "rows": [
                                {
                                    "keys": [
                                        "ai marketing agent",
                                        "https://www.example.com/product",
                                        "usa",
                                    ],
                                    "clicks": 1,
                                    "impressions": 200,
                                }
                            ]
                        },
                    }
                )
            elif command[1] == "proxy":
                stdout = seo_audit_harness.json.dumps(
                    {
                        "results": [
                            {
                                "text": "ai ad generator",
                                "keywordIdeaMetrics": {
                                    "avgMonthlySearches": "2400",
                                    "competition": "MEDIUM",
                                    "competitionIndex": "63",
                                },
                            }
                        ]
                    }
                )
            else:
                stdout = "{}"
            return subprocess.CompletedProcess(command, 0, stdout, "")

        result = seo_audit_harness.generate_keyword_research(
            brand_dir,
            "1234567890",
            max_prioritized=10,
            raw_limit=10,
            runner=fake_runner,
        )

        self.assertTrue(result["ok"])
        self.assertTrue(seo_audit_harness.keyword_csv_path(brand_dir).exists())
        self.assertTrue(seo_audit_harness.keyword_universe_path(brand_dir).exists())
        self.assertTrue(any(call[1] == "proxy" for call in calls))

    def test_context_system_registry_validates(self):
        result = seo_audit_harness.validate_context_system(
            checklist_paths=seo_audit_harness.default_checklist_paths()
        )

        self.assertTrue(result["ok"], result["errors"])

    def test_context_map_generation_covers_checklist_items(self):
        sample = self.make_checklist(
            """# Content SEO Checklist

## 1. Page Purpose And Audience

Evidence sources: `Human/context`, `GSC`.

- [ ] The page has one primary purpose.
- [ ] The audience is explicit enough to shape copy.
"""
        )

        result = seo_audit_harness.build_checklist_context_map(
            checklist_paths=[str(sample)]
        )

        self.assertEqual(result["item_count"], 2)
        self.assertEqual(len(result["entries"]), 2)
        self.assertIn("target_audience", result["entries"][1]["requires"])

    def test_resolve_context_uses_brand_dna_and_questions_for_missing_fields(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "brand-dna.md").write_text(
            """# Brand DNA

### Name

Example

### Website URL

https://www.example.com

### Business Description

Example is a SaaS platform for ecommerce marketing teams.
""",
            encoding="utf-8",
        )

        result = seo_audit_harness.resolve_context_fields(
            brand_dir,
            {"business_model", "primary_business_goal"},
        )

        self.assertIn("business_model", result["resolved"])
        self.assertEqual(
            result["resolved"]["business_model"]["source_type"],
            "system_inferred",
        )
        self.assertEqual(
            [question["question_id"] for question in result["questions"]],
            ["primary_business_goal"],
        )

    def test_record_context_answer_writes_brand_context(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "brand-dna.md").write_text("# Brand DNA\n", encoding="utf-8")

        result = seo_audit_harness.record_context_answer(
            brand_dir,
            "primary_business_goal",
            "Increase qualified leads",
            question_id="primary_business_goal",
        )

        self.assertTrue(result["ok"])
        stored = seo_audit_harness.read_json(
            seo_audit_harness.brand_context_path(brand_dir)
        )
        self.assertEqual(
            stored["fields"]["primary_business_goal"]["value"],
            "Increase qualified leads",
        )

    def test_resolve_context_skips_irrelevant_vertical_questions(self):
        tmpdir = tempfile.TemporaryDirectory()
        self.addCleanup(tmpdir.cleanup)
        brand_dir = Path(tmpdir.name)
        (brand_dir / "context").mkdir(parents=True)
        seo_audit_harness.write_json(
            {
                "brand_id": "example",
                "fields": {
                    "business_model": seo_audit_harness.context_answer(
                        "business_model",
                        ["saas"],
                        "client_confirmed",
                        "test",
                        "high",
                    ),
                    "site_type": seo_audit_harness.context_answer(
                        "site_type",
                        ["saas marketing site"],
                        "client_confirmed",
                        "test",
                        "high",
                    ),
                },
            },
            seo_audit_harness.brand_context_path(brand_dir),
        )

        result = seo_audit_harness.resolve_context_for_work(
            brand_dir,
            checklist_ids=["ai-seo-aeo-geo"],
        )
        question_ids = {question["question_id"] for question in result["questions"]}

        self.assertNotIn("local_context", question_ids)
        self.assertNotIn("ecommerce_context", question_ids)
        self.assertNotIn("off_page_scope", question_ids)


if __name__ == "__main__":
    unittest.main()
