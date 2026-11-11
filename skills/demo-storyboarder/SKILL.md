---
name: demo-storyboarder
description: Plans a short silent demo video of a real working build (scene list with timings, on-screen text, callouts, captions and a cover frame) that makes sense with the sound off and shows only what the demo really does. Use when turning a demo into a LinkedIn, Contra or portfolio video, or before recording a screen walkthrough.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule"
---

# Demo storyboarder

**Core rule:** if the video makes no sense on mute, it fails. Most viewers will never turn the sound on.

## Input

- The working demo (URL or recording).
- The one thing the viewer should leave with ("prices come from the owner's list, not the AI").
- Target length and platform.

## Steps

1. Write the one-line takeaway. Every scene serves it.
2. Pick the real moments to show: the customer message, the reply, the price line, the handoff, the owner's view. Record them from the real demo.
3. Write the scene list: time range, what is on screen, the on-screen headline (under 8 words), any callout ring.
4. Open on the problem in the first 3 seconds, as text on screen.
5. Add captions for any spoken words. Sound design is optional and quiet.
6. Pick the cover frame: the clearest single frame, with the headline.
7. End on the product name and site. No "thanks for watching".

## Rules

- 30 to 45 seconds for feeds. 4:5 or 1:1 framing for LinkedIn feeds.
- Every callout points at something that really happens in the demo ([evidence-rule](references/evidence-rule.md)). No mocked screens presented as live.
- On-screen text follows [anti-slop](references/anti-slop.md).
- A recorded voice walkthrough is allowed; live calls are not part of this skill.

## Done when

- [ ] Takeaway written.
- [ ] Every scene comes from the real demo.
- [ ] Watched once on mute and still clear.
- [ ] Under 45 seconds for feed versions.

## Output

```
| Time | On screen | Headline | Callout |
| 0.0-2.9 | 23:47 clock | An aircon starts leaking | none |
```

## Not this skill's job

Written posts (`break-log-writer`). Rendering the video (use a video tool).

Research behind this skill: [references/research.md](references/research.md).
