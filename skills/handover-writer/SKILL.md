---
name: handover-writer
description: Writes the handover runbook a non-technical client team uses after delivery, covering how to change rules and templates, how to read each alert, what to do when each known failure happens, and who to contact. Use at the end of a build, after the Break Report is done.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule"
  templates: "handover-runbook"
---

# Handover writer

**Core rule:** every alert the system can send has a matching entry that says what it means and what to do, in words the client's office manager understands.

## Input

- The final build and its spec.
- The Break Report (every failure becomes a runbook entry).
- Who on the client side will own it, and how technical they are.

## Steps

1. Name the internal owner. If the client has not named one, ask; a system with no owner is the most common reason automations die about a month after handover.
2. Write "how it works" in five lines or fewer, from the customer's point of view.
3. Write the change guides: edit a price, edit a template, add a category. Each is numbered clicks with the exact screen names.
4. For each alert and each Break Report row, write an entry: what you see, what it means, what to do now, when to call for help.
5. Add the routine checks: what to look at weekly, and the monthly retest if there is a retainer.
6. Record a short screen recording of the change guides if the scope includes it.
7. Have someone non-technical read one entry and do it. Fix what confused them.

## Entry format

```
Alert: "FirstTouch: email provider failed"
What it means: the lead was saved, but the customer did not get the acknowledgement email.
Do now: reply to the customer from your inbox using the template in the Templates sheet.
Call for help if: this happens more than twice in a day.
```

## Rules

- No jargon without a plain explanation next to it ("webhook, the link the form sends data to").
- Only describe behaviour that was tested ([evidence-rule](references/evidence-rule.md)).
- Plain language throughout ([anti-slop](references/anti-slop.md)).
- If a step is the same fixed sequence every time an alert fires, say it should be automated instead.

## Done when

- [ ] Internal owner named.
- [ ] Every alert and every Break Report row has an entry.
- [ ] Every change guide tested by following it once.
- [ ] One non-technical read-through done.

## Output

Fill [assets/handover-runbook.md](assets/handover-runbook.md).

## Not this skill's job

Testing (`break-tester`). Ongoing monitoring (`retest-monitor`).

Research behind this skill: [references/research.md](references/research.md).
