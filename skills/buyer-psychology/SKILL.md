---
name: buyer-psychology
description: Researches why a buyer would pick a freelancer with no reviews and what they fear about the service (for AI work, such as wrong answers, invented prices, no human handoff and silent failure), then maps each fear and decision driver to the owner's existing proof or marks it as a gap. Use when writing a profile, a proposal opening, a landing page or an offer.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Buyer psychology

**Core rule:** a fear with no proof against it is a gap to close, not a line to write around.

## Input

- The buyer type (agency owner, trade business owner, startup founder).
- The service being offered.
- The owner's proof list.

## Steps

1. Find the buyer's decision drivers from client-side sources: hiring guides, buyer surveys, client threads.
2. Find their specific fears about this service: incidents, surveys, complaints.
3. Rank both lists by evidence strength.
4. Map each driver and fear to an owner asset (a demo, a test, a report) with a link. No asset means "gap".
5. For each gap, name the smallest piece of proof that would close it (one test, one recorded walkthrough).

## Rules

- Sources opened in the session ([evidence-rule](references/evidence-rule.md)).
- No manipulation tactics (fake urgency, fake scarcity). The goal is to remove real doubt with real proof.
- Plain output ([anti-slop](references/anti-slop.md)).

## Done when

- [ ] Top 5 drivers and top 5 fears, each sourced.
- [ ] Every item mapped to an asset or marked gap.
- [ ] Every gap has the smallest proof that would close it.

## Output

```
| Fear or driver | Evidence | Owner asset | Gap? | Smallest proof to close |
```

## Not this skill's job

Writing the proposal itself (`upwork-proposal`).

Research behind this skill: [references/research.md](references/research.md).
