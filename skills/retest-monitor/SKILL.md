---
name: retest-monitor
description: Reruns a saved test suite (Break Report tests and red-team conversations) after any model, prompt, provider or workflow change, or on a monthly schedule, diffs the results against the last run, and flags new failures before the client notices. Use for retainers, after upgrades, or when a client reports something changed.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Retest monitor

**Core rule:** compare with the last run, not with memory. A pass today means nothing without the same test from last time beside it.

## Input

- The saved suite: Break Report tests and red-team conversations, with expected results.
- The last run's results.
- What changed since then (model version, prompt edit, provider, workflow edit), if known.

## Steps

1. Record versions: model name and version, prompt hash or date, n8n or platform version.
2. Rerun every test in the suite under the same conditions as last time.
3. Diff: new fails, new passes, unchanged.
4. For each new fail, check whether the change list explains it. If nothing changed on the owner's side, suspect the model provider; hosted models can shift behaviour without notice.
5. Report new fails first, with both runs' evidence.
6. Add any new real-world failure the client reported to the suite, so it is tested from now on.

## When to run

- After any prompt, model, provider or workflow change.
- After a platform update (for example an n8n security release).
- Monthly on a retainer, even if nothing changed.

## Rules

- Same inputs, same order, fresh sessions.
- Evidence for both runs ([evidence-rule](references/evidence-rule.md)).
- Short plain report ([anti-slop](references/anti-slop.md)).

## Done when

- [ ] Versions recorded.
- [ ] Every suite test rerun.
- [ ] Diff table produced, new fails first.
- [ ] New real-world failures added to the suite.

## Output

```
Run 2026-12-10 vs 2026-11-10 | model: ... | prompt: ...
| Test | Last run | This run | Change | Evidence |
```

## Not this skill's job

Designing new tests (`break-tester`, `chatbot-red-teamer`).

Research behind this skill: [references/research.md](references/research.md).
