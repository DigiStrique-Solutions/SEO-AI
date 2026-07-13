#!/usr/bin/env python3
"""Require evaluation coverage when SEO writing instructions or skills change."""

import argparse
import subprocess

WATCHED_PREFIXES = (".agents/skills/", "prompts/seo-content", "tools/seo_content_pipeline_v2.py")
EVAL_PREFIXES = ("evals/seo-content-v2/", "tests/test_seo_content_pipeline_v2.py")


def validate(paths):
    """Return a CI error when writing behavior changes without evaluation changes."""
    watched = any(path.startswith(WATCHED_PREFIXES) for path in paths)
    evaluated = any(path.startswith(EVAL_PREFIXES) for path in paths)
    return ["SEO writing behavior changed without an evaluation-suite update."] if watched and not evaluated else []


def main():
    """Compare the current branch with its pull-request base."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument("--changed-file", action="append", default=[])
    args = parser.parse_args()
    paths = args.changed_file
    if not paths:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", f"{args.base}...HEAD"], text=True
        )
        paths = output.splitlines()
    errors = validate(paths)
    for error in errors:
        print(error)
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
