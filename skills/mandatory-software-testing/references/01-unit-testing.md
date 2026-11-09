# Unit Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Verify individual functions, methods, classes, hooks, and modules in isolation against their contracts.

## 2. Prerequisites
No prior test suite is required. The changed unit's requirements/contract and test command MUST be known. Follow §4 baseline rules in `00-agent-contract.md`.

## 3. When required
During implementation, after every meaningful code change, and before each release.

## 4. Procedure
1. Identify changed units and document inputs, outputs, side effects, invariants, and error contracts.
2. MUST keep tests hermetic: no real network, real database, or filesystem access outside an isolated temporary directory.
3. MUST keep tests deterministic: use fake clocks/timers, seeded random generators, controlled concurrency, and no shared mutable state.
4. MUST ensure tests are order-independent and can run in isolation.
5. MUST cover normal, boundary, invalid, null/empty, and exception paths applicable to the contract.
6. MUST include at least one assertion in every test; failure-path tests MUST assert the specific error type/code/message contract, not merely that an exception was thrown.
7. MUST run the relevant unit suite and collect configured coverage for changed code.

## 5. Pass criteria
- [ ] Every executed test contains at least one assertion.
- [ ] All in-scope tests pass with first-run evidence; a test that fails then passes on diagnostic rerun is recorded as `FAIL` with `FLAKY` classification under the central policy.
- [ ] No test performs real network/database access or writes outside its isolated temporary location.
- [ ] Failure-path assertions identify the expected error contract.
- [ ] Configured coverage threshold is met; if none exists, report measured coverage without inventing a threshold.

## 6. Release gate
Any NEW unit failure blocks the change and release gate. PRE-EXISTING failures remain reported against the baseline; they do not permit a PASS claim for the affected suite.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Test doubles MUST be local deterministic fakes/stubs; use framework-supported fake timers and seeded RNG.
- Tests MUST NOT depend on execution order, wall-clock timing, external services, or shared mutable fixtures.
- Coverage percentages are evidence, not a substitute for assertions or behavior verification.

## 9. Execution record
See `00-agent-contract.md` §6.
