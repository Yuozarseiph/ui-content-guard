# Usability Testing

**Label:** `HUMAN-ONLY`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Evaluate whether representative intended users can understand and complete critical tasks effectively through observed human participation.

## 2. Prerequisites
A human-led protocol, target-user criteria, task script, mapped `ux_owner`, informed consent, recording decision, and retention/deletion policy MUST be approved before sessions.

## 3. When required
Before launch for user-facing products; after major UX changes; when support/analytics indicate task-completion problems.

## 4. Procedure
1. `ux_owner` MUST define target-user characteristics and objective inclusion/exclusion criteria based on the intended audience.
2. Define critical tasks, session protocol, success measures, observation method, recording choice, access controls, and retention/deletion schedule before recruiting.
3. Obtain informed consent before collecting participant responses, recordings, or identifiable data.
4. A human facilitator MUST conduct sessions with representative participants; an AI agent MUST NOT impersonate participants or fabricate observations.
5. Observe task completion without leading participants; record completion, errors, time, assistance, and participant comments with consent.
6. Redact PII from evidence and store recordings/notes under the approved access and retention policy.
7. Prioritize findings by task impact and frequency; obtain human UX review.

## 5. Pass criteria
- [ ] Participant criteria and recruitment method are documented and match the intended audience.
- [ ] Consent was obtained before data collection.
- [ ] Recording and retention/deletion policy was followed.
- [ ] Critical task outcomes are recorded from actual human sessions.
- [ ] No participant feedback or observation was fabricated by an AI agent.
- [ ] Severe issues preventing a critical task are triaged by `ux_owner`.

## 6. Release gate
An AI agent cannot mark usability testing PASS without human sessions and attributable evidence. Missing participants, consent, or UX ownership is BLOCKED.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- This test is HUMAN-ONLY. AI MAY prepare scripts, organize anonymized notes, calculate metrics, and draft summaries.
- Informed consent, data minimization, access control, retention, and deletion are mandatory.
- Participant criteria MUST be defined before recruitment; convenience samples MUST be labeled as such and cannot be represented as representative without evidence.

## 9. Execution record
See `00-agent-contract.md` §6.
