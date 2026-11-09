# Errors, progress, and feedback

## Write for the state the system can prove

| State | User needs | Good message | Avoid |
| --- | --- | --- | --- |
| Validation | Which field, what to fix | `Enter a date on or after November 1.` | `Invalid input.` |
| Upload rejected | Accepted type/size, recovery | `Choose a PDF under 10 MB.` | `Upload failed (413).` |
| Connectivity failure | Clear failure and retry if safe | `Couldn't save changes. Check your connection and try again.` | `Database unavailable.` |
| Permission denial | Effective restriction and next step | `Only workspace owners can change billing.` | `403: insufficient claims.` |
| Processing started | Accurate pending state | `Export started. You'll be notified when it's ready.` (only if notifications exist) | `Export complete.` |
| Processing continues | State and optionally next step | `Processing your upload…` | `Everything is finished!` |
| Operation complete | Verified outcome | `Report downloaded.` | `Request queued successfully.` presented as completed download |
| No records | Clear absence, optional creation action | `No projects yet. Create a project to get started.` | `No data found in database.` |
| No search matches | Filter-specific absence | `No results match these filters.` | `No records exist.` |
| Recoverable partial failure | What worked and what did not | `2 of 3 files uploaded. Retry the remaining file.` | `Upload successful.` |
| Destructive result | Exact action completion | `Workspace deleted.` | `Operation success: HTTP 204.` |

## Error composition

Use `[problem] + [specific recovery]` where recovery exists. Explicitly separate **cannot retry**, **retry is safe**, and **retry could duplicate an operation**. Keep diagnostic codes in telemetry or expandable details for technical audiences, not primary UI copy. Never display raw API payloads, stack traces, secrets, or user-private metadata.

## Feedback mechanics

- Avoid duplicate announcements and repeated success toasts for every trivial action.
- For long operations, use real progress or neutral indeterminate status; never invent percentages.
- Distinguish **accepted**, **queued**, **processing**, **completed**, and **failed**. A `202 Accepted` response is not proof of completed work.
- Do not tell users “You'll receive an email” unless the email workflow exists.
- Keep focus and accessible live-region announcements aligned with validation and status changes.
- Preserve recovery data if possible after a failed submission; never clear an entire form without reason.

## Error levels and placement

- **Field-specific:** inline, associated with the correct input and announced on error.
- **Form-wide:** summary for multiple field errors or submission failures; offer navigation to fields where appropriate.
- **Transient/global:** banner, status, or notification according to product conventions.
- **Irreversible:** confirmation and policy disclosure *before* action, not merely an error after it.

Consult [accessibility and localization](accessibility-and-localization.md) and [content audit](content-audit.md).
