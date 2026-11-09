# Sanity Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Quickly verify that a focused change or fix behaves as intended and that its immediate callers are not obviously broken.

## 2. Prerequisites
A specific change/defect and expected behavior MUST be identified. Baseline and flaky policies in `00-agent-contract.md` apply.

## 3. When required
After a focused bug fix, small patch, configuration change, or narrowly scoped modification.

## 4. Procedure
1. Define scope as the files touched by the change plus their direct callers.
2. List the exact defect or behavior being checked and its expected result.
3. Run focused tests for the changed behavior and direct callers only.
4. Reproduce the original defect conditions and verify the defect no longer occurs.
5. Check directly adjacent boundary/error cases.
6. Explicitly list all relevant areas outside this scope as NOT tested; do not imply broad regression coverage.

## 5. Pass criteria
- [ ] Targeted changed behavior meets its stated expected result.
- [ ] Original defect is not reproducible under the recorded conditions.
- [ ] Direct callers in scope pass their focused checks.
- [ ] Scope not tested is explicitly listed.

## 6. Release gate
A failed sanity check blocks verification of the patch. Sanity PASS MUST NOT be represented as full regression or release readiness.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Scope is strictly changed files plus direct callers. Transitive system behavior is outside scope unless separately tested.
- Any test outside this scope MUST be reported as NOT tested, not assumed covered.

## 9. Execution record
See `00-agent-contract.md` §6.
