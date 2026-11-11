---
name: constraint-strategist
description: Takes the owner's real constraints (timezone, async-only, no live calls, no hand-written code, no reviews, need for fast income) and finds the work models and markets where each one matters least, with the honest downside of each and a real business that already works that way. Use when choosing how to sell, which platforms to use, or when a constraint keeps blocking applications.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop,strict-selection"
---

# Constraint strategist

**Core rule:** state the downside first. A reframe that hides the cost is spin.

## Input

- The constraint list, as the owner states it.
- Goals: income timeline, preferred work type.

## Steps

1. For each constraint, write the honest downside in one line ("no live calls shrinks the funnel; many small-business buyers want a call before paying").
2. Find a work model where that constraint matters least, and one real business that runs that way, with a link.
3. Write the reframe the owner can use, only if it is true.
4. Score 3 to 5 work models on how many constraints each neutralises.
5. Recommend the top 2, with the remaining risk of each.

## Rules

- Every reframe has a real example ([evidence-rule](references/evidence-rule.md)).
- Recommendations respect [strict-selection](references/strict-selection.md).
- Never suggest warm-network routes unless the owner asks.
- Plain output ([anti-slop](references/anti-slop.md)).

## Done when

- [ ] Every constraint has a downside, a model and a real example.
- [ ] Top 2 models named with remaining risk.

## Output

```
| Constraint | Honest downside | Model where it matters least | Real example | Usable reframe |
```

## Not this skill's job

Segment scoring (`segment-scout`).

Research behind this skill: [references/research.md](references/research.md).
