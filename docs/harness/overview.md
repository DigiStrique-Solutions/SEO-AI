---
title: Harness Overview
sidebar_position: 1
---

# Harness Overview

`tools/seo_audit_harness.py` is the local CLI for Strique SEO audit work. It turns Markdown checklists into stable audit rows, collects evidence, verifies audit coverage, records source-backed content authenticity, and keeps brand workspace outputs in predictable files.

## Core Flows

1. Compile Markdown checklists.
2. Initialize an audit matrix.
3. Collect or attach evidence.
4. Record `pass`, `fail`, `not_applicable`, or `not_checked_blocked`.
5. Verify before summarizing.
6. Generate tasks or content only after the relevant gate passes.

## Full Audit Rule

A full audit is only complete when every relevant row is `pass`, `fail`, or `not_applicable`. If any row is `not_checked_blocked`, call it a partial audit and name the missing access, data, or tool.

## Content Authenticity Rule

Publish-ready content needs concrete source evidence. AI detector scores are weak editorial signals and never replace source-backed claims.
