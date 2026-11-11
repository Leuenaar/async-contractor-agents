---
name: outreach-drafter
description: Drafts one cold outreach email for one company, led by a specific checked detail about that company, under 100 words, with text hyperlinks and a plain signature, saved as a Gmail draft for the owner to send. Use when the owner has a researched target and wants an outreach, hail mary or service email written.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule,human-gate"
---

# Outreach drafter

**Core rule:** the first sentence is about them, specific enough that it could not be sent to anyone else.

## Input

- One company and one checked detail (a slow reply to a test enquiry, a broken form, a job post, a public review).
- The decision maker's name if known.
- The proof link that matches their problem.

## Layout

```
Hi [first name],

[One sentence: the specific thing you saw or tested, with day and time if it was a test.]

[One sentence: what that costs them, in their terms.]

**What I built:** [one line]
**What you'd get:** [one line, fixed price or free sample]

[One-sentence intro to the link]
[Proof link as linked text on its own line]

[One yes-or-no question.]

[Name]
Website · LinkedIn (both as linked text)
```

## Steps

1. Confirm the detail is real and recent. If it came from memory or a guess, stop and verify.
2. Write the draft in the layout above, under 100 words in the body.
3. Every link is linked text. The visible domain matches the real link. No URL shorteners or tracking wrappers.
4. Check it against every other draft in the batch: no shared sentences. Each email is written for its reader.
5. Save as a Gmail draft. Never send.

## Rules

- Under 100 words. First-touch emails under 80 words perform best in large benchmarks.
- No follow-ups scheduled unless the owner asks for them.
- Max 15 cold emails a day, at least 5 minutes apart, after a seed test to the owner's own inbox.
- No flattery without a fact behind it ("love your work" is out; "your Google reviews mention 2-day reply times" is in).
- [anti-slop](references/anti-slop.md), [evidence-rule](references/evidence-rule.md), and sending stays with the owner ([human-gate](references/human-gate.md), tier 2).

## Done when

- [ ] First sentence names a checked, specific detail.
- [ ] Body under 100 words.
- [ ] Links are linked text, domains match, no wrappers.
- [ ] No sentence repeated from another draft in the batch.
- [ ] Saved as a Gmail draft, not sent.

## Not this skill's job

Choosing who to email (`segment-scout`). Deliverability setup (SPF, DKIM, DMARC; see the security repo).

Research behind this skill: [references/research.md](references/research.md).
