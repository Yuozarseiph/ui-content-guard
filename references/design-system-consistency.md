# Design-system consistency and change scope

## Inspect first

Where project access is available, examine:

1. Nearby screens and recurring patterns (labels, headings, helper text, errors, toasts, confirmations).
2. Reusable components and their API for required, optional, disabled, loading, and validation states.
3. Existing localization keys, translation namespaces, pluralization and number/date formatters.
4. Product vocabulary: object names, roles, statuses, navigation, currency/units and metrics definitions.
5. Accessibility implementation for controls (names, associations, status regions, keyboard behavior).
6. Existing tests and conventions for content and behavior.

Do not claim inspection of inaccessible code or screenshots. If only a prose request is available, provide best-effort patterns but label assumptions.

## Rules for changes

- Reuse existing labels where meaning matches; don't introduce synonyms merely to vary tone.
- Keep the established page hierarchy, component density, spacing, and interaction patterns. A content change does not authorize redesigning the layout.
- Prefer changes inside the requested component and associated tests/translations; avoid unrelated edits.
- Do not add new packages for strings, tooltips, schema wrappers, or localization if the product already handles them.
- Preserve localization keys when safe. When changing meaning, update keys and translations according to project convention; do not leave inconsistent fallback strings.
- Check mobile wrap, truncation, zoom and RTL before deciding a label is concise enough.
- Do not duplicate text both below a control and in its tooltip unless each serves a different, necessary function.
- Match the product's established error and success patterns; keep true system status.

## Mini terminology ledger

Before proposing copy, capture a compact mapping when relevant:

| Concept | Established term | Avoid | Where confirmed |
| --- | --- | --- | --- |
| Workspace membership | `Member` | `User`, `Collaborator` interchangeably | Navigation + invite dialog |
| Publish flow | `Publish` | `Release`, `Submit` interchangeably | Main call-to-action |
| Failed transaction | `Payment failed` | `Error 402` | Billing state |

The examples above illustrate a ledger; **never assume these specific words are correct for an uninspected product**.

## Verification

Review changed UI in compact/mobile layouts, at increased text size, with keyboard navigation, and in all supported locales where possible. If such checks cannot be run, state that they remain unverified rather than asserting cross-platform correctness.
