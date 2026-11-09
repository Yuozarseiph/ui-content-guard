# Content audit: full-state review and remediation

## Scope

Audit the entire user journey for the requested surface, not just visible strings in one screenshot. Where accessible, inspect headings, form labels, help, tooltips, errors, loading, empty results, success, permissions, confirmation, navigation, metric labeling, responsive layouts, RTL, screen-reader names and status announcements.

## Workflow

1. **Inventory surfaces:** page, component, modal, notifications, onboarding, error path, and localized variants.
2. **Trace requirements:** capture user goals, behavior contracts, data/security boundaries, and content intentionally required by policy.
3. **Inspect actual evidence:** source code, UI, state transitions, design tokens, tests, translation catalogs.
4. **Classify content:** implementation leak, duplication, ambiguity, inconsistency, missing disclosure, accessibility gap, or misleading state.
5. **Prioritize:** use the severity rubric below; assign the highest applicable level.
6. **Fix concretely:** propose replacement microcopy, an omission, a behavior change, or an accessible association; include exact location.
7. **Verify:** test or specify a reproducible acceptance check. Report limits if source/UI cannot be inspected.

## Severity rubric

| Level | Conditions | Example | Action |
| --- | --- | --- | --- |
| **CRITICAL** | Exposed secret/private information; materially misleading promise; missing material irreversible consequences; essential action inaccessible | Raw token in error; permanent deletion with no warning; important control unnamed to assistive technology | Block release until mitigated and verified |
| **HIGH** | Core task is confusing or impossible; missing necessary guidance; wrong validation or recovery; material status ambiguity | “Saved” while writes have not finished; upload restriction missing and unrecoverable | Fix before shipping the affected flow |
| **MEDIUM** | Redundant explanation; repeated instructions; inconsistent terminology; unnecessary copy density | “These filters are independent” under clear independent controls | Improve in planned cleanup; no safety loss |
| **LOW** | Minor non-material tone, grammar, or punctuation issue | Inconsistent sentence-ending periods in toasts | Fix when touching relevant copy |

A problem's severity is contextual. Excess words around a payment disclosure may be medium, but a missing renewal price is critical.

## Finding template

```text
Location: Settings > Account > Delete
Evidence: Screenshot of dialog (or file + line when available)
Issue: Dialog says “Continue?” without naming deleted data.
Category: Missing material consequence
Severity: CRITICAL
User impact: Cannot make an informed irreversible decision.
Proposed UI: “Delete account and all stored files? This can't be undone.”
Implementation: Ensure cancellation and server-side authorization work.
Verification: Trigger dialog, inspect focus, cancel path, screen reader name,
              successful delete state, and responsive layout.
Confidence: Verified from screenshot; API deletion behavior not verified.
```

## Content-density analysis

Flag repetition rather than counting words mechanically. Ask whether a sentence provides new information at the right time. Detect chains of `heading → subtitle → helper → tooltip` repeating the same concept. Use labels or short supporting copy when sufficient, and retain non-obvious limits or risks. Avoid artificial scores presented as objective UX metrics without user research.

## QA checklist

- [ ] No developer or technical instructions accidentally rendered.
- [ ] Essential user-facing facts are present before commitment.
- [ ] Each field has a persistent, meaningful accessible name.
- [ ] Guidance is specific, contextual, and not duplicated.
- [ ] Errors state recovery and do not reveal internal data.
- [ ] Success/progress claims correspond to verified system stages.
- [ ] Empty and filtered-empty states are distinct from errors.
- [ ] Permission failures and destructive confirmations are understandable.
- [ ] Terminology, capitalization, units, dates and locales are consistent.
- [ ] Persian/RTL and mixed-script layouts are correctly handled when relevant.
- [ ] Responsive reflow and enlarged text do not hide key messages.
- [ ] Tests/observations are distinguished from assumptions.

## Output contract

For audit-only work, list findings sorted by severity; provide targeted replacement copy and implementation behavior checks. If no issues are found, say what was actually reviewed. For implementation work, apply minimal scoped edits, run available tests, and report unverified behavior explicitly.
