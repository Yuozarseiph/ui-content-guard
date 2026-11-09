# Security Testing

**Label:** `AI-ASSISTED`  
**Agent rules:** See `00-agent-contract.md` (MANDATORY reading before execution).

## 1. Objective
Identify vulnerabilities and verify that security controls protect application data, identities, services, and infrastructure.

## 2. Prerequisites
A written security test scope authorization MUST exist before ANY active scan, exploit attempt, or penetration test. The scope artifact MUST be stored at `docs/security/test-scope.md` or an explicitly recorded repository-approved equivalent. `security_owner` must be mapped.

## 3. When required
Before first launch; before major security-sensitive releases; continuously for approved passive dependency/configuration checks.

## 4. Procedure
1. Read the written scope authorization and confirm target assets, allowed techniques, rate limits, test window, exclusions, and emergency contact.
2. If scope authorization is missing, expired, or ambiguous, do not run active tests; set BLOCKED.
3. Review threat model, authentication, authorization, session management, secrets, least privilege, and trust boundaries.
4. Within authorized scope, test relevant injection, XSS, CSRF, SSRF, access-control bypass, file upload, API abuse, and other applicable risks.
5. Scan dependencies, containers, infrastructure, configuration, and exposed endpoints using approved tools.
6. Review encryption, sensitive logging, backups, rate limits, and security headers where applicable.
7. Verify findings manually where required; classify severity, assign owner, remediate, and retest.
8. Report scanner output as tool evidence only; a clean scanner result alone MUST NOT be treated as a clean security posture.

## 5. Pass criteria
- [ ] Written scope authorization exists and covers every active test target/technique.
- [ ] No unresolved critical/high finding remains unless formally accepted by `security_owner` under policy.
- [ ] Authorization tests show users/tenants cannot access each other's protected data.
- [ ] Secrets and sensitive data are not exposed in code, logs, artifacts, or client bundles.
- [ ] Findings include severity, evidence, remediation owner, and retest status.
- [ ] Manual review/threat-model coverage limitations are disclosed; scanner-only output is not a security PASS.

## 6. Release gate
Security testing is a mandatory launch gate. Any out-of-scope or unauthorized active test MUST NOT run. Scanner-only clean results cannot satisfy the full security gate.

## 7. Evidence
See `00-agent-contract.md` §6 (Output contract).

## 8. Test-specific rules
- Scope file default: `docs/security/test-scope.md`. If another location is approved, record it.
- Written authorization MUST precede active scans and penetration tests, not merely be obtained afterward.
- `security_owner` owns security scope authorization and risk disposition; an agent cannot approve its own findings.
- A scanner with zero findings is not proof that the system is secure.

## 9. Execution record
See `00-agent-contract.md` §6.
