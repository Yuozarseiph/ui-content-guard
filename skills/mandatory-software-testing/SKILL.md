---
name: mandatory-software-testing
description: Plan, run, and report evidence-backed software QA and release-readiness checks for code, configuration, dependency, or deployment changes. Use when implementing or reviewing software changes, debugging failing tests, evaluating a release candidate, or requesting unit, integration, system, end-to-end, acceptance, smoke, sanity, regression, performance, load, stress, security, usability, compatibility, exploratory, alpha, or beta testing. Does not authorize production or destructive actions.
---

# Mandatory Software Testing Skill

## Mission

Act as the project's QA execution and release-readiness coordinator. Select the applicable test types, inspect repository instructions, establish a baseline, execute only authorized checks, preserve evidence, classify findings, and report a defensible result.

This Skill is a governance layer, not permission to access systems or perform destructive actions. Repository policy, tool permissions, and explicit human authorization remain controlling.

## Mandatory first read

Before executing or reporting any test, read:

1. [Central testing contract](references/00-agent-contract.md) — authoritative authorization, statuses, baseline, flaky policy, output contract, privacy, dependencies, and human roles.
2. Relevant [test-specific references](#reference-map) for the requested scope, and the [dependency matrix](references/TEST-DEPENDENCY-MATRIX.md) when planning multiple test layers.
3. Repository instructions, following [the contract discovery order](references/00-agent-contract.md) §7.

If a required reference is unavailable or contradictory, stop and report `BLOCKED`. Do not invent missing policy.

## Activation and scope

Activate this Skill when:
- A code, configuration, schema, infrastructure, or dependency change is proposed or completed.
- A user asks to test, verify, validate, debug, audit, or assess release readiness.
- A build, deployment, or release candidate needs a QA decision.
- A test failure, flaky result, regression, or security finding needs triage.

First determine the requested scope:
- **Focused change:** test changed files and direct callers; add relevant regression coverage.
- **Feature or integration change:** include all impacted test layers and their prerequisites.
- **Release candidate / pre-launch:** evaluate every applicable mandatory gate in the dependency matrix.
- **Single named test:** perform that test and its prerequisites; do not imply that other test types passed.
- **Advisory-only request:** explain or plan tests without claiming execution.

Never silently expand a focused task into unrelated source-code changes or production actions.

## Operating procedure

### 1. Establish repository context

1. Identify repository root, branch, commit SHA, working-tree state, changed files, and requested target.
2. Read project instructions in the order defined in `00-agent-contract.md` §7.
3. Identify language, framework, package manager, test runner, scripts, CI conventions, and test directories.
4. Record the commands and tools actually available. Do not assume a command, dependency, service, credential, or environment exists.
5. Map required governance roles to identifiable human owners when a decision requires them. If a required role is unmapped, the relevant approval is `BLOCKED`.

### 2. Build the test plan

1. Identify the change type, risk, affected components, public interfaces, data boundaries, user journeys, and operational dependencies.
2. Select applicable test types using the reference documents and `references/TEST-DEPENDENCY-MATRIX.md`.
3. Build a dependency-aware plan. At minimum:
   - Integration requires relevant Unit tests `PASS`.
   - System requires relevant Integration tests `PASS`.
   - E2E requires Smoke `PASS` on the candidate environment.
   - Acceptance requires System and critical E2E `PASS`.
   - Beta requires Alpha exit criteria `PASS` and human approval.
4. Distinguish mandatory, conditional, and genuinely not-applicable tests. `NOT APPLICABLE` requires written scope rationale and approval from the mapped human role.
5. Identify required artifacts before execution: requirements, journey inventory, support matrix, workload forecast, security scope authorization, acceptance criteria, exploratory charter, or participant protocol as applicable.
6. Present the plan before taking any action that requires approval.

### 3. Establish baseline

1. Use the last green run on the target branch for the relevant suite, where available.
2. Record the baseline run/report reference and previously fixed defect IDs.
3. Compare current results against the baseline.
4. Classify every failure as `NEW`, `PRE-EXISTING`, or `UNCLASSIFIED`, with evidence.
5. A `NEW` failure blocks the affected gate. A `PRE-EXISTING` failure remains visible and linked to its baseline/defect; never silently fix or suppress it.
6. If classification cannot be evidenced, use `BLOCKED` or `PARTIAL`, not a guess.

### 4. Check authorization before execution

Run only checks permitted by the central contract and available tool permissions.

Obtain explicit human approval before:
- Modifying production configuration, CI/CD, test framework configuration, coverage thresholds, lockfiles, or dependencies.
- Deleting, disabling, skipping, or quarantining tests.
- Changing source outside the assigned/changed scope.
- Touching shared development, staging, or production environments.
- Running tests against production.
- Running active security scans, penetration tests, destructive tests, or high-volume load/stress tests without the required written scope and safety approval.
- Recording acceptance, UX, security, or release exceptions.

If approval is missing, do not perform the action. Record `BLOCKED`, the exact missing approval, the proposed action, and the required approving role.

### 5. Execute in dependency order

1. Start with the lowest relevant test layer and proceed only when prerequisites pass.
2. Use project-defined commands and isolated test environments.
3. Use synthetic or approved-anonymized data only. Never expose secrets or PII in logs or evidence.
4. Preserve raw tool output, exit codes, test reports, timestamps, environment details, and commit SHA.
5. Do not alter tests or thresholds merely to make a build green.
6. Do not claim that a test ran unless a tool actually executed it and returned evidence.
7. For `AI-ASSISTED` tests, coordinate only the approved tool-executable portion and clearly identify human/specialist work still required.
8. For `HUMAN-ONLY` tests, prepare protocol and evidence collection; do not impersonate participants, stakeholders, or approvers.

### 6. Handle failures and flaky tests

1. Preserve the original failure.
2. A rerun is allowed only to diagnose possible flakiness, with no more than three total executions for that test during the diagnostic investigation.
3. A test that fails and then passes on rerun is classified `FLAKY`; its execution status is `FAIL`, not `PASS`.
4. Never rerun repeatedly to obtain a green result.
5. Record reproducible steps, expected/actual behavior, severity, owner role, defect ID, remediation, and retest status.
6. Stop deeper post-deployment testing after a Smoke failure and follow the approved rollback runbook. If rollback needs human approval, stop and escalate.
7. Stop immediately when a security scope boundary, stress-test stop condition, data-safety rule, or authorization boundary is reached.

### 7. Determine status

Use only the status definitions in the [central contract](references/00-agent-contract.md) §3:

- `NOT RUN`
- `PASS`
- `FAIL`
- `BLOCKED`
- `PARTIAL`
- `NOT APPLICABLE`

`PASS` requires every mandatory criterion to be met and execution evidence in the same record. Missing evidence, unknown environment, missing prerequisites, or absent approvals cannot be interpreted as success.

### 8. Release decision

For a release-readiness request, evaluate all applicable mandatory gates. Any applicable mandatory gate that is `NOT RUN`, `FAIL`, `BLOCKED`, or `PARTIAL` means `NO-GO`. Open NEW critical/high defects and missing human approvals also mean `NO-GO`.

Only the mapped human `release_owner` can make the final production release decision. The Skill reports evidence and a recommendation; it never authorizes release.

## Required final response format

For every test execution, follow the [central contract](references/00-agent-contract.md) §6 exactly. The final response MUST contain exactly these three top-level sections:

1. **Completed Execution Record** — use the unified field table from the contract.
2. **Defect list** — include IDs, NEW/PRE-EXISTING classification, severity, owner role, remediation, retest status, and evidence. If none, state `None observed`.
3. **Residual risk** — one paragraph covering untested scope, assumptions, unknown fields, environment differences, pre-existing failures, flaky tests, blocked work, and accepted risks.

Do not add process narration, unsupported confidence claims, or a separate competing evidence format. Unknown values must be `unknown` and explained in residual risk.

## Reference map

Load only the test-specific references relevant to the current scope, in addition to the mandatory central contract.

| Reference | Test |
|---|---|
| [references/01-unit-testing.md](references/01-unit-testing.md) | Unit |
| [references/02-integration-testing.md](references/02-integration-testing.md) | Integration |
| [references/03-system-testing.md](references/03-system-testing.md) | System |
| [references/04-end-to-end-testing.md](references/04-end-to-end-testing.md) | End-to-End |
| [references/05-acceptance-testing.md](references/05-acceptance-testing.md) | Acceptance |
| [references/06-smoke-testing.md](references/06-smoke-testing.md) | Smoke |
| [references/07-sanity-testing.md](references/07-sanity-testing.md) | Sanity |
| [references/08-regression-testing.md](references/08-regression-testing.md) | Regression |
| [references/09-performance-testing.md](references/09-performance-testing.md) | Performance |
| [references/10-load-testing.md](references/10-load-testing.md) | Load |
| [references/11-stress-testing.md](references/11-stress-testing.md) | Stress |
| [references/12-security-testing.md](references/12-security-testing.md) | Security |
| [references/13-usability-testing.md](references/13-usability-testing.md) | Usability |
| [references/14-compatibility-testing.md](references/14-compatibility-testing.md) | Compatibility |
| [references/15-exploratory-testing.md](references/15-exploratory-testing.md) | Exploratory |
| [references/16-alpha-beta-testing.md](references/16-alpha-beta-testing.md) | Alpha/Beta |
| [references/TEST-DEPENDENCY-MATRIX.md](references/TEST-DEPENDENCY-MATRIX.md) | Test dependencies and lifecycle |

## Non-negotiable constraints

- Never fabricate execution, evidence, coverage, approvals, or participants.
- Never mark `PASS` without same-record execution evidence.
- Never weaken, delete, disable, skip, or rerun-to-green a valid test.
- Never act outside authorization or changed scope.
- Never use production customer data, secrets, or unapproved PII.
- Never self-approve exceptions, acceptance, security risk, or release.
- When blocked or ambiguous, stop and state exactly what is missing.
