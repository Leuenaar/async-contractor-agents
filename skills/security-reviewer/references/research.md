# Research notes: security-reviewer

## Findings used

- Cloudflare Security Insights covers about 33 insight types, all about configuration that passes through Cloudflare (DNS, TLS, WAF, MFA, API endpoints). It does not look inside workflows, databases, servers or chatbot behaviour. Source: https://developers.cloudflare.com/security/security-insights/
- OWASP Top 10 for LLM Applications 2025 and OWASP Top 10 for Agentic Applications 2026 list risks, not test steps; the LLM and AGT layers turn them into checks. Sources: https://genai.owasp.org/llmrisk/llm062025-excessive-agency/ and https://www.giskard.ai/knowledge/owasp-top-10-for-agentic-application-2026
- Supabase splinter lints include rls_disabled_in_public, rls_enabled_no_policy, policy_exists_rls_disabled, security_definer_view, rls_references_user_metadata. Source: https://supabase.github.io/splinter/0013_rls_disabled_in_public
- n8n security audit covers 5 risk categories (credentials, database, nodes, filesystem, instance). Q1 2026 had six critical CVEs including CVE-2026-21858 "Ni8mare", unauthenticated RCE, CVSS 10.0. Sources: https://docs.n8n.io/security-audit and https://blog.canadianwebhosting.com/n8n-critical-cves-q1-2026-security-hardening/
- promptfoo documents well over 100 red-team plugins (the page gives no total) aimed at LLM and agent behaviour, not at servers, DNS or TLS. Source: https://www.promptfoo.dev/docs/red-team/llm-vulnerability-types/

## Targets that shaped it

- Gonya (live SaaS on a VPS with Supabase): a knowledge table had RLS turned off on purpose, found on 9 Nov 2026. That is the output example.
- The owner's mail host had no PTR record for the sending IP (Oct 2026), the reason DNS and email is its own layer.
- The full 104-check catalog lives in the companion security repo; this skill is the runner.

## AIC layer: code written by AI
- A study by the University of Texas at San Antonio, University of Oklahoma and Virginia Tech generated 576,000 code samples and found at least 5.2% of package references from commercial models and 21.7% from open-source models pointed to packages that do not exist, 205,474 unique names in all. Attackers can register such names ("slopsquatting"). Source: https://www.securityweek.com/ai-hallucinations-create-a-new-software-supply-chain-threat/
- A 2026 replication on five newer code models (199,845 Python and JavaScript prompts, checked against PyPI and npm) measured overall rates of 4.62% to 6.10%: a much narrower spread than the original, but the threat remains. Source: https://www.alphaxiv.org/abs/2605.17062 (preprint, not peer reviewed).
- What this means for the check: every dependency an AI added is looked up on its registry before install, to confirm it exists and is the intended package. The other AIC checks (hardcoded secrets, debug endpoints, swallowed errors) come from the secrets and error-handling layers above and are not backed by a separate study.
