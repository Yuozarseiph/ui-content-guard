# Stress Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Discover system limits and verify safe degradation and recovery when load or dependency pressure exceeds expected operating conditions.

## 2. Prerequisites
Approved stress-test plan, isolated environment, stop conditions, monitoring, and recovery procedure are required. Production is prohibited by default.

## 3. When required
Before launch for critical/high-availability systems; after major architecture/scaling changes; periodically where resilience policy requires.

## 4. Procedure
1. Define the objective, maximum authorized load, stop conditions, safety owner, and recovery plan.
2. Default target MUST be an isolated non-production environment. NEVER run stress tests in production by default.
3. Increase load in controlled steps beyond expected peak while monitoring saturation, error modes, queues, dependencies, and data integrity.
4. Verify graceful degradation, rate limiting, backpressure, circuit breakers, and user-facing failure behavior where applicable.
5. Reduce load and verify recovery, backlog drainage, and return to healthy state.
6. Preserve metrics, logs, exact workload profile, and recovery duration.
7. Any proposed production stress test requires prior written approval recorded in the run from the mapped `release_owner` and `security_owner`, plus a documented maintenance window and rollback/stop plan.

## 5. Pass criteria
- [ ] Test ran only in an authorized environment.
- [ ] System degraded or failed according to documented safe limits.
- [ ] No unrecoverable data loss or corruption occurred.
- [ ] Recovery and backlog drainage completed within approved objectives.
- [ ] All stop conditions, approvals, and metrics are recorded.

## 6. Release gate
Unsafe conditions or failure to recover blocks the test and may block launch for critical systems. Production stress without the specified written role approvals MUST NOT occur.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Production stress is NEVER the default. Approval must be attributable to the named human roles in `00-agent-contract.md` §11.
- The agent MUST stop immediately if safety thresholds or stop conditions are reached.
- No unapproved shared-environment load generation is permitted.

## 9. Execution record
See `00-agent-contract.md` §6.
