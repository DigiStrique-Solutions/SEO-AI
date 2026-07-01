---
title: Release Checklist
sidebar_position: 7
---

# Release Checklist

## Required Checks

```bash
test -f AGENTS.md
sed -n '1,220p' AGENTS.md
python3 -m unittest tests/test_seo_audit_harness.py
npm run docs:build
```

## Privacy Checks

```bash
rg -i "api[_-]?key|secret|token|password|credential" docs .agents
rg -i "raw connector|customer data|private payload" docs
```

## Local URL Check

Before reporting a preview URL:

```bash
lsof -nP -iTCP:<port> -sTCP:LISTEN
curl -I http://localhost:<port>/
```

## Release Notes Template

- What changed.
- Verification commands and results.
- Known gaps.
- Restricted artifacts excluded.
- Deployment target.
