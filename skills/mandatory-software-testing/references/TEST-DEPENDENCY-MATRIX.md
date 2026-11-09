# Test Dependency & Release Matrix

This matrix supplements `00-agent-contract.md`; the central contract is authoritative.

| Test | Default label | Minimum prerequisite | Default lifecycle |
|---|---|---|---|
| Unit | AI-EXECUTABLE | Changed code + contract | Continuous |
| Integration | AI-EXECUTABLE | Relevant Unit PASS | Continuous / pre-release |
| System | AI-ASSISTED | Relevant Integration PASS | Pre-launch |
| E2E | AI-ASSISTED | Candidate Smoke PASS | Pre-launch / critical flows |
| Acceptance | HUMAN-ONLY | System + critical E2E PASS | Pre-launch sign-off |
| Smoke | AI-EXECUTABLE | Build + authorized environment | Every build/deployment |
| Sanity | AI-EXECUTABLE | Defined changed scope | After focused change |
| Regression | AI-EXECUTABLE | Target branch baseline | Every change / pre-release |
| Performance | AI-ASSISTED | Approved SLO/workload/duration | Pre-launch when required |
| Load | AI-ASSISTED | Named linked forecast source | Pre-launch when capacity matters |
| Stress | AI-ASSISTED | Approved plan + isolated environment | Risk-based pre-launch |
| Security | AI-ASSISTED | Written scope authorization for active tests | Pre-launch + ongoing |
| Usability | HUMAN-ONLY | Human protocol, criteria, consent | Pre-launch for user-facing products |
| Compatibility | AI-EXECUTABLE | Official support matrix | Pre-launch / platform changes |
| Exploratory | AI-ASSISTED | Completed charter | Continuous / pre-launch |
| Alpha/Beta | HUMAN-ONLY | Pre-approved exit criteria; Beta after Alpha | Staged pre-launch |

## Decision
A missing prerequisite results in BLOCKED or PARTIAL, never PASS. A mandatory applicable gate that is NOT RUN, FAIL, BLOCKED, or PARTIAL results in NO-GO. Only the mapped human `release_owner` can make the final production release decision.
