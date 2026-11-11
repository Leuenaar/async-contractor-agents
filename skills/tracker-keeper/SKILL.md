---
name: tracker-keeper
description: Keeps the job and client application tracker complete by reading Gmail and session history, adding one row per application with date, role, platform, status and source, and updating statuses when replies arrive. Use when the owner asks what was applied to, when an old application replies, or before screening new listings.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,human-gate"
---

# Tracker keeper

**Core rule:** the owner should never have to remember an application. The tracker remembers, from sources, not from guesses.

## Input

- Gmail access (read).
- The current tracker (sheet, CSV or doc).
- Session history or notes that mention applications.

## Steps

1. Search Gmail for application confirmations, platform notifications and replies since the last update. Useful queries: "application received", "thank you for applying", "applied", platform sender domains.
2. For each one, match it to an existing row by company plus role. Update the status if it changed.
3. Add missing applications as new rows. Every row cites its source: the email subject and date, or the session date.
4. Mark stale rows: no reply after 30 days becomes "no response", not "rejected".
5. Show the owner the diff: rows added, statuses changed. Nothing is written to a shared tracker until the owner confirms.

## Columns

| Applied | Company | Role | Platform | Process | Status | Last update | Source | Link |

Status values: applied, assessment pending, interview pending, declined, no response, offer, withdrawn.

## Rules

- No row without a source ([evidence-rule](references/evidence-rule.md)).
- Do not schedule follow-ups. Record status only.
- Changes to the tracker wait for confirmation ([human-gate](references/human-gate.md), tier 1 for local files, tier 2 for shared sheets).

## Done when

- [ ] Every new or changed row cites an email or session date.
- [ ] Duplicate rows merged.
- [ ] Diff shown to the owner before writing.

## Not this skill's job

Deciding what to apply to (`job-screener`).

Research behind this skill: [references/research.md](references/research.md).
