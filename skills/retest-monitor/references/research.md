# Research notes: retest-monitor

## Findings used

- Chen, Zaharia and Zou, "How is ChatGPT's behavior changing over time?" (2023): GPT-4's accuracy on prime number identification fell from 84% in March 2023 to 51% in June 2023; both GPT-3.5 and GPT-4 made more code formatting mistakes in June; instruction following declined. The same hosted model can shift a lot in months, so continuous monitoring is needed. Source: https://arxiv.org/abs/2307.09009
- promptfoo recommends running red-team suites in CI/CD to catch regressions, re-running the suite to verify fixes, and keeping the test suite updated; it names no specific tracking tool. Source: https://www.promptfoo.dev/docs/red-team/
- n8n had six critical CVEs in Q1 2026, including an unauthenticated RCE (CVE-2026-21858); platform security releases are a retest trigger. Source: https://blog.canadianwebhosting.com/n8n-critical-cves-q1-2026-security-hardening/

## Targets that shaped it

- Cekura, a chatbot and voice-agent testing tool, prices continuous testing at $500 per month or $0.25 per test minute, a reference point for what automated retesting costs. Source: https://www.cekura.ai/pricing
- FirstTouch's final v6 regression run was never done (Nov 2026): the reason a retest is a required step, not an extra.
