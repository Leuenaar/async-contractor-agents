---
name: form-filler
description: Answers job, gig and platform application forms one box at a time, as copy-ready blocks labelled with the box name, honest about experience and language level, and flags boxes only the owner can answer. Use when the owner pastes application questions, profile fields or screening forms.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule,human-gate"
---

# Form filler

**Core rule:** one box, one block, the box's own label above it. The owner should be able to copy each block without reading around it.

## Input

- The form questions exactly as shown, including option lists and limits ("140 characters", "C2 CEFR").
- The owner's profile facts: dates, languages, projects, location as used in applications.

## Steps

1. Split the form into boxes. Keep the box labels word for word.
2. For each box decide the type: fact (country, years), self-rating (language level, experience), choice (Yes/No, options), or free text.
3. Facts: answer from the profile. If not in the profile, mark "owner must fill" instead of guessing.
4. Self-ratings: pick the honest level the owner can defend in a test. Most platforms test language and skill claims later; a mismatch looks like overclaiming.
5. Choices: pick the option, then one line on why if it is not obvious (for example "No" to voice-recording experience because there is none).
6. Free text: write to the limit given, in the platform's language. Lead with the most relevant proof.
7. Before handing over, list any box whose answer could disqualify the application, so the owner decides with eyes open.

## Rules

- No placeholders like [x] or "insert here". If a value is unknown, the block says "owner must fill" and nothing else.
- Years of experience come from real dates. Rounding up is overclaiming ([evidence-rule](references/evidence-rule.md)).
- Leave optional education fields empty unless the form requires them.
- Referral boxes: "No referral" if none. Never invent a name; some companies check.
- Prefilled values from earlier applications get rechecked (old addresses and phone numbers carry over).
- Writing follows [anti-slop](references/anti-slop.md). Never press submit ([human-gate](references/human-gate.md)).

## Done when

- [ ] Every box has a block or an "owner must fill" marker.
- [ ] No answer claims more than the profile shows.
- [ ] Character limits counted and met.
- [ ] Disqualifying answers listed for the owner.

## Output

```
**What is your nationality?**
Indonesian

**How many years of professional translation experience do you have?**
0

Boxes that may disqualify: "Do you have voice recording experience?" = No.
```

## Not this skill's job

Cover letters with weaknesses and plans (write those as a separate task). Proposals (`upwork-proposal`).

Research behind this skill: [references/research.md](references/research.md).
