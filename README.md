# Mandatory Software Testing — Agent Skill

An evidence-first, policy-aware software QA skill for AI coding agents. Written in the open [Agent Skills](https://agentskills.io/specification) format for use with agent platforms that support `SKILL.md`, including OpenAI Codex and GitHub Copilot.

This repository **distributes one skill** at [`skills/mandatory-software-testing/`](skills/mandatory-software-testing/). It does **not** provide a test framework, run tests by itself, grant access to services, or override authorization requirements.

## What it covers

- **16 testing categories**: Unit, Integration, System, End-to-End, Acceptance, Smoke, Sanity, Regression, Performance, Load, Stress, Security, Usability, Compatibility, Exploratory, and Alpha/Beta.
- **Evidence-backed decisions**: preserve real command outputs, exit codes, environment context, baselines, and defect records.
- **Test dependencies**: enforce prerequisites and separate release readiness from an individual test result.
- **Safety and governance**: obtain explicit permission before protected or destructive operations; require human approval for release decisions.
- **Flaky handling**: diagnose reruns without converting failed runs into a false pass.

## Install from GitHub

Replace `YOUR_USERNAME` with the GitHub account or organization that owns the repository. The GitHub CLI skill subcommands are in preview and require a recent version of [`gh`](https://cli.github.com/manual/gh_skill).

**OpenAI Codex — current project:**

```bash
gh skill install YOUR_USERNAME/mandatory-software-testing mandatory-software-testing --agent codex --scope project
```

**GitHub Copilot — current project:**

```bash
gh skill install YOUR_USERNAME/mandatory-software-testing mandatory-software-testing --agent github-copilot --scope project
```

**Install for your user account** (change `--agent` as needed):

```bash
gh skill install YOUR_USERNAME/mandatory-software-testing mandatory-software-testing --agent codex --scope user
```

If `gh skill` is not available, install manually by copying the **entire** [`skills/mandatory-software-testing/`](skills/mandatory-software-testing/) directory, preserving its name and contents:

| Agent | Project directory | User directory |
| --- | --- | --- |
| OpenAI Codex | `.agents/skills/mandatory-software-testing/` | `~/.agents/skills/mandatory-software-testing/` |
| GitHub Copilot | `.github/skills/mandatory-software-testing/` (or `.agents/skills/`) | `~/.copilot/skills/mandatory-software-testing/` |

The installed `SKILL.md` should be found directly inside the named skill folder. Restart or refresh the agent if the new skill is not shown.

## Use

You can explicitly ask your agent to use `mandatory-software-testing` to check a change, run relevant authorized tests, assess a failed test, or prepare a release-readiness report. In Codex, `$mandatory-software-testing` is an explicit invocation form.

**Sample requests**

- `Use $mandatory-software-testing to test this PR, with actual evidence and remaining risks.`
- `Assess release readiness using mandatory-software-testing; do not touch production.`
- `Investigate failing integration tests with the skill's baseline and flaky policies.`

An Agent Skill is loaded when supported and selected. **Installing a skill does not enforce its use on every commit.** To enforce testing in your organization, add repository policy and CI checks separately.

## Layout

```text
mandatory-software-testing/           # GitHub repository root
├── README.md
├── README.fa.md
├── .gitignore
├── .github/workflows/validate-skill.yml
├── tools/validate_skill.py
└── skills/
    └── mandatory-software-testing/
        ├── SKILL.md                 # Skill entry point
        ├── README.md
        ├── agents/openai.yaml        # Optional agent interface metadata
        └── references/
            ├── 00-agent-contract.md
            ├── 01-unit-testing.md ... 16-alpha-beta-testing.md
            └── TEST-DEPENDENCY-MATRIX.md
```

## Validate changes

```bash
python -m pip install 'PyYAML>=6,<7'
python tools/validate_skill.py
```

GitHub Actions runs the same structural validation for pull requests and pushes. Structural validation checks format, required metadata, local reference links, and expected documents; **it cannot prove that an agent executed the testing workflow correctly**.

## Publishing and permissions

Publish the **extracted files**, not the ZIP itself, at the root of a GitHub repository named `mandatory-software-testing` (or update the commands above if you choose another name). Before making this publicly reusable, choose and add a `LICENSE` file with the permissions you intend to grant. No license has been selected on your behalf.

## References

- [Agent Skills specification](https://agentskills.io/specification)
- [GitHub: add agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills)
- [GitHub CLI: install skills](https://cli.github.com/manual/gh_skill_install)
- [Codex: build skills](https://learn.chatgpt.com/docs/build-skills)
