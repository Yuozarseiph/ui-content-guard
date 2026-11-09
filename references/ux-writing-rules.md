# UX writing rules by interface element

Each category below specifies its **purpose**, **writing rules**, **common mistake**, and **good/bad** examples. Adapt tone and terminology to the product's audience and established style. “Bad” indicates a typical defect, not a universally banned phrase.

| Element | Purpose | Writing rules | Common mistake | Good example | Bad example |
| --- | --- | --- | --- | --- | --- |
| Page heading | Orient the user to their task | State the destination/task in known terms; usually one concise heading | Explaining page architecture in the heading | `Team settings` | `Here you can manage and configure everything about your team's settings` |
| Section heading | Group related decisions | Use parallel, distinctive nouns or actions; avoid repetition | Section titles restating page title | `Notifications` | `Options related to your notifications and notification preferences` |
| Field label | Identify expected input | Persistent, unambiguous label; expose units/format where needed | Placeholder-only identity; ambiguous jargon | `Invoice email` | `Email thing` |
| Button | Predict the immediate action | Use a clear verb and object; distinguish Save, Submit, Send, Delete | Generic `OK` for irreversible actions | `Delete project` | `Proceed` |
| Link | Predict the destination | Specific accessible link text; avoid duplicated adjacent links | “Click here”; link text stripped of context | `View billing history` | `Click here` |
| Placeholder | Show an example of expected format | Make optional examples short, not instructions or labels | Placeholder used as label or long helper text | `name@example.com` | `Please type your email address in this box` |
| Helper text | Clarify a genuine constraint or consequence | Show only information not already obvious; place near affected control | Text describing built-in control mechanics | `Maximum 10 MB. PDF only.` | `Use this button to upload a file.` |
| Tooltip | Provide secondary detail | Brief, accessible, supplementary only; don't hide essential info | Costs or mandatory warnings only on hover | `Includes archived projects` | `Your data is permanently deleted` (only in tooltip) |
| Error message | Explain failure and recovery | Name issue, location, remedy; be accurate and kind | Internal error codes or blame | `Enter a valid email address.` | `ERROR_422_INVALID_EMAIL_PARAM` |
| Success message | Confirm real, meaningful outcome | Say what completed, not how; avoid toast spam | Claiming success before persistence | `Changes saved.` | `Database row transaction successfully finalized!` |
| Warning message | Surface meaningful risk in time | State consequence and prevention; keep prominent | Generic warnings unrelated to next action | `This will sign out everyone on the account.` | `Warning: please be careful.` |
| Confirmation dialog | Support informed consequential choice | Specific action, object, effect; distinct confirm/cancel actions | Vague “Are you sure?” alone | `Delete workspace? This can't be undone.` | `Continue?` |
| Empty state | Explain absent data and next action when helpful | Distinguish no records, no search results, and errors | Blaming user; filler text | `No invoices yet.` | `Oopsie! It looks like nothing exists here right now.` |
| Loading state | Communicate actual progress | Concise, accurate; show stage when meaningful | Pretending completion during processing | `Processing file…` | `Done!` (while still processing) |
| Notification | Surface a timely change or required action | Concise event + action, suppress duplicates | Generic success for non-events | `Export ready. Download file.` | `Something new has happened in your system!` |
| Dashboard metric | Label a measure accurately | Include unit, period, population, and comparison when material | Ambiguous numbers without timespan | `Revenue · last 30 days` | `Revenue: 109` |
| Navigation | Make destinations predictable | Favor stable familiar terminology; align page and nav labels | Different names for same destination | `Billing` | `Financial operations center` (for basic invoices) |
| Onboarding | Help first-time users complete a real task | Prefer action-focused steps, show only when needed, allow skipping where appropriate | Mandatory generic tour before task | `Create your first project` | `Welcome to our wonderful application journey!` |

## Style principles

- **Clarity first:** a short but ambiguous label is worse than a slightly longer precise label.
- **Plain language:** prefer verbs people use naturally; avoid machine-generated pleasantries and inflated claims.
- **Parallel grammar:** keep equivalent buttons, labels, and states consistent across screens.
- **Concrete scope:** identify affected object, period, and unit in consequential or statistical text.
- **True state:** never equate request received with completed; never use “saved” before confirmed save.
- **No double instructions:** labels and controls ordinarily explain ordinary interactions; helper copy should add new value.
- **Preserve context:** accessible names, status messaging, and important conditions matter even when visual copy is compact.

## Writing across languages

Write microcopy in the UI's selected locale, not necessarily in the developer's language. Translate the *intent and terminology*, not the literal English sentence structure. Use [accessibility and localization](accessibility-and-localization.md) for Persian/RTL rules and examples.
