---
name: build-director
description: Writes the build spec that Claude or another coding model builds from, giving the AI one narrow decision per step, keeping prices and business rules in plain code, defining when to hand off to a person, and attaching a test plan. Use after a scope is approved and before any code is written.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,human-gate"
---

# Build director

**Core rule:** use the simplest thing that passes the tests. An LLM call is used only where plain code cannot decide.

## Input

- The approved scope.
- The client's systems and accounts.
- The source of truth for prices, policies and rules (a price list, a policy page).

## Steps

1. Draw the flow as numbered steps: trigger, each action, each output.
2. For each step, mark who decides: plain code, AI, or a person. Default to plain code.
3. Where AI decides, write its one job as a classification or extraction with a fixed set of outputs (for example `job_type` in `[leak_repair, install, service, other]`). Free text from the AI never reaches money, prices or legal wording.
4. Write the handoff rule: when confidence is low, the input is off-topic, or the AI returns "other", the flow sends it to a person and tells the customer a person will reply.
5. Order side effects so the customer and the owner hear first. Logging to a CRM comes after alerts and replies, so a CRM failure does not silence the alert.
6. List every external dependency (email, chat, CRM, each LLM key) and its failure behaviour. This list becomes the `break-tester` plan.
7. Write acceptance tests from the scope's pass conditions.

## Rules

- One AI decision per step, with an allowed-values list. No AI step chooses tools or next steps on its own unless the scope says so.
- Prices come from the owner's list through code: `base + extras + tax`, never "the AI quotes".
- Secrets live in the platform's credential store, never in node text or the spec.
- The spec names which actions are irreversible and how they are confirmed ([human-gate](references/human-gate.md)).
- Claims about how the system behaves are tested before they go in a proposal or case study ([evidence-rule](references/evidence-rule.md)).

## Done when

- [ ] Every step is marked code, AI or person.
- [ ] Every AI step has a fixed output set and a handoff path.
- [ ] Customer reply and owner alert happen before CRM writes.
- [ ] Dependency list with failure behaviour exists.
- [ ] Acceptance tests cover every scope deliverable.

## Output

```
Step 3  AI   classify job_type in [leak_repair, install, service, other]; other -> step 7 (person)
Step 4  code price = list[job_type] + extras + GST 9%
Step 5  code send customer reply (template, price from step 4)
Step 6  code alert owner on Telegram
Step 7  code write CRM row (after 5 and 6)
```

## Not this skill's job

Writing the code (the coding model does that). Running failure tests (`break-tester`).

Research behind this skill: [references/research.md](references/research.md).
