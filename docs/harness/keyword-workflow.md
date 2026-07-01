---
title: Keyword Workflow
sidebar_position: 6
---

# Keyword Workflow

The harness tracks keyword evidence in brand workspaces.

## Files

- `keywords/keywords.csv`: prioritized working keyword list.
- `exports/keyword-universe.csv`: larger deduped keyword universe.
- `references/keyword-research-summary.json`: summary counts, blockers, and source notes.

## Fields

The tracker captures keyword, intent, page type, target URL, volume, difficulty, priority, source, status, and notes.

## Commands

Use `generate-keywords` to create or update keyword rows from available demand inputs. Use `verify-keywords` to check quality, coverage, and blockers.

Do not invent demand. If Keyword Planner, GSC, or other demand evidence is missing, record the blocker.
