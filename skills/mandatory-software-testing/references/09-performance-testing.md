# Performance Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Measure responsiveness, throughput, resource use, and scalability against documented performance objectives under a controlled, representative workload.

## 2. Prerequisites
Approved performance objectives/SLOs, workload model, test environment, and measurement tools MUST be identified. If objectives or workload assumptions are missing, BLOCKED.

## 3. When required
Before launch when performance is a product requirement; after material architecture, infrastructure, database, or performance-sensitive code changes.

## 4. Procedure
1. Obtain approved latency, throughput, error-rate, and resource objectives; do not invent thresholds.
2. Record environment specification: CPU, RAM, storage/I/O, network bandwidth/latency, database and queue versions/configuration, runtime, and deployment topology.
3. Define representative workload, dataset size, concurrency, request mix, and test duration with a named source/owner.
4. Warm up the system; discard warm-up measurements from reported steady-state statistics.
5. Run the measurement phase for at least the duration specified by the approved performance plan. If no duration is defined, BLOCKED.
6. Report p50, p95, and p99 latency, throughput, error rate, resource utilization, sample count, and confidence intervals where the tool supports statistically valid intervals.
7. Check variance across repeated measurement windows; investigate unstable results before comparing candidates.
8. Profile bottlenecks and repeat under equivalent conditions after approved optimization.

## 5. Pass criteria
- [ ] All approved performance objectives have measured results.
- [ ] Warm-up samples are excluded from steady-state results.
- [ ] p50/p95/p99, sample count, duration, environment specification, and confidence interval or reason unavailable are reported.
- [ ] Variance is measured and anomalous instability is explained.
- [ ] No unacceptable resource leak, saturation, or error-rate increase is observed against approved limits.

## 6. Release gate
If performance is a launch requirement, missing objectives, workload source, duration, or measurements block release. An agent MUST NOT invent SLOs or claim performance PASS from a single unqualified timing.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- The performance plan MUST define a minimum measurement duration; no universal duration is assumed here.
- Confidence intervals MUST be calculated using a method appropriate to the measurement distribution/tool; if not supported, report `unavailable` and the limitation.
- Environment changes invalidate direct comparisons unless normalized and documented.

## 9. Execution record
See `00-agent-contract.md` §6.
