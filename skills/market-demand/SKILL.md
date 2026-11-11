---
name: market-demand
description: Finds what buyers are paying for right now in a market (job post patterns, marketplace data, surveys, community threads), ranks 5 to 7 findings by strength of evidence with sources opened in the session, and names the demand pockets that fit the owner's proof. Use before choosing a niche, an offer or a positioning, or when the owner asks "what do people actually pay for?".
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Market demand

**Core rule:** rank findings by how strong the evidence is, not by how good the news is.

## Input

- The market or service area to research.
- The owner's proof list, so findings can be matched to it.

## Steps

1. Search four kinds of source: marketplace data (Upwork, Fiverr, Contra reports), surveys with a stated sample, job posts, and community threads where buyers complain (Reddit, n8n forum, Indie Hackers).
2. Open every page used. Note who published it and whether they sell something related.
3. Write findings as one sentence each with the number and the source.
4. Rank by evidence strength: large survey with method > platform data > many repeating anecdotes > one vendor blog > one anecdote.
5. Mark what each finding means for the owner: fits current proof, needs new proof, or does not fit.
6. Name the 2 demand pockets that fit best.

## Rules

- Sources opened in this session only ([evidence-rule](references/evidence-rule.md)).
- Vendor numbers labelled as directional.
- No finding without a number or a direct quote.
- Plain summary ([anti-slop](references/anti-slop.md)).

## Done when

- [ ] 5 to 7 findings, ranked, each with a source link.
- [ ] Evidence strength stated per finding.
- [ ] 2 demand pockets named with the proof that fits them.

## Output

```
1. [finding with number] (strength: survey, n=3,566) source
...
Best fits: ...
```

## Not this skill's job

Mapping competitors (`competitor-map`). Buyer motives (`buyer-psychology`).

Research behind this skill: [references/research.md](references/research.md).
