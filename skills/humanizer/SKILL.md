---
name: humanizer
description: Rewrites a draft so it reads like a specific person wrote it, removing AI writing patterns (em dashes, negative parallelisms, reflex triplets, cliche vocabulary, chatbot openers and closers) while keeping every fact, number and link unchanged. Use as the last step before any text is sent, posted or submitted, or when the owner says a draft sounds like AI.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "anti-slop"
---

# Humanizer

**Core rule:** change how it is said, never what it says. Facts, numbers, names and links come out exactly as they went in.

## Input

- The draft.
- Where it goes (email, form box, post, report) and any length limit.
- Optional: a sample of the owner's own writing to match.

## Steps

1. List the facts in the draft: every number, name, date, link and claim.
2. Run the checks in [anti-slop](references/anti-slop.md) and mark each hit.
3. Rewrite the marked sentences. Prefer cutting to replacing.
4. Read the first and last sentence alone. The first answers or says something specific. The last is a fact or a direct question.
5. Vary sentence length: some under 8 words, none over 30.
6. Compare the fact list with the rewrite. Anything missing or changed is restored.
7. Check the length limit.

## Rules

- Do not add facts, examples or claims to make text "sound human". Only reshape what is there.
- Do not add casual slang the owner would not use in that channel.
- If the owner's sample is given, match its sentence length and punctuation habits.
- Return the clean text only, then a one-line list of what changed.

## Done when

- [ ] Zero em dashes.
- [ ] Zero words from the cliche list.
- [ ] No opener or closer of the "Great question / hope this helps" type.
- [ ] Fact list identical before and after.
- [ ] Within the length limit.

## Output

```
[clean text]

Changed: removed 2 em dashes, cut "robust", rewrote the closing offer as a question.
```

## Not this skill's job

Checking whether claims are true (`evidence-auditor`, `fact-checker`).

Research behind this skill: [references/research.md](references/research.md).
