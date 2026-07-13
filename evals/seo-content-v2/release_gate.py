#!/usr/bin/env python3
"""Fail closed until all manual and deterministic SEO content gates are complete."""

import importlib.util
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MODULE = ROOT / "tools" / "seo_content_pipeline_v2.py"
SPEC = importlib.util.spec_from_file_location("seo_content_pipeline_v2_eval", MODULE)
pipeline = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = pipeline
SPEC.loader.exec_module(pipeline)

cases = json.loads((Path(__file__).parent / "cases.json").read_text(encoding="utf-8"))
report = pipeline.evaluate_corpus(cases)
print(json.dumps(report, indent=2))
raise SystemExit(0 if report["release_ready"] else 1)
