# Integration Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Verify that collaborating modules and external dependencies communicate correctly through their real interfaces and protocols.

## 2. Prerequisites
Relevant Unit tests MUST be PASS. Integration boundary inventory, test configuration, and approved isolated dependencies MUST exist. Follow baseline rules in `00-agent-contract.md`.

## 3. When required
After component integration and after API, database, queue, cache, authentication, adapter, or serialization changes; before release.

## 4. Procedure
1. List every changed integration boundary and its expected contract.
2. MUST run each integration test in an isolated environment with isolated data.
3. MUST make tests idempotent: repeated execution MUST NOT create cumulative state or depend on prior runs.
4. Use real dependency instances where feasible, such as Testcontainers or LocalStack; use WireMock or equivalent protocol-faithful doubles for external HTTP services when real services are unavailable or prohibited.
5. MUST verify serialization, API/schema compatibility, persistence, transactions, retries, timeouts, and error propagation where applicable.
6. SHOULD maintain consumer/provider contract tests using Pact, OpenAPI validation, or an equivalent contract mechanism.
7. MUST verify cleanup and ensure no production/shared data is touched.

## 5. Pass criteria
- [ ] Relevant Unit tests are PASS.
- [ ] Every integration test is isolated and idempotent.
- [ ] Observed requests/responses conform to the declared API or message contract.
- [ ] Persistence, transaction, retry, timeout, and failure behavior required by scope passes.
- [ ] Test resources and data are cleaned up or their retention is documented.

## 6. Release gate
A NEW integration failure blocks system testing and release promotion. Missing dependency access or an unavailable isolated environment is BLOCKED, not PASS.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Allowed dependency approaches: Testcontainers, LocalStack, WireMock, or equivalent approved tools already available in the project.
- Contract-test artifacts MUST be linked in the execution evidence.
- Test doubles MUST preserve the relevant protocol/contract; a simplistic mock that bypasses serialization or transport behavior is insufficient.

## 9. Execution record
See `00-agent-contract.md` §6.
