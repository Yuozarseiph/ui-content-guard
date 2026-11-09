# End-to-End (E2E) Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Validate complete user journeys through the actual user-facing entry points and connected services, including final persisted outcomes.

## 2. Prerequisites
Smoke MUST be PASS on the candidate environment. Critical journeys MUST be sourced from approved requirements or analytics-derived real-user paths. Follow baseline and flaky policies in `00-agent-contract.md`.

## 3. When required
For every release candidate; rerun impacted journeys after UI, API, authentication, payment, permission, or workflow changes.

## 4. Procedure
1. Load the approved journey inventory from requirements and/or analytics. Store executable journey definitions in `e2e/journeys.yaml` or the repository's documented equivalent.
2. MUST identify the requirement/analytics source and owner for each critical journey.
3. Execute each journey through the actual supported user interface or public API boundary; do not replace the full journey with isolated mocks.
4. Cover success, validation, permission, cancellation, interruption, and recovery paths where relevant.
5. MUST use isolated synthetic test accounts/data; MUST clean up created records and external test resources.
6. Assert both user-visible outcomes and durable backend effects, such as persisted records or emitted events.
7. Record browser/device, build, environment, journey ID, and evidence.

## 5. Pass criteria
- [ ] Smoke is PASS for the candidate environment.
- [ ] Every designated critical journey has a source reference and execution result.
- [ ] UI-visible result and backend durable state agree.
- [ ] Test data is isolated and cleanup is completed or documented.
- [ ] No NEW failure blocks a critical user journey.

## 6. Release gate
A failed critical journey blocks launch. Missing journey source, missing Smoke prerequisite, or unavailable safe test accounts is BLOCKED/PARTIAL, never PASS.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Journey source MUST be approved requirements or analytics; agents MUST NOT invent critical journeys.
- `e2e/journeys.yaml` is the default location. If the repository uses another location, record the actual path.
- E2E tests MUST not use production customer accounts or real payment/notification side effects.

## 9. Execution record
See `00-agent-contract.md` §6.
