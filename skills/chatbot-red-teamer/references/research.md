# Research notes: chatbot-red-teamer

## Findings used

- OWASP Top 10 for LLM Applications 2025: prompt injection (LLM01), sensitive information disclosure (LLM02), improper output handling (LLM05), excessive agency (LLM06), system prompt leakage (LLM07), misinformation (LLM09). The categories above map to these. Source: https://genai.owasp.org/llm-top-10/
- promptfoo's red team process: define the vulnerability types that matter for the app, generate broad adversarial inputs, test end to end in a production-like setup, grade with deterministic checks plus model grading plus human review, rerun after fixes. Source: https://www.promptfoo.dev/docs/red-team/
- Incidents: Air Canada liable for a wrong refund answer from its chatbot ($812.02 awarded by the BC Civil Resolution Tribunal); Cursor's support bot invented a one-device policy and users announced cancellations; a Chevrolet of Watsonville bot said it would sell a 2024 Tahoe for $1 (Dec 2023, no binding sale resulted). Sources: https://www.cxtoday.com/conversational-ai/court-orders-air-canada-to-pay-out-for-chatbots-bad-advice/ , https://www.cxtoday.com/conversational-ai/a-contact-center-chatbot-invents-company-policies-now-customers-want-out/ and https://letsdatascience.com/news/chevrolet-chatbot-accepts-1-tahoe-offer-973398ee
- Market prices for similar work: Contra guardrail assessment from $2,500 in 4 days; SMB "AI audit" tiers of $200-500 entry and $999-1,500 productized (vendor source, biased). Sources: https://contra.com/s/rBkvgMss-ai-guardrail-and-adversarial-reliability-assessment and https://signalarc-io.pages.dev/blog/how-much-does-an-ai-audit-cost.html

## Targets that shaped it

- Frontdesk demo bot (aircon, plumbing, renovation): price pressure and handoff categories come from its design.
- Bots in Southeast Asia that switch between English, Indonesian and Malay: the language-switching category.
