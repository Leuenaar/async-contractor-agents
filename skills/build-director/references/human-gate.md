# Human gate

Skills draft and prepare. A person approves anything that leaves the workspace or cannot be undone.

Why it matters: OWASP lists excessive agency as one of the top 10 risks for LLM applications and names human approval of high-impact actions as a key control. The opposite failure is real too: Anthropic reports users approve 93% of Claude Code permission prompts, so asking for everything turns approval into a rubber stamp. The gate below asks only where it matters.

## Tiers

| Tier | Actions | Rule |
| --- | --- | --- |
| 0 | Read, search, research, open pages | No approval. |
| 1 | Write files in the workspace, save a Gmail draft, fill a local doc | No approval. Say what was written and where. |
| 2 | Send a message or email, submit a form or application, post publicly, commit or push to a public repo, accept terms | Stop. Show the exact content and destination. Wait for a clear yes. |
| 3 | Pay, buy, delete, change account or security settings, rotate or revoke credentials | Stop. Show what changes and that it may not be undoable. Wait for a clear yes. |
| 4 | Enter passwords, card numbers, API keys or ID numbers into any field; bypass a CAPTCHA | Never. Hand the step to the person. |

## How to ask

- Show the exact text, recipient, URL or file, not a summary.
- One action per approval. A yes covers that action only.
- Silence or "looks fine" about something else is not approval.

## Sources

- OWASP Top 10 for LLM Applications 2025, LLM06 Excessive Agency: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- Anthropic Engineering, Claude Code auto mode (users accept 93% of manual permission prompts; the post gives no time period): https://anthropic.com/engineering/claude-code-auto-mode
- NeuralTrust, "Human-in-the-loop for AI agents" (tiering and approval fatigue data): https://neuraltrust.ai/blog/human-in-the-loop-ai-agents
