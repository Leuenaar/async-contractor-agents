---
name: security-reviewer
description: Runs a layered security checklist against one project built with AI (secrets and repo, DNS and email, web headers, VPS, n8n, Supabase, chatbot and LLM risks, agent permissions, operational resilience, privacy basics, WordPress, third-party tokens) and returns pass, fail or not applicable per check with evidence and a fix. Use before a client handover, before making a repo public, or after a platform security advisory.
license: MIT
metadata:
  author: Harva Heru
  version: "0.1.0"
  shared: "evidence-rule,human-gate"
---

# Security reviewer

**Core rule:** a check passes only with evidence from this run: a scan output, a screenshot, a config value. "Probably fine" is a fail.

## Input

- The project: repos, domains, hosting, platforms used.
- Read access to the relevant dashboards, or the owner running commands and sharing output.

## Layers

| Layer | Example checks |
| --- | --- |
| SEC secrets and repo | No keys in git history (gitleaks or trufflehog); secret scanning and push protection on; leaked keys rotated at the provider |
| DNS and email | SPF valid, DKIM on, DMARC at quarantine or stricter, PTR matches the sending host, no dangling records |
| WEB | HTTPS forced, TLS 1.2+, HSTS, CSP present, secure cookies, CORS not `*` with credentials |
| VPS | SSH keys only, root login off, only needed ports open, auto security updates, backups restored at least once |
| N8N | Version patched against current n8n security advisories (including the Q1 2026 critical CVEs), `n8n audit` run, editor not public, webhooks authenticated, execution data pruned, error workflow on every production flow |
| SUPA | Security advisor clean, RLS on every public table with real policies, service role key never in frontend, anon-key read of another user's row fails |
| LLM | Injection, system prompt leak, PII leak, invented prices and policies, output cannot inject HTML, cost caps and rate limits |
| AGT | Tool allowlist, human approval on irreversible actions, least-privilege credentials, pinned third-party tools |
| AIC AI-generated code | Every dependency exists and is the intended package (no hallucinated or look-alike names), no hardcoded secrets, no leftover debug endpoints, no swallowed errors |
| OPS | Provider outage, dead keys, floods, silent stop detection (see `break-tester`) |
| PRIV | Users told they are talking to AI, retention limit, data map, client's country rules noted for the client to check |
| WP, TOK | WordPress core and plugins updated, xmlrpc off, 2FA; third-party tokens stored in credential stores and rotated |

## Steps

1. List the project's layers. Mark layers that do not apply.
2. Run each check with the cheapest real method. Save the evidence.
3. Mark pass, fail or not applicable. Unknown counts as fail until checked.
4. For each fail, write the fix and its severity (critical, high, medium, low).
5. Report critical fails first.

## Rules

- Read and scan only. Changing settings, rotating keys and deleting data are the owner's actions ([human-gate](references/human-gate.md), tier 3).
- Never paste secrets into the report. Show the last 4 characters at most.
- Evidence per check ([evidence-rule](references/evidence-rule.md)).
- PRIV checks are readiness notes, not legal advice.

## Done when

- [ ] Every applicable layer checked.
- [ ] Every check has evidence or is marked fail.
- [ ] Every fail has a fix and severity.

## Output

```
| ID | Check | Result | Evidence | Fix | Severity |
| SUPA-02 | RLS on all public tables | Fail | advisor: rls_disabled_in_public on knowledge | enable RLS + owner-only policy | Critical |
```

## Not this skill's job

Failure-mode testing of workflows (`break-tester`). Conversation attacks in depth (`chatbot-red-teamer`).

Research behind this skill: [references/research.md](references/research.md).
