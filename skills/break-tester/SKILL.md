---
name: break-tester
description: Designs and runs deliberate failure tests on a built automation (provider outages, dead API keys, floods, bad input, duplicates, retries), records each result as a Break Report row with evidence, fixes what fails and retests. Use after a workflow is built and before handover, or when a client asks how the system behaves when something breaks.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
  templates: "break-report"
---

# Break tester

**Core rule:** a test that was not run did not pass. Every row carries a run ID, a screenshot or a log line.

## Input

- The build spec and its dependency list.
- A test copy of the workflow, or permission to test on the live one with test data.
- The owner's notification channel, so alerts can be seen arriving.

## Steps

1. Write the steady state: what a normal run produces (customer reply sent, owner alerted, row saved) and how long it takes.
2. For each dependency, write a hypothesis: "If the email provider is down, the lead is still saved and the owner is alerted."
3. Break one thing at a time. Use the cheapest real method: a wrong API key, a blocked host, a Stop and Error node, a disabled credential. Never break more than one dependency per run unless the test is about combined failure.
4. Run with test data. Record the execution ID and what each party saw: the customer, the owner, the logs.
5. Compare with the hypothesis. Pass, or fail with what actually happened.
6. For each fail, fix, then rerun the same test. A fixed row shows both run IDs.
7. Run the input tests: invalid email, empty field, duplicate submission, very long text, another language, a flood of 20 submissions in a minute.
8. Write the Break Report. Lead with the most serious failure found, even if fixed.

## Standard test set

| ID | Break | Hypothesis to check |
| --- | --- | --- |
| OPS-01 | Email provider unreachable | Lead saved, owner alerted |
| OPS-02 | Alert channel unreachable | Error workflow fires on a second channel |
| OPS-03 | CRM write fails | Customer reply and owner alert already sent |
| OPS-04 | All LLM keys invalid | Lead marked urgent and routed to a person |
| OPS-05 | First LLM key invalid | Second key takes over |
| OPS-06 | 20 leads in one minute | Owner can tell it is unusual, nothing dropped |
| OPS-07 | Workflow silently stops | Daily heartbeat missing triggers an alert |
| OPS-08 | Invalid email, empty field, duplicate | Rejected or merged with a clear reason |
| OPS-09 | Retry after timeout | No duplicate customer email |

## Rules

- Test data only. Never send test messages to real customers.
- A fallback that hides a problem is a fail (for example, a flood that looks like a normal day).
- Results are written as observed. "Should work" is not a result ([evidence-rule](references/evidence-rule.md)).
- Report wording follows [anti-slop](references/anti-slop.md).

## Done when

- [ ] Steady state written before any break.
- [ ] Every dependency has at least one test row.
- [ ] Every row has a run ID or screenshot.
- [ ] Every fail is fixed and retested, or listed as a known limit.
- [ ] Break Report filled from [assets/break-report.md](assets/break-report.md).

## Not this skill's job

Adversarial conversations with a chatbot (`chatbot-red-teamer`). Rerunning the suite monthly (`retest-monitor`).

Research behind this skill: [references/research.md](references/research.md).
