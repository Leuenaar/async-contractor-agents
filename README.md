# async-contractor-agents

Claude skills for doing AI automation work async and in writing: finding work that fits, scoping it, building it with AI doing one narrow job, breaking it on purpose before it ships, and proving every claim with evidence.

I'm Harva Heru. I build automations and chatbots by directing AI rather than writing code by hand, I work from Indonesia (UTC+7), and I work in writing rather than on calls. These skills are how I run that work. They are early: most were written from research and from tests on my own demo projects, not yet from paid client jobs. The status table below says which is which.

## How it works

It starts with a market, not a company. `segment-scout` scores a few segments on whether they can pay, whether my proof matches their problem, and whether I can reach them without a call. Only then does it name companies, each with one detail I checked myself, like a test enquiry that took two days to answer.

When there's a job to apply for, `job-screener` throws out anything with a live interview, required hand-written code or experience I don't have, and checks I haven't already applied. `upwork-proposal` opens with the closest thing I've built and answers the client's own test cases.

Once a job is won, `scope-writer` turns the brief into deliverables that each have a pass condition, and `build-director` writes the spec a coding model builds from. The rule there: AI makes one decision per step, from a fixed list of answers. Prices and rules stay in plain code. When the AI isn't sure, a person takes over.

Then `break-tester` breaks it. Email provider down, every API key dead, twenty leads in a minute, a duplicate submission. Each result goes in a Break Report with a run ID. The first version of my own lead flow failed one of these: a CRM error stopped the owner alert from going out. That's why alerts now run before the CRM write, and why the report leads with the worst failure found, even after it's fixed.

Nothing leaves without a person saying yes. Skills draft emails, proposals and posts; I send them.

## Skills

| Group | Skill | What it does |
| --- | --- | --- |
| Finding work | `segment-scout` | Scores segments before companies, with sources |
| | `job-screener` | Filters listings against the async-only rule and past applications |
| | `upwork-proposal` | One proposal per job, opening with matching proof |
| | `form-filler` | Application forms, one copy-ready block per box |
| | `outreach-drafter` | One cold email per company, under 100 words, saved as a draft |
| | `tracker-keeper` | Keeps the application tracker filled from Gmail |
| Delivery | `scope-writer` | Brief to testable deliverables, out-of-scope list, fixed price |
| | `build-director` | Build spec: one AI decision per step, rules in code, handoff to a person |
| | `break-tester` | Deliberate failure tests and the Break Report |
| | `chatbot-red-teamer` | About 50 adversarial conversations, severity-ranked |
| | `handover-writer` | Runbook a non-technical team can follow |
| | `retest-monitor` | Reruns the suite after model, prompt or platform changes |
| Proof | `case-study-writer` | Case study from logs, with demo work labelled as demo |
| | `break-log-writer` | Weekly post about one real failure, no sales pitch |
| | `demo-storyboarder` | Silent demo video plan that works on mute |
| Quality gates | `humanizer` | Removes AI writing patterns, keeps every fact |
| | `devils-advocate` | Premortem: assume it failed, find why |
| | `evidence-auditor` | Every claim checked against proof |
| | `fact-checker` | Outside facts traced to their original source |
| Strategy | `market-demand` | What buyers pay for now, ranked by evidence strength |
| | `competitor-map` | Where the crowd stands and where nobody does |
| | `buyer-psychology` | Buyer fears mapped to proof, gaps named |
| | `constraint-strategist` | Work models where each constraint matters least |
| Security | `security-reviewer` | Layered checks from secrets to chatbot behaviour |

Every skill has a `references/research.md` with the sources and real cases it was built from.

## Rules every skill follows

Four files in [`shared/`](shared/) hold the rules. A script copies the ones each skill needs into that skill's `references/` folder, so every skill works on its own when uploaded.

- [anti-slop](shared/anti-slop.md): no em dashes, no "not X but Y", no cliche vocabulary, no chatbot openers. Specific numbers and plain verbs.
- [strict-selection](shared/strict-selection.md): written assessments, portfolio reviews, paid trials and written interviews pass. Live interviews fail.
- [evidence-rule](shared/evidence-rule.md): every claim points to proof, and the wording matches the proof.
- [human-gate](shared/human-gate.md): sending, submitting, posting, paying and deleting wait for a person.

## Status

| Skill | Status |
| --- | --- |
| `break-tester` | Method used by hand on the FirstTouch demo (failure tests run by hand, Oct 2026). Not yet run as a skill. |
| `build-director` | Design used in the Frontdesk demo (AI picks the job type, code computes the price). Not yet run as a skill. |
| `job-screener`, `upwork-proposal`, `form-filler` | Rules taken from real screenings and applications in Nov 2026. Not yet run as skills. |
| All others | Written from research. Not yet run. |

When a skill is run on a real job, its row will say what it was run on and link the result.

## Install

**claude.ai:** download a skill's zip from the latest workflow run (Actions > skills > skill-zips), then Customize > Skills > Upload a skill. Code execution must be on. Or run `python scripts/build_zips.py` and upload from `dist/`.

**Claude Code:**

```
/plugin marketplace add Leuenaar/async-contractor-agents
/plugin install async-contractor-skills@async-contractor-agents
```

**By hand:** copy a folder from `skills/` into `~/.claude/skills/`.

## Editing the rules

Edit a file in `shared/` or `templates/`, then run:

```
python scripts/sync_shared.py
python scripts/validate.py
```

The workflow runs both on every push and fails if a copy is out of date.

## What this is not

Not coding agents. Claude already writes the code; these skills decide what gets built, check it, and write about it honestly. Not a guarantee of anything: they reduce mistakes, they don't remove them.

## License

MIT. See [LICENSE](LICENSE).
