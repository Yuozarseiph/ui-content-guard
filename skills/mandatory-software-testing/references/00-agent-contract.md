# 00 — Agent Contract & Testing Governance

**Applies to:** AI agents using this Skill to plan, execute, or report tests for the current repository. The Skill does not override human policy or grant permissions.  
**Normative language:** MUST / MUST NOT are mandatory; SHOULD is recommended; MAY is optional.  
**Authority:** This contract governs all files `01`–`16`. A test-specific file MUST NOT override this contract.

## 1. PRIME DIRECTIVE

- NEVER fabricate results, evidence, coverage, approvals, or participants.
- NEVER mark PASS without execution evidence in the same record.
- NEVER weaken, skip, delete, or rerun-to-green a valid test.
- NEVER change anything outside the changed scope without explicit human approval.
- If ambiguous or blocked: STOP, set Status=BLOCKED, report exactly what is missing.
- An AI agent CANNOT self-approve exceptions to a release gate.

## 2. Authorization boundary

### Allowed without asking
An agent MAY:
- Run tests using an already-authorized local or ephemeral test environment.
- Collect and summarize test evidence.
- Add or modify tests within the changed scope.
- Fix a defect within the changed scope when the fix is directly necessary for the assigned task and does not require a protected action.
- Create synthetic test data and clean up resources it created in its isolated test environment.

### Requires explicit human approval before acting
An agent MUST obtain approval before:
- Modifying production configuration, CI/CD pipelines, coverage thresholds, test framework configuration, or dependency lockfiles.
- Adding or removing dependencies, changing test frameworks, or changing build tooling.
- Deleting, disabling, quarantining, or skipping an existing test.
- Changing source code outside the assigned/changed scope.
- Touching any shared development, staging, or production environment.
- Running any test against production.
- Performing destructive, high-volume, active security, penetration, load, or stress testing outside an isolated environment.
- Recording a business, security, UX, or release exception.

If approval is absent, the agent MUST NOT act and MUST record `BLOCKED`, the exact approval required, the proposed action, and the approving role. An approval MUST be attributable to a human and recorded in the execution evidence.

## 3. Status decision table

| Status | Use only when |
|---|---|
| `NOT RUN` | Default state; execution has not started. |
| `PASS` | Every mandatory criterion for this test passed, the required prerequisites passed, and execution evidence is recorded in the same report. |
| `FAIL` | At least one mandatory criterion was violated by observed evidence. A NEW failure is always a failure. |
| `BLOCKED` | Execution cannot proceed because a dependency, environment, input, authorization, required artifact, or human action is missing. |
| `PARTIAL` | Some criteria were executed and passed, but other criteria remain unexecuted or blocked. This is not a pass and does not satisfy a release gate. |
| `NOT APPLICABLE` | The test is outside the documented product/release scope, with a written rationale and approval from the applicable human role defined in §11. Lack of access, time, tooling, or expertise is NOT a valid reason. |

An agent MUST NOT convert `FAIL`, `BLOCKED`, or `PARTIAL` into `PASS` by explanation alone. `SKIPPED` is a count in the execution report, not a status; skipped mandatory tests prevent a passing release gate.

## 4. Baseline and failure classification

Before evaluating a change, the agent MUST establish a baseline:
1. Prefer the last green run on the target branch using the same suite and materially equivalent environment.
2. If no last-green run exists, record the exact baseline limitation and use an approved prior report or a human-provided defect inventory. If no defensible baseline can be established, record `BLOCKED` for baseline-dependent conclusions.
3. Compare current failures with the baseline and classify each as `NEW` or `PRE-EXISTING`. Include the baseline run/report reference and defect ID where available.
4. `NEW` failures MUST block the relevant gate until fixed and retested or handled by a formally authorized release exception.
5. `PRE-EXISTING` failures MUST remain visible with baseline evidence and defect reference. Agents MUST NOT silently fix them, suppress them, or claim the suite is fully green. They do not become newly introduced failures merely because the current run observed them.
6. If classification cannot be supported by evidence, classify it as `UNCLASSIFIED` and set the affected result to `BLOCKED` or `PARTIAL`; do not guess.

## 5. Flaky-test policy

- A test that passes on a diagnostic rerun after failing is classified `FLAKY`; its execution status remains `FAIL` (not `PASS`) until the underlying issue is resolved and verified.
- A rerun MAY be performed only to diagnose nondeterminism, with a maximum of three total executions for that test in the diagnostic investigation.
- The original failure and every diagnostic result MUST be preserved.
- Repeated reruns intended to obtain a green build are prohibited and invalidate the result.
- A flaky mandatory test MUST be reported as unresolved and MUST NOT satisfy a release gate until its cause is addressed or an authorized human owner accepts the documented risk where policy permits.

## 6. Output contract

Every test execution report MUST use the following structure. The final response for a test execution MUST contain exactly these three top-level sections, with no process narration:

### 6.1 Completed Execution Record

| Field | Value |
|---|---|
| Test / status | |
| Build / commit SHA | |
| Environment | |
| Tool + version | |
| Executed by | |
| Start–end (timezone) | |
| Passed / failed / blocked / skipped / N/A counts | |
| Baseline reference | |
| NEW / PRE-EXISTING / UNCLASSIFIED failures | |
| Scope covered | |
| Scope NOT covered | |
| Evidence location | |
| Defect IDs | |
| Reviewer / approval | |

