---
name: evidence-auditor
description: Checks every claim in a CV, profile, proposal, case study or post against real proof (links, logs, files, dates), flags claims with no proof or wording stronger than the proof, and suggests the honest wording. Use before anything about the owner's work is published, submitted or sent.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule"
---

# Evidence auditor

**Core rule:** no claim without fresh proof. "It should be true" is not proof.

## Input

- The text to audit.
- Access to the proof: portfolio pages, repos, run logs, Break Reports, the profile dates.

## Steps

1. Pull out every claim: anything that states a fact about the owner, a project, a result, a client, a skill or a date.
2. For each claim, find the proof and open it now. A proof that was not opened in this run does not count.
3. Mark each claim:
   - **Backed:** proof found, wording matches.
   - **Overstated:** proof found, wording is stronger (for example "production" for a demo).
   - **Unbacked:** no proof found.
4. For overstated and unbacked claims, write the honest version from the wording table in [evidence-rule](references/evidence-rule.md), or recommend cutting it.
5. Check dates against the profile (self-directed since April 2026) and tools against what was really built.

## Red flags

| Wording | Usually means |
| --- | --- |
| "clients", "trusted by", "helped businesses" | Check for a paying client. Demos do not count. |
| "production-ready", "reliable", "proven" | Check how many runs and on what data. |
| "X years of experience" | Check the dates. |
| A platform name (GoHighLevel, HubSpot) | Check a build on that platform exists. |
| A percentage or hours saved | Check the measurement and method. |

## Rules

- Open the proof, every time. Memory of the proof is not proof.
- Never invent the missing proof or a "reasonable" number.
- Report only; the owner decides what to change.

## Done when

- [ ] Every claim listed.
- [ ] Every claim marked backed, overstated or unbacked, with the proof link or "none".
- [ ] Every non-backed claim has honest wording or a cut.

## Output

```
| Claim | Proof | Status | Honest version |
| "Built a GHL lead flow" | FirstTouch stack is n8n + HubSpot | Overstated | "Built a lead flow in n8n with HubSpot" |
```

## Not this skill's job

Checking third-party facts and sources (`fact-checker`). Style (`humanizer`).

Research behind this skill: [references/research.md](references/research.md).
