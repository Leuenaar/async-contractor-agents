# Research notes: break-tester

## Findings used

- Principles of Chaos Engineering: define steady state from observable output, write a hypothesis that it holds, inject real-world events (server failures, malformed responses, traffic spikes) ordered by impact, automate, minimise blast radius. Source: https://principlesofchaos.org/
- n8n error handling: an error workflow starting with an Error Trigger receives the execution ID, URL, error message, last node run and workflow name; a Stop and Error node forces a failure on purpose. Source: https://docs.n8n.io/flow-logic/error-handling/
- Silent failure is the pain buyers report most: one agency lost a $2,500/month client after an n8n lead flow died unnoticed for 3 days, about 40 leads lost. Source: https://www.indiehackers.com/post/lost-a-2-500-month-client-in-my-ai-automation-agency-in-the-worst-way-possible-T1lcOPJFmIvuMLkkSbmT
- Testlio (April 2026) reported nearly half of high-severity chatbot issues came from guardrails and fallback handling. Source: https://itbrief.com.au/story/testlio-launches-ai-chatbot-testing-service-amid-scrutiny

## Targets that shaped it

- FirstTouch failure log (Oct 2026): #710 CRM failed before alert (fixed by reordering), #715 retest, #730 email provider down, #735 Telegram down, all three Groq keys dead with fallback to a person, and a first fallback that made a flood look routine. The standard test set is built from these runs.
