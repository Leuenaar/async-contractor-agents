# Research notes: build-director

## Findings used

- Anthropic, "Building effective agents": find the simplest solution and add complexity only when it clearly improves results; workflows (predefined code paths) suit well-defined tasks; routing classifies an input and hands it to a dedicated handler; guardrails work better as a separate check than inside the main call; add programmatic checks between steps. Source: https://www.anthropic.com/engineering/building-effective-agents
- OWASP LLM06 Excessive Agency: give the model the minimum tools and permissions and enforce authorization outside the model. Source: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- Real incidents where AI text reached prices or policy: Air Canada was held liable after its chatbot gave a wrong refund answer (2024); a Chevrolet of Watsonville bot said it would sell a 2024 Tahoe for $1 (Dec 2023, no binding sale). Sources: https://www.cxtoday.com/conversational-ai/court-orders-air-canada-to-pay-out-for-chatbots-bad-advice/ and https://letsdatascience.com/news/chevrolet-chatbot-accepts-1-tahoe-offer-973398ee

## Targets that shaped it

- Frontdesk demo (Nov 2026): AI only identifies the job; code computes 60 + 20 + 10 + 8.10 GST = S$98.10; unknown questions go to a person. The output example follows this design.
- FirstTouch test #710: a CRM step failing before the alert silenced the owner alert. The fix (alerts and replies first) became step 5.
