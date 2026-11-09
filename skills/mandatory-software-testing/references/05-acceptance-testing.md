# Acceptance Testing

**Label:** `HUMAN-ONLY`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Determine whether the product satisfies agreed business requirements and acceptance criteria, with approval provided by an authorized human stakeholder.

## 2. Prerequisites
System and critical E2E tests MUST be PASS. Acceptance criteria MUST be approved and versioned. `product_owner` MUST map an `authorized_delegate` before testing begins.

## 3. When required
On a feature-complete release candidate before launch, contractual handover, or business sign-off.

## 4. Procedure
1. Read the approved acceptance criteria and link each criterion to its requirement or user story.
2. `product_owner` MUST identify the authorized human stakeholder or `authorized_delegate` before execution.
3. Prepare scenarios, synthetic/approved-anonymized data, and evidence templates for the human tester.
4. The authorized human MUST execute or directly witness the acceptance scenarios and record criterion-level outcomes.
5. The agent MAY organize evidence and identify missing criteria, but MUST NOT impersonate the stakeholder, provide the stakeholder's judgment, or record acceptance as PASS on their behalf.
6. Attach the stakeholder's signed/attributable approval evidence and record rejected, deferred, or conditional criteria.

## 5. Pass criteria
- [ ] System and critical E2E prerequisites are PASS.
- [ ] Every mandatory acceptance criterion has a human-attributed result.
- [ ] Approval evidence is attributable to the mapped authorized delegate/product owner.
- [ ] No criterion is marked accepted solely by an AI agent.

## 6. Release gate
No production launch where business acceptance is required without explicit human sign-off. AI-generated summaries are not acceptance approval.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- `authorized_delegate` MUST be mapped by `product_owner` before the test begins.
- The AI MUST NOT create, forge, infer, or sign stakeholder approval.
- Acceptance evidence MUST use synthetic or approved-anonymized data and follow the central privacy policy.

## 9. Execution record
See `00-agent-contract.md` §6.
