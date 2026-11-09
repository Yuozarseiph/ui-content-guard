# Exploratory Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Discover defects through structured exploration where scripted cases may miss unexpected states, sequences, or interactions.

## 2. Prerequisites
A completed charter MUST exist before each session. Relevant build/environment and safety boundaries must be known.

## 3. When required
During feature development and on release candidates, especially for novel, complex, or high-risk workflows.

## 4. Procedure
1. Create a charter using the required template: feature, risk, timebox, boundaries, out-of-scope, and note format.
2. Identify build, environment, test account/data, and safety restrictions.
3. Explore realistic and unusual workflows, boundary values, interruptions, unexpected sequences, and state transitions within the charter.
4. Vary roles and inputs using synthetic/approved data; do not access production customer data.
5. Record reproducible steps, expected/actual behavior, evidence, and impact for each finding.
6. Triage findings with the relevant owner and convert repeatable defects into regression tests where appropriate.
7. Close the session with coverage limitations and follow-up actions.

## 5. Pass criteria
- [ ] Charter is complete and timebox/boundaries were observed.
- [ ] Session notes identify build, environment, scope, and explored areas.
- [ ] Every finding has reproducible steps or is explicitly labeled as an observation needing confirmation.
- [ ] Critical/high findings are triaged and dispositioned.
- [ ] No sensitive data or unauthorized environment was used.

## 6. Release gate
Exploratory testing cannot be marked PASS without a completed charter and session record. Unresolved critical/high findings block the relevant release gate.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
### Charter template
- Feature / area:
- Risk hypothesis:
- Timebox (start/end):
- Build / environment:
- Boundaries / allowed actions:
- Out of scope:
- Test data / account:
- Notes format: action → observation → expected result → evidence → defect ID
- Exit criteria:
- Session owner / reviewer:

AI may explore approved test environments and analyze observations; human review is required for risk disposition.

## 9. Execution record
See `00-agent-contract.md` §6.
