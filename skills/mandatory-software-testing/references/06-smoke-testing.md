# Smoke Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Perform a short set of broad health checks to determine whether a build or deployment is stable enough for deeper testing.

## 2. Prerequisites
A built artifact and authorized isolated target environment are required. For E2E execution, Smoke MUST pass first. Deployment runbook and rollback procedure MUST be available for post-deployment checks.

## 3. When required
Immediately after each candidate build and after every deployment, including production deployment only where explicitly authorized.

## 4. Procedure
1. Verify artifact identity, application startup, health/readiness endpoints, and essential service connectivity.
2. Check one representative authentication path and one critical workflow using synthetic test data.
3. Verify key pages/API routes and essential database/queue connectivity.
4. Inspect startup/deployment logs and health indicators for immediate errors.
5. Record checks, environment, build, and evidence.
6. If post-deployment Smoke FAILs, STOP deeper testing and trigger rollback according to the approved runbook; if rollback requires human authorization, set BLOCKED and escalate immediately.

## 5. Pass criteria
- [ ] Application starts and required health/readiness checks return expected status.
- [ ] Essential dependencies are reachable.
- [ ] Representative critical workflow completes.
- [ ] No deployment-blocking startup/configuration error is observed.

## 6. Release gate
Smoke failure stops promotion. Post-deployment Smoke failure triggers rollback per runbook; deeper tests MUST NOT proceed until the deployment is restored or explicitly stabilized by the responsible human.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Smoke tests MUST be short and deterministic; they do not establish full functional correctness.
- Rollback MUST follow the repository/service runbook. The agent MUST NOT invent rollback commands or bypass required approval.
- Smoke PASS does not replace System, E2E, Security, or Regression testing.

## 9. Execution record
See `00-agent-contract.md` §6.