Unknown values MUST be written as `unknown`; the residual-risk section MUST explain why. Evidence MUST be referenced from this record or its linked report. Do not create a second, conflicting evidence table.

### 6.2 Defect list

Use a table with: `Defect ID | NEW/PRE-EXISTING/UNCLASSIFIED | Severity | Description | Owner role | Remediation | Retest status | Evidence`. If there are no defects, write `None observed` and state the tested scope.

### 6.3 Residual risk

Write one paragraph identifying untested scope, assumptions, unknown fields, environment differences, pre-existing failures, flaky tests, blocked work, and accepted risks. Do not claim risk is absent merely because no defect was observed.

The final answer MUST contain exactly these three sections. Test-specific files MUST NOT define a competing output format.

## 7. Where to read project instructions

Before execution, inspect these sources in order and record which were found:
1. `README.md` (and relevant nested README files).
2. `CONTRIBUTING.md`.
3. `docs/testing/`, `docs/testing*`, and test-specific documentation.
4. `Makefile` and task runner configuration.
5. `package.json` scripts, if present.
6. `pyproject.toml`, `pytest.ini`, `tox.ini`, `vitest.config.*`, `jest.config.*`, and equivalent framework configuration.
7. `CODEOWNERS`.

The agent MUST use the repository's documented commands and conventions. If no test instructions or command are present, it MUST identify the project language/framework, use a standard non-destructive test command only when unambiguous, and state the assumption in residual risk. If the command or environment is ambiguous, set `BLOCKED` and ask for the missing decision.

## 8. Test data, privacy, and PII

- Agents MUST NOT use production customer data, personal data (PII), credentials, tokens, or secrets in tests unless a documented legal/security approval explicitly authorizes a controlled use.
- Use synthetic data or approved-anonymized data. Anonymization MUST be validated; merely masking visible fields is insufficient.
- Evidence MUST redact secrets, tokens, personal data, and sensitive payloads before storage or sharing.
- Participant-based tests (including usability, alpha, and beta) MUST have informed consent, a stated purpose, participant eligibility criteria, a data minimization plan, access controls, and a retention/deletion policy before collection.
- Test data MUST be isolated from real customer records and MUST be cleaned up according to the environment's retention policy.

## 9. Test dependency matrix

| Test | Required prerequisite |
|---|---|
| Integration | Relevant Unit tests `PASS` |
| System | Relevant Integration tests `PASS` |
| End-to-End | Smoke `PASS` on the candidate environment |
| Acceptance | System and critical E2E `PASS` |
| Beta | Alpha exit criteria `PASS` and approved |

These are minimum dependencies. Each test file may define additional prerequisites. A prerequisite that is missing or not green MUST result in `BLOCKED` or `PARTIAL`, never `PASS`. Independent tests MAY run in parallel when doing so does not violate dependencies or contaminate test data.

## 10. Executability labels

| Label | Meaning |
|---|---|
| `AI-EXECUTABLE` | An authorized agent can normally execute the checks using repository tooling and isolated environments. Human approval is still required for protected actions. |
| `AI-ASSISTED` | The agent can prepare, orchestrate, execute approved tool-based portions, analyze results, and document evidence; human oversight or specialized infrastructure is required for meaningful completion. |
| `HUMAN-ONLY` | The required judgment, participation, or sign-off must come from a human. AI MAY prepare materials and organize evidence but MUST NOT impersonate participants or signatories. |

Default classification:
- `AI-EXECUTABLE`: Unit, Integration, Smoke, Sanity, Regression, Compatibility.
- `AI-ASSISTED`: System, End-to-End, Performance, Load, Stress, Security, Exploratory.
- `HUMAN-ONLY`: Acceptance, Usability, Alpha/Beta.

A project may impose stricter controls. A label does not grant authorization.

## 11. Governance roles

These are role names, not assumed people. The repository/project MUST map each role to an identifiable human (name or team and contact/channel) before a gate requiring that role is evaluated.

| Role | Responsibility |
|---|---|
| `release_owner` | Human accountable for release readiness, release-gate exceptions where policy permits, and final go/no-go decision. |
| `security_owner` | Human accountable for security test scope authorization, security finding disposition, and security-risk acceptance. |
| `product_owner` | Human accountable for product requirements, business acceptance criteria, acceptance delegation, and business-risk decisions. |
| `ux_owner` | Human accountable for UX research protocol, participant criteria, consent, and usability finding disposition. |
| `human_owner` | Human accountable for approving `NOT APPLICABLE` decisions and other human approvals not assigned to a more specific role. |

`authorized_delegate` for acceptance MUST be explicitly named or mapped by `product_owner` before acceptance begins. An AI agent MUST NOT act as any of these roles. If the applicable role is not mapped, the relevant approval or N/A decision is `BLOCKED`.

## 12. Repository-level release decision

The release report MUST conclude `READY FOR RELEASE` or `NO-GO`.
- `NO-GO` is required if any applicable mandatory gate is `NOT RUN`, `FAIL`, `BLOCKED`, or `PARTIAL`; if any NEW critical/high defect remains open; or if required human approvals are absent.
- `READY FOR RELEASE` is allowed only when all applicable mandatory gates pass, required evidence exists, and required human sign-offs are recorded.
- Only `release_owner` may make the final production release decision. An AI agent MUST report evidence and recommendation, not authorize production release.
