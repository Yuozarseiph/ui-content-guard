# Alpha & Beta Testing

**Label:** `HUMAN-ONLY`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Validate a stabilized product through controlled internal alpha testing and limited representative external/real-world beta participation before general availability.

## 2. Prerequisites
Written alpha and beta exit criteria MUST be defined and approved by `product_owner` and `release_owner` BEFORE the relevant stage starts. Beta requires Alpha exit criteria PASS. Consent/privacy protocol, support route, feedback SLA, and rollback criteria MUST be ready.

## 3. When required
When the product's release model includes alpha/beta stages; alpha follows core feature stabilization and beta follows approved alpha exit.

## 4. Procedure
1. Before alpha begins, document scope, participant profile, eligibility, consent, privacy notice, data minimization, retention/deletion, feedback channel, support owner, exit criteria, and stop/rollback conditions.
2. Obtain human approval of alpha exit criteria before alpha starts; record approval evidence.
3. Conduct alpha with actual authorized internal participants; record attributable observations and defects.
4. Triage alpha findings and verify every alpha exit criterion before beta begins.
5. Before beta begins, obtain human approval of beta exit criteria and participant/data handling plan.
6. Recruit a limited representative cohort using documented eligibility criteria; obtain informed consent before collecting feedback or telemetry tied to participants.
7. Triage feedback within the approved feedback SLA; record owner, severity, decision, and remediation/retest.
8. Verify beta exit criteria and obtain explicit human release approval before general launch.

## 5. Pass criteria
- [ ] Alpha and beta exit criteria were written and approved before each stage started.
- [ ] Alpha exit criteria passed before beta began.
- [ ] Participant eligibility, consent, privacy notice, data minimization, and retention/deletion controls were followed.
- [ ] Feedback triage SLA and responsible owner are documented and met or breaches are reported.
- [ ] All participant feedback is attributable to real sessions/submissions; AI-generated or inferred feedback is never represented as participant feedback.
- [ ] No unresolved launch-blocking defect remains; exit approval is attributable to the mapped human roles.

## 6. Release gate
If alpha/beta are part of the release model, missing prior-approved exit criteria, consent controls, human participation, or exit sign-off blocks general launch. AI cannot fabricate participant feedback or approve stage exit.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- This test is HUMAN-ONLY. AI MAY prepare plans, summarize real feedback, cluster issues, and track SLA status.
- Privacy and consent MUST follow applicable law and the project's privacy policy; for EU/EEA participants, the project MUST have its GDPR role, lawful basis, notice, minimization, retention, and data-subject handling reviewed by the responsible human privacy/legal function.
- Feedback triage SLA MUST specify a measurable time window and responsible role before the stage starts.
- The agent MUST NOT invent participants, testimonials, survey responses, telemetry, or approval.

## 9. Execution record
See `00-agent-contract.md` §6.
