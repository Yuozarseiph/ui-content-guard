# Form and interaction copy

## Field model before helper text

Inspect the form contract: field types, default values, required/optional constraints, supported combinations, validation timing, dependencies, backend behavior, and errors. A field's *behavior* often resolves the need for an explanatory paragraph.

- Use stable labels even when placeholders or values are visible.
- Mark required/optional status consistently with the existing design system; don't add “optional” to every field if a form-level convention is already clear.
- Show units and formats where surprising or necessary (`Budget (USD)`, accepted file types, time zone).
- Preserve independent selection, clearing, and keyboard operation of each independently optional control.
- Separate format guidance from validation feedback; only show each when relevant.
- Avoid constraints that exist only in the frontend when the backend rejects different values.
- If the user must understand a downstream consequence, display it before commitment; do not hide it in hover text.

## Helper vs tooltip vs validation vs confirmation

| Situation | Recommended treatment | Rationale |
| --- | --- | --- |
| Obvious single-line text field | Label; no helper | Input affordance already clear |
| File accepts only PDFs up to 10 MB | Persistent or contextual helper near upload | Restriction affects selection and recovery |
| Optional date/time with straightforward independent controls | Two labels and optional indication according to conventions | Requirement is about logic, not a tutorial |
| Field currently invalid | Inline accessible validation tied to field | Timely, actionable correction |
| A rarely needed definition | Accessible tooltip or supplementary help | Secondary context; not essential |
| Destructive action | Confirmation with consequence and precise labels | Informed action and recovery |
| Permission prevents action | Accurate affordance and understandable explanation where needed | Prevents mystery disabled controls |
| Charge or subscription | Clearly visible price/renewal terms before purchase | Material informed consent |

## Independent controls example

**Requirement:** “The status and assignee filters must be independently clearable and combinable.”

**UI:** `Status` and `Assignee`; clear buttons with accessible names `Clear status` and `Clear assignee` where used. No paragraph “These filters work separately.”

**Acceptance:** none/status only/assignee only/both produce correct results; changing one preserves the other; selection state is announced and visible; no-results is distinct from fetch errors.

## Upload example

**Requirement:** “Reject files larger than 10 MB and accept PDF only; verify server-side.”

**UI:** `Upload document` and `PDF only, up to 10 MB`. If rejected: `Choose a PDF smaller than 10 MB.`

**Acceptance:** client guidance and server validation agree; invalid files never appear uploaded; keyboard and screen reader feedback is available.

## Confirmation example

**Requirement:** “Deleting a project permanently removes its members' files.”

**UI:** `Delete project` → dialog `Delete “Atlas”?` / `This permanently deletes the project and its files for all members.` / buttons `Cancel`, `Delete project`.

**Acceptance:** confirmation occurs *before* deletion; focus moves into dialog and returns safely on cancel; final state is announced; server authorization is enforced.

## Anti-patterns

- Required information inside placeholders that disappear on typing.
- Helper text under every field because the component supports it.
- Error copy that simply repeats the field label.
- Tooltips as the only disclosure of a fee, retention period, or risk.
- Confirmation text without the affected object or irreversibility when material.
- A button reading “Done” while data is still being processed.
