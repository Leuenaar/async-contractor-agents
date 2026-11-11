---
name: upwork-proposal
description: Writes one Upwork proposal for one job post, opening with the closest matching proof, answering every screening question, placing any required keyword first, and stating the Connects cost. Use when the owner picks an Upwork job and wants a proposal draft, or asks how to answer a job's screening questions.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule,human-gate"
---

# Upwork proposal

**Core rule:** the first two lines show the client their own problem solved once already, with a link. Everything after supports that.

## Input

- The full job post, including screening questions and any required keyword.
- The owner's proof list: demos, Break Reports, case studies, repo links.
- Connects balance.

## Steps

1. Pull out of the post: the deliverables, the tests the client asked for, the keyword, the budget, the questions.
2. Pick the one piece of proof closest to the deliverables. If none is close, say so to the owner before writing; a weak match is better handled honestly than dressed up.
3. Write the opening: keyword first if required, then one sentence naming the client's workflow, then the proof link.
4. Map each deliverable to how it will be built and tested, one line each. Reuse the client's own words for the deliverables.
5. If the client listed test cases, answer with the Break Report format: each test, what will be checked, what they will receive.
6. State price and timeline plainly. Fixed-price posts get a fixed number, not a range.
7. Answer every screening question separately, labelled with the question.
8. Close with one question about their setup, never a generic offer.
9. Count Connects needed against the balance and say if more must be bought.

## Length

Short posts and small budgets: 120 to 250 words. Detailed posts with test requirements or budgets above $1,000: longer is fine if every paragraph answers something in the post. Research shows both very short and very long proposals outperform the middle; padding does not.

## Rules

- [anti-slop](references/anti-slop.md) applies line by line. No "I hope this finds you well", no "I am confident".
- [evidence-rule](references/evidence-rule.md): demos are called demos. No invented client count, hours saved or ratings.
- Do not claim platforms the owner has not built with (for example GoHighLevel without a GHL build).
- Never submit. The owner pastes and sends ([human-gate](references/human-gate.md), tier 2).

## Done when

- [ ] Required keyword is the first word, if the post has one.
- [ ] Every deliverable in the post appears in the proposal.
- [ ] Every screening question has its own answer.
- [ ] Every claim has a link or is removed.
- [ ] Connects cost stated.

## Output

```
Connects: 11 needed, 1 available, buy 10.

LEADFLOW

Your form leads get reviewed and followed up by hand...
[proof link on its own line]
...

Screening question 1: ...
```

## Not this skill's job

Deciding whether to apply (`job-screener`). Writing the Break Report after the build (`break-tester`).

Research behind this skill: [references/research.md](references/research.md).
