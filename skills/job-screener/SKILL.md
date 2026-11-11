---
name: job-screener
description: Screens job and gig listings against an async-only selection filter, coding requirements, experience gaps, client risk signals and past applications, and returns a short pass list with a reason for every reject. Use when the owner shares listings, asks to search job boards, or wants a shortlist of roles to apply for.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "strict-selection,evidence-rule,human-gate"
---

# Job screener

**Core rule:** a listing that fails one hard rule is a reject, however good the pay. Say which rule.

## Input

- Listings: pasted text, links, or a board and a search term.
- The application tracker or Gmail history, to catch duplicates.
- The owner's real experience and dates (self-directed since April 2026).

## Steps

1. Read each listing in full once. Read at most 20 listings per session on any single platform; accounts get rate-limited.
2. Check the hard rules in [strict-selection](references/strict-selection.md) first. Reject on the first failure and record it.
3. For survivors, check client risk signals (table below).
4. Check the tracker and Gmail for a past application to the same company or posting. A past application is a reject unless the owner asks to reapply.
5. Rank survivors by fit to existing proof, then by pay, then by freshness.
6. Return 3 to 5 at most. If none pass, say so and say which rule killed most of them; that tells the owner where the market and the profile disagree.

## Client risk signals (Upwork and similar)

| Signal | Treat as |
| --- | --- |
| Payment method not verified, 0 hires, account under 30 days old | Soft flag; allowed for small fixed-price jobs only |
| Asks for unpaid test work or free samples | Reject |
| Pushes to talk or pay outside the platform | Reject |
| Budget far below market for the stated scope | Soft flag; name the gap |
| 50+ proposals and 0 interviews after 2 days | Soft flag; low odds |
| Many hires with poor feedback left to freelancers | Soft flag |

## Rules

- Never apply, submit or message. Shortlist only ([human-gate](references/human-gate.md), tier 2).
- Every reason quotes the listing line that triggered it ([evidence-rule](references/evidence-rule.md)).
- "Selection process unknown" is a soft flag, never a pass.

## Done when

- [ ] Each listing has pass, soft flag or reject, with the quoted reason.
- [ ] No passed listing was already applied to.
- [ ] Session listing count is 20 or fewer per platform.
- [ ] Results saved to a CSV in the workspace.

## Output

```
| Listing | Client | Posted | Budget | Process | Verdict | Reason (quoted) | Link |
```

Then one line: the most common reject reason and what it implies.

## Not this skill's job

Writing the proposal (`upwork-proposal`). Filling the form (`form-filler`).

Research behind this skill: [references/research.md](references/research.md).
