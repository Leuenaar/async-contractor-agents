---
name: competitor-map
description: Maps how competing freelancers and small agencies position themselves (headlines, proof shown, prices), marks where the market is saturated and where almost nobody stands, and names 3 to 5 white spaces with the owner's existing proof for each. Use when choosing positioning, writing a profile headline, or pricing a service.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Competitor map

**Core rule:** a white space only counts if the owner already has proof for it, or a plan to get proof soon. Empty ground with no proof is just empty.

## Input

- The service area and platforms to map (Upwork, Fiverr, Contra, LinkedIn).
- The owner's proof list.

## Steps

1. Sample 15 to 30 real listings or profiles. Record headline, proof shown, price, reviews.
2. Group the headlines into patterns. Count how many use each.
3. Record what proof the crowd shows: canvas screenshots, project counts, ratings, demos, test reports.
4. Mark saturated patterns (many sellers, same claim, price war) and thin ones (few sellers, real demand evidence).
5. For each thin area, check demand evidence (link) and the owner's proof (link). No both, no white space.
6. Name 3 to 5 white spaces, ranked.

## Rules

- Every pattern count comes from listings actually opened ([evidence-rule](references/evidence-rule.md)).
- Copying a competitor's wording is out; the map is for finding gaps.
- Plain output ([anti-slop](references/anti-slop.md)).

## Done when

- [ ] At least 15 listings sampled, with links saved.
- [ ] Saturated and thin areas both named.
- [ ] Each white space has demand evidence and owner proof linked.

## Output

```
| Pattern | Count | Typical price | Proof shown | Saturation |
White spaces: 1. ... (demand: link, proof: link)
```

## Not this skill's job

Demand sizing (`market-demand`).

Research behind this skill: [references/research.md](references/research.md).
