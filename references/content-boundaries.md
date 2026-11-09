# Content boundaries: from requirements to the right surface

## The decision is about *placement*, not simply length

A developer's message may mix system behavior, business rules, technical constraints, intended microcopy, and engineering context. Parse each clause separately. Never copy a paragraph into the UI just because it accompanies an implementation request. Never discard a policy because it appears inside a developer note.

| Source category | Typical signal | Correct destination | UI exception |
| --- | --- | --- | --- |
| Developer instruction | “Make”, “Ensure”, “Do not allow”, “Implement” | Behavior, tests, code | Intentional user-facing strings explicitly specified and checked for accuracy |
| Product requirement | Eligibility, fees, deadlines, retention, feature behavior | Implementation and product experience | Display constraints needed for informed action |
| Internal implementation detail | API name, queue, schema, worker, cache, internal ID | Source, logs, architecture docs | Only when the user needs actionable technical detail, such as an integration admin |
| User-facing content | Label, feedback, caution, disclosure, consent | UI string/component and localization catalog | No exception; ensure audience/placement are appropriate |
| Technical documentation | Runbook, API contract, deployment procedure | Docs and comments | Documentation interfaces intentionally created for technical users |

## A practical five-step classification

1. **Break down** the instruction into atomic behaviors, conditions, and proposed strings.
2. **Identify the audience** for each fact: end user, operator/admin, engineer, auditor, or support agent.
3. **Choose the destination:** code and tests; product UI; documentation; or internal operational telemetry.
4. **Apply the necessity test** to candidate UI content: purpose, risk, timing, redundancy, and accessibility.
5. **Verify the promise:** visible copy must match what the feature actually does, including partial failures and reversibility.

A statement may have two destinations. “The server permanently deletes uploaded files after 30 days” requires lifecycle logic, and in some contexts a visible retention disclosure. “Use Redis to schedule deletion” normally belongs only to implementation notes. Do not expose a storage provider in consent copy without a user reason.

## Examples of sensitive distinctions

- **Internal architecture:** “Authenticate via an API gateway” → implement authentication and appropriate UI states; do not show the gateway name.
- **Material business policy:** “The subscription renews at $12/month until canceled” → implement billing rules *and* disclose the renewal and pricing before purchase.
- **Required consent:** “We need the user's permission to share their data with a third party” → preserve a clearly labeled, meaningful opt-in if required. A tooltip alone is inadequate.
- **Permission restriction:** “Only owners may delete workspaces” → disable/omit action according to conventions, and if a visible restriction matters, state “Only workspace owners can delete this workspace.” Do not mention the internal role-check endpoint.
- **Privacy/security:** “Never expose raw tokens or PII in the UI” → ensure output redaction and safe error handling in code. A paragraph reassuring the user is not a substitute.
- **Developer-specified copy:** “Show ‘Your session has expired. Sign in again.’” → use the explicit wording if accurate and consistent, or explain a necessary correction; do not reinterpret it as a hidden engineering note.

## When *more* copy is needed

Visible explanation is valuable when users cannot infer a non-obvious consequence from an affordance: a data loss warning, a retention window, a charge, an invalid selection, an irreversible action, a consent consequence, or a permission limitation. This is **not** over-explaining. Place such information at the decision point, not buried in unrelated paragraphs.

## Anti-patterns

- Treat all requirements as copy, or all copy as noise.
- Replace clear interface labels with placeholders and call it minimalism.
- Put essential content only behind tooltips or hover.
- Remove warnings because their information is repeated in developer prose.
- Show inaccurate success claims to conceal async work.
- Leak technical error details into a consumer-facing UI.

Consult [content audit](content-audit.md) to report boundary failures with severity and actionable changes.
