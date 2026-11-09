# System Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Validate the fully integrated application as a complete system against documented functional and non-functional requirements in a release-like environment.

## 2. Prerequisites
Relevant Integration tests MUST be PASS. A release candidate, system requirements, deployment instructions, and environment-parity checklist MUST be available.

## 3. When required
On each release candidate after staging deployment; after material architecture, infrastructure, or configuration changes.

## 4. Procedure
1. Identify the release candidate, system requirements, and target deployment topology.
2. MUST verify environment parity and record differences: operating system/runtime, database version, queue/broker version, configuration shape, network topology, identity provider, and relevant external service versions.
3. Deploy the complete candidate using the approved release procedure; do not modify shared/staging systems without approval.
4. Map each applicable requirement to one or more system scenarios.
5. Verify user roles, permissions, persistence, background jobs, service health, startup/shutdown, logging, and recovery as applicable.
6. Execute the scenarios in the production-like environment and preserve build/environment identifiers.
7. Escalate unresolved critical/high defects to `release_owner`.

## 5. Pass criteria
- [ ] Relevant Integration tests are PASS.
- [ ] Every in-scope system requirement has a recorded result and evidence.
- [ ] Environment parity checklist is complete; every difference has an impact assessment.
- [ ] Critical workflows and required operational checks pass.
- [ ] No unresolved NEW critical/high defect remains.

## 6. Release gate
System testing is a mandatory pre-launch gate. Any unmet mandatory requirement or unverified critical environment difference is FAIL or BLOCKED and results in NO-GO. `release_owner` owns the release decision.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- `release_owner` is the human role defined in `00-agent-contract.md` §11; the role MUST be mapped before release evaluation.
- Environment parity means matching versions and configuration shape where required by the architecture; differences MUST be explicit, not assumed harmless.

## 9. Execution record
See `00-agent-contract.md` §6.
