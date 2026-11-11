---
name: segment-scout
description: Scores market segments before picking companies to approach, using weighted fit and reachability criteria with cited evidence, then lists 5 to 10 companies inside the winning segment. Use when choosing a niche, an outreach target list, or deciding where to look for clients next.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,anti-slop"
---

# Segment scout

**Core rule:** pick the segment first, the company second. A perfect company inside a segment that cannot pay or cannot be reached is wasted research.

## Input

- A market idea or a list of candidate segments (for example "plumbing businesses in Singapore", "small n8n agencies").
- The owner's current proof: which demos, test reports and case studies exist. Read them, do not assume.
- Constraints: async only, no live calls, timezone UTC+7.

If the proof list is missing, ask once.

## Steps

1. List 3 to 6 candidate segments. A segment is a type of buyer plus a place, never a single company.
2. Score each segment 1 to 5 on the six factors below. Every score cites a source opened in this session, or is marked "unverified" and capped at 2.
3. Multiply by the weights and rank.
4. Apply the negative signals as subtractions after the weighted total.
5. For the top segment only, find 5 to 10 real companies and note one specific detail per company (a slow reply, a broken form, an after-hours gap, a job post). That detail is what an outreach email will lead with.
6. Write a one-line prediction ("expect 1 reply from 10 emails") and save it, so the result can be compared later.

## Weights

| Factor | Weight | 5 looks like | 1 looks like |
| --- | --- | --- | --- |
| Ability to pay | 25% | Spends on software or contractors already | Price is the only decision factor |
| Strength of the owner's proof for this need | 25% | A tested demo of this exact job exists | Nothing built that resembles it |
| Pain visibility | 15% | The leak can be seen from outside (test enquiry, public reviews) | Pain has to be guessed |
| Reachability, async | 15% | Public email or form, decision maker reads it | Only phone or in-person |
| Cost to serve | 10% | Same build reused with small changes | Custom work every time |
| Competition | 10% | Few sellers show proof for this | Crowded with cheap gigs |

## Negative signals (subtract)

- Buyers expect calls or WhatsApp voice notes as the main channel: minus 1.0.
- Segment already contacted in the last 30 days with zero replies: minus 0.5.
- Legal or regulated data (health, finance) the owner cannot handle yet: minus 1.0.

## Rules

- Follow [evidence-rule](references/evidence-rule.md): a score without a source is "unverified".
- Follow [anti-slop](references/anti-slop.md) in the written summary.
- Stop at the target count. More companies than needed is wasted context.
- Never suggest warm-network or referral routes unless the owner asks; this repo assumes none.

## Done when

- [ ] Every factor score has a link or is marked unverified.
- [ ] The top segment beats the second by a stated margin, or the tie is called out.
- [ ] Each listed company has one specific, checked detail.
- [ ] A prediction is written down with a date.

## Output

```
| Segment | Pay | Proof | Pain | Reach | Cost | Comp | Weighted | Neg | Final |
| SG plumbing 1-20 staff | 4 | 5 | 4 | 4 | 4 | 3 | 4.15 | -0.5 | 3.65 |

Top segment: ...
Companies: name, site, detail, source link
Prediction (2026-11-10): ...
```

## Not this skill's job

Writing the emails (use `outreach-drafter`). Screening job listings (use `job-screener`).

Research behind this skill: [references/research.md](references/research.md).
