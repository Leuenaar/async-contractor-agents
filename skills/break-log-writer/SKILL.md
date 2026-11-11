---
name: break-log-writer
description: Writes one Break Log post for LinkedIn or Contra from one real failure test, showing a problem a small-business owner would feel, what was broken on purpose, what the customer and owner saw, and the fix, without any sales pitch or link in the body. Use for weekly public posts that build proof without selling.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop,evidence-rule,human-gate"
---

# Break log writer

**Core rule:** pull, never push. The post shows why the problem matters and proof it can be handled. It never says "hire me".

## Input

- One Break Report row, with its run ID or screenshot.
- The post number in the series (Break Log #1, #2, ...).

## Structure

1. **Hook (first 150 characters, before "see more"):** a concrete situation the owner recognises. "Your booking form works. What happens at 9pm when the email service is down?"
2. **The cost:** one or two lines on what that failure does to a real business.
3. **The test:** what was broken on purpose, in plain words.
4. **What happened:** what the customer saw, what the owner was told. Include the first result if it was a fail.
5. **The fix:** one or two lines.
6. **Close:** one question to owners about their own setup. Not "agree?", not "comment below".
7. Attach the screenshot or a short document of the test. No link in the body.

## Rules

- 120 to 220 words. Short paragraphs, one idea each.
- At most 2 hashtags, inline or at the end, relevant only.
- External links cut reach sharply; put the portfolio in the profile, not the post.
- Demo work is called a demo test ([evidence-rule](references/evidence-rule.md)).
- [anti-slop](references/anti-slop.md) applies; this is the most read text in the repo's output.
- The owner posts it. Never post ([human-gate](references/human-gate.md), tier 2).

## Done when

- [ ] Hook is under 150 characters and concrete.
- [ ] One real test with evidence attached.
- [ ] No "hire me", no offer, no link in the body.
- [ ] Ends on a question about the reader's setup.

## Not this skill's job

Long-form write-ups (`case-study-writer`). Video posts (`demo-storyboarder`).

Research behind this skill: [references/research.md](references/research.md).
