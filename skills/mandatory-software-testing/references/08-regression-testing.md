# Regression Testing

**Label:** `AI-EXECUTABLE`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Verify that a change has not broken previously working behavior or reintroduced previously fixed defects.

## 2. Prerequisites
A target branch and baseline MUST be identified. Baseline is the last green run on that target branch plus an explicit inventory of previously fixed defect IDs. Follow central baseline/flaky rules.

## 3. When required
After every code change, bug fix, refactor, dependency upgrade, schema change, and before every release.

## 4. Procedure
1. Identify target branch, current commit, and last green run for the relevant suite on that branch.
2. Load the previously-fixed defect inventory and record defect IDs relevant to changed or high-risk areas.
3. Determine impacted modules and select the automated regression suite plus required focused manual scenarios.
4. Run critical workflows, permissions, data integrity, API contracts, and previously fixed defect tests relevant to scope.
5. Compare results to baseline and classify failures NEW/PRE-EXISTING with evidence and defect IDs.
6. Update expected results only when behavior intentionally changes and an authorized requirement/owner approves the change.

## 5. Pass criteria
- [ ] Baseline reference is the last green target-branch run or an explicitly approved alternative.
- [ ] Previously fixed defect IDs in scope are retested.
- [ ] All NEW failures are resolved and retested or formally dispositioned by an authorized human where policy permits.
- [ ] PRE-EXISTING failures remain linked to baseline and defect IDs.
- [ ] No expected result was changed merely to hide a failure.

## 6. Release gate
Any unexplained NEW regression blocks release. PRE-EXISTING failures remain visible and cannot be reported as a fully green suite.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Baseline MUST include both the last green run and explicit previously-fixed defect IDs.
- If either source is unavailable, state the gap; if it prevents reliable classification, set BLOCKED/PARTIAL.
- A regression test that passes only on diagnostic rerun is FLAKY under the central policy.

## 9. Execution record
See `00-agent-contract.md` §6.
