---
name: ui-content-guard
description: Review, write, or implement user-facing interface content without leaking developer instructions, internal technical explanations, or unnecessary copy into the UI. Use when building or auditing forms, dashboards, settings, flows, error states, onboarding, localization, accessibility labels, or design-system microcopy; distinguish implementation requirements from product-facing messages while preserving essential safety, privacy, consent, validation, and accessibility information.
license: MIT
metadata:
  version: "1.0.0"
---

# UI Content Guard

**Principle:** Implement what the developer explains. Do not display the developer's explanation to the end user.

This skill is **agent-agnostic, framework-agnostic, and dependency-free**. Apply it to interface design, implementation, copy review, and refactoring. Its goal is meaningful, accurate UI content—not simply less text.

## 1. Establish context before writing

1. Inspect the actual UI and related flows, component conventions, existing strings, localization files, product terminology, validation logic, and design system when accessible.
2. Identify the intended audience, task, language, locale, user permissions, risks, and established interaction model. Never assume the language of a developer request is the UI language.
3. Preserve existing layout, styling, navigation, accessibility, and naming unless the request specifically requires changing them.
4. If only a description is available, distinguish assumptions from observed behavior. Do not claim to have audited unseen screens or tested unrun code.

For applicable details, consult [design-system consistency](references/design-system-consistency.md) and [accessibility/localization](references/accessibility-and-localization.md).

## 2. Separate five content categories

Classify each relevant statement before deciding where it belongs:

| Category | Meaning | Default disposition |
| --- | --- | --- |
| Developer instruction | An instruction to the implementer | Implement; **do not render verbatim** |
| Product requirement | Expected user-visible behavior or policy | Implement; render only what users must know |
| Internal implementation detail | APIs, persistence, queues, schemas, internal reasoning | Keep in code, tests, logs, or technical docs; never expose by default |
| User-facing content | Labels, feedback, essential guidance, policy disclosures | Render deliberately, using the product's language and conventions |
| Technical documentation | Engineering notes, operational explanations, API contracts | Place in documentation, not product UI |

A single statement can imply both an implementation action and an essential user-facing disclosure. **Extract both separately.** Treat explicitly requested user copy as a candidate, then check accuracy, safety, clarity, accessibility, and product context; do not silently override legitimate product requirements.

See [content boundaries](references/content-boundaries.md).

## 3. Apply the content necessity test

Before adding or retaining visible text, ask:

1. Does the user need this to complete a task or make an informed decision?
2. Is the meaning already clear from labels, affordances, or surrounding context?
3. Does it prevent a realistic misunderstanding or communicate a limitation?
4. Does it disclose an important cost, consequence, risk, permission, privacy use, or consent choice?
5. Is it necessary for validation, recovery, system status, or accessibility?

**Decision:** Keep essential content; simplify useful but wordy content; move secondary content to appropriate contextual help; omit unsupported or redundant content. Never hide critical information exclusively in tooltips, placeholders, hover states, color, or icons. Do not delete contractual, legal, safety, financial, privacy, consent, or accessibility requirements merely for brevity.

## 4. Implement behavior, not explanatory prose

Developer: “Date and time are independent and optional.”

- **Incorrect UI:** “Date and time are independent and optional. Choose one, both, or neither.”
- **Correct UI:** Two clear controls labeled “Date” and “Time”, no needless paragraph. Indicate optionality only if the existing pattern requires it.
- **Correct behavior:** Accept neither, either, or both; validate each supplied value independently; preserve filters and meaningful empty states.

Developer: “Store uploads using a background job.”

- **Incorrect UI:** “We use an asynchronous queue and workers to handle your upload.”
- **Correct UI:** “Uploading…” followed by “Upload complete”, or accurate processing status when meaningful.
- **Correct behavior:** Handle asynchronous states, retries and failures without falsely claiming completion.

More patterns: [examples and patterns](references/examples-and-patterns.md), [developer-instruction examples](examples/developer-instruction-examples.md).

## 5. Produce UI copy using a consistent system

- Prefer familiar, action-oriented, concrete wording in the user's interface language.
- Favor descriptive labels and controls over explanatory paragraphs; do not use placeholder text as the only field label.
- State errors with the problem and actionable recovery; do not leak stack traces or internal codes by default.
- Make confirmations proportionate to consequences; preserve irreversible-action warnings.
- Show meaningful loading, success, empty, offline, and permission states when relevant.
- Keep terminology, capitalization, punctuation, number/date formats, and translation keys consistent.
- For Persian/RTL, use natural Persian microcopy and correct bidi handling for mixed-script data.

For detailed rules consult [UX writing rules](references/ux-writing-rules.md), [forms and interactions](references/form-and-interaction-copy.md), [errors and feedback](references/error-and-feedback-messages.md), and [accessibility and localization](references/accessibility-and-localization.md).

## 6. Audit the complete experience

Audit the screen **and its states**: default, keyboard/focus, loading, errors, success, empty, permissions, destructive actions, and relevant responsive layouts. Compare the UI to requirements and implemented behavior. Record each issue with its location, evidence, severity, user impact, proposed copy or behavior fix, and verification approach.

Severity:
- **CRITICAL** — security/privacy exposure, misleading material claims, missing material consequences, or inaccessible essential actions.
- **HIGH** — confusing core interactions, missing important guidance, incorrect validation or recovery.
- **MEDIUM** — redundant copy, needless helpers, terminology inconsistency, unnecessary content density.
- **LOW** — minor tone, punctuation, or non-material stylistic inconsistencies.

Fix critical and high issues first, but do not recommend removing essential information. See [content audit](references/content-audit.md).

## 7. Deliver and verify

When implementing: make focused changes, preserve the existing design system, and run available project checks. When reviewing: provide actionable findings and precise replacement copy, explicitly distinguishing verified observations from assumptions.

Final checklist:
- [ ] Developer instructions were implemented, not pasted into UI.
- [ ] Every visible sentence has a user-facing purpose.
- [ ] Required consent, safety, cost, privacy, and destructive-action information is present.
- [ ] Accessible names, descriptions, keyboard flows, and announcements remain intact.
- [ ] Existing terminology, translations, and RTL behavior are respected.
- [ ] Errors, loading, empty, and success states accurately reflect real behavior.
- [ ] Scope is controlled; no speculative UX or unrelated changes were introduced.
- [ ] Tests and limitations are reported truthfully.

**Priority rule:** Follow applicable higher-priority instructions and the product's verified requirements. Content minimization is never a justification for hiding material information or for claiming functionality that is not implemented.
