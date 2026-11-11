---
name: devils-advocate
description: Attacks a plan, positioning, proposal or decision the way a skeptical buyer, competitor or reviewer would, using a premortem (assume it already failed, list why), and returns the objections that have no answer yet with what would answer them. Use before committing to a strategy, sending a high-stakes proposal, or when the owner asks for blunt criticism.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Devil's advocate

**Core rule:** assume it already failed. Find the reasons. Kind criticism that hides a real problem is worse than none.

## Input

- The plan, positioning, proposal or decision, in writing.
- Who it is aimed at (buyer type, reviewer, platform).

## Steps

1. Write the failure: "It is three months later. This produced nothing." Make it specific to the plan.
2. List every reason it could have failed, from three viewpoints: the buyer ("why would I not pick this?"), the competitor ("how do I beat this?"), the reviewer or platform ("what here is not true or not allowed?").
3. For each reason, check the plan: is there already an answer in it? Mark answered or open.
4. For open reasons, say what would answer them: a fact to check, a test to run, a change to make.
5. Rank open reasons by how likely and how damaging they are.
6. Give a verdict: keep, change, or drop. One line on why.

## Rules

- At least one objection per viewpoint. If none can be found, say so and why.
- Objections about facts get checked, not argued ([evidence-rule](references/evidence-rule.md)).
- Blunt, specific, no padding ([anti-slop](references/anti-slop.md)). No "great plan, but".
- A premortem produces more reasons, not certainty. Say the verdict's confidence.

## Done when

- [ ] Failure scenario written.
- [ ] All three viewpoints covered.
- [ ] Each objection marked answered or open.
- [ ] Open objections have a concrete answer path.
- [ ] Verdict with confidence.

## Output

```
| Viewpoint | Objection | Answered in plan? | What would answer it | Risk |
Verdict: change. Confidence: medium.
```

## Not this skill's job

Checking individual claims line by line (`evidence-auditor`).

Research behind this skill: [references/research.md](references/research.md).
