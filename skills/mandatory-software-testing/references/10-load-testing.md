# Load Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Verify system behavior at expected and forecasted normal/peak traffic levels, including capacity and steady-state behavior.

## 2. Prerequisites
Expected/peak workload and forecast source MUST be named and linked (for example, analytics report or product-management capacity plan). If no source exists, BLOCKED. Isolated load-test environment and approved objectives are required.

## 3. When required
Before launch when concurrent usage/capacity matters; after infrastructure, scaling, or traffic-pattern changes.

## 4. Procedure
1. Obtain expected average, peak, and forecast growth traffic from a named source and link the source artifact.
2. If the forecast source is absent or not approved, STOP and set BLOCKED; do not substitute an agent-generated guess.
3. Define user journeys, request mix, data shape, concurrency, ramp profile, and steady-state duration.
4. Run against an isolated authorized environment with synthetic/approved data.
5. Ramp to target load gradually and sustain the approved target period.
6. Monitor latency percentiles, throughput, error rate, queue depth, CPU, memory, database, and network.
7. Verify autoscaling and capacity limits where they are part of the design.

## 5. Pass criteria
- [ ] Forecast source is named, linked, and approved.
- [ ] The system sustains the documented expected/peak workload for the approved duration.
- [ ] Latency and error rate meet documented objectives.
- [ ] No uncontrolled queue growth, resource exhaustion, or data corruption occurs.
- [ ] Environment, workload, and measurements are recorded.

## 6. Release gate
Failure to sustain required capacity blocks launch or requires an explicit decision by `release_owner`. Missing forecast evidence is BLOCKED, not PASS.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Forecast source examples: product-management capacity plan, analytics report, contractual capacity requirement.
- The agent MUST NOT invent traffic forecasts, concurrency targets, or acceptable thresholds.
- Load testing MUST NOT target production without explicit written approval and safety controls.

## 9. Execution record
See `00-agent-contract.md` §6.
