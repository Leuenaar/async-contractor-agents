---
name: case-study-writer
description: Writes a case study from a project's real logs, test results and Break Report, structured as challenge, what was built, how it was tested, results and known limits, with every number sourced and demo work labelled as demo work. Use when a project is finished and needs to become public proof on a portfolio, Contra, Upwork or LinkedIn.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule"
  templates: "case-study"
---

# Case study writer

**Core rule:** small buyers read case studies for the problem and how it was solved. Lead with their problem, prove the solution with the test log, and say what is still open.

## Input

- Project files: spec, build notes, run logs or execution IDs.
- The Break Report.
- Whether the client is real (and agreed to be named) or the project is a demo.

## Structure

1. **Title:** what it does, for whom. "Lead intake for a plumbing business that answers in under a minute", not "Revolutionizing lead management".
2. **The problem:** one paragraph in the buyer's words. What happened before, what it cost.
3. **What was built:** the flow in 5 to 7 steps. Name where AI decides and where plain code decides.
4. **How it was tested:** the Break Report summary. Name the most serious failure found and how it was fixed.
5. **Results:** only measured numbers, each with its source. For demos: test results, not business results.
6. **Known limits:** what was not tested, what still fails, what it needs from the client.
7. **Stack:** tools, one line.
8. **Links:** live demo, repo, Break Report.

## Rules

- Demo or fictional client: say so in the first paragraph ([evidence-rule](references/evidence-rule.md)).
- No em dash, no marketing adjectives ([anti-slop](references/anti-slop.md)). Describe the owner's role as the profile does (a builder who directs AI), not as a developer.
- Every number links to its run, log or screenshot.
- Real client names only with written permission.

## Done when

- [ ] Demo status stated in the first paragraph, if a demo.
- [ ] The most serious failure found appears, with its fix.
- [ ] Every number has a source link.
- [ ] Known limits section is not empty.

## Output

Fill [assets/case-study.md](assets/case-study.md).

## Not this skill's job

Short social posts (`break-log-writer`). Video (`demo-storyboarder`).

Research behind this skill: [references/research.md](references/research.md).
