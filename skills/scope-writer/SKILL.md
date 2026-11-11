---
name: scope-writer
description: Turns a loose client brief into a written scope with testable deliverables, assumptions, an explicit out-of-scope list, a change rule and a fixed estimate, plus one list of questions if anything is unknown. Use before quoting a price, accepting a contract, or when a client asks "how much for this?".
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule"
  templates: "scope"
---

# Scope writer

**Core rule:** if a deliverable cannot be tested, it is not a deliverable yet. Rewrite it until it can be.

## Input

- The client's brief, word for word.
- Answers to earlier questions, if any.
- The tools the client already uses and pays for.

## Steps

1. Copy every request out of the brief as a line. Keep the client's words.
2. Turn each line into a deliverable with a test: "acknowledgement email sent" becomes "a valid test submission produces an acknowledgement email within 2 minutes".
3. List assumptions: which accounts the client provides, who pays for API usage, what data is test data.
4. Write the out-of-scope list. Name the obvious next asks (more forms, a dashboard, WhatsApp) so the client sees the edge.
5. Write the change rule: anything not listed is quoted separately before work starts.
6. Estimate hours per deliverable, add 20% buffer, and turn it into one fixed price. Show the hours only if the client asks.
7. If anything blocks a test from being written, add it to one question list. Send the list once, not one question at a time.

## Rules

- No deliverable is "make it smart", "use AI where useful" or "optimise". Each one has a pass condition.
- AI is used for one narrow decision per step. Prices, rules and money stay in plain code. Say so in the scope.
- Ongoing costs (API, hosting, WhatsApp fees from Meta) are listed as the client's, with rough monthly ranges marked as estimates.
- [anti-slop](references/anti-slop.md) and [evidence-rule](references/evidence-rule.md) apply: no outcome promises ("will double your leads").

## Done when

- [ ] Every request in the brief maps to a deliverable with a pass condition.
- [ ] Out-of-scope list has at least three items.
- [ ] Change rule present.
- [ ] One fixed price, one delivery date.
- [ ] Questions, if any, sent as one list.

## Output

Fill [assets/scope.md](assets/scope.md).

## Not this skill's job

The build spec Claude codes from (`build-director`). The test run (`break-tester`).

Research behind this skill: [references/research.md](references/research.md).
