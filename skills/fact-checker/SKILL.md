---
name: fact-checker
description: Verifies numbers, dates, names, quotes and links in a draft before it is sent or published, using lateral reading (checking what other sources say about a claim and its source) and tracing each claim to its original source. Use on research summaries, posts, reports and proposals that cite outside facts.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule"
---

# Fact checker

**Core rule:** trace every outside fact to where it started. A blog quoting a study is not the study.

## Input

- The draft and its sources.

## Steps (SIFT)

1. **Stop:** list every outside fact: numbers, dates, names, quotes, rankings, prices.
2. **Investigate the source:** who published it, and do they sell something related? Vendor data stays usable but is labelled "vendor data, directional".
3. **Find other coverage:** search for the same fact elsewhere. One source only means "single source".
4. **Trace to the original:** follow the citation to the first publisher. Check the original says what the draft says, with the same scope (for example "number of reasons generated", not "accuracy").
5. Check every link opens and lands on the cited content.
6. Mark each fact: confirmed, corrected, single source, or remove.

## Rules

- A search snippet is not a source. Open the page.
- Dates and prices change: anything about "now" is checked today.
- When the original says less than the draft, the draft changes, not the meaning of the original.

## Done when

- [ ] Every outside fact marked.
- [ ] Every link opened.
- [ ] Vendor-sourced numbers labelled.
- [ ] Corrections applied or listed.

## Output

```
| Fact | Draft says | Original says | Source | Status |
```

## Not this skill's job

Claims about the owner's own work (`evidence-auditor`).

Research behind this skill: [references/research.md](references/research.md).
