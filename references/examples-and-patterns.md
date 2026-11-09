# Reusable patterns and difficult boundary cases

## Pattern: “behavior requirement, not UI copy”

**Input:** “The assignee filter and status filter can be used independently.”

**Use:** two clear labeled filters; reliable combined/independent filtering; accessible clearing. **Avoid:** a permanent paragraph explaining independent filters. **Exception:** if users repeatedly misunderstand interaction due to an unusual control, concise contextual guidance may be warranted.

## Pattern: implementation complexity stays internal

**Input:** “Use a background worker and deduplicate job IDs.”

**Use:** `Processing…`, `Ready`, or an accurate retry state based on actual progress. **Avoid:** “Our workers and queue are deduplicating your request.” **Exception:** operator/admin observability screens whose explicit task is to inspect jobs can show queue details.

## Pattern: material constraint stays visible

**Input:** “Uploads must be PDF and at most 10 MB.”

**Use:** `PDF only, up to 10 MB`; reject invalid files before claiming success; validate server-side. **Avoid:** removing the restriction on minimalism grounds or presenting raw server errors.

## Pattern: permission restrictions are user-relevant

**Input:** “Billing edits are restricted to account owners.”

**Use:** accurate state, optionally `Only account owners can edit billing.` near the unavailable action; enforce access in backend. **Avoid:** explaining JWT claims or silently showing an action that always fails.

## Pattern: destructive actions require disclosure

**Input:** “Deletion is permanent and removes member files.”

**Use:** confirmation naming what is deleted and that it cannot be undone, with distinct `Cancel` / `Delete` actions. **Avoid:** ambiguous `Continue?` or hiding irreversibility behind a hover icon.

## Pattern: product metrics need a defined scope

**Input:** “Display MAU calculated from distinct authenticated sessions per calendar month.”

**Use:** `Monthly active users` with clear period; explanation of metric definition only if users need it for decisions. **Avoid:** `MAU (distinct authenticated sessions per UTC partition)` as a consumer dashboard subtitle. Verify the metric definition before making assertions.

## Pattern: genuine consent needs more than a checkbox

**Input:** “Get opt-in before sharing health data with the analytics provider.”

**Use:** clear, specific explanation of what is shared, with whom, why, and consequences where legally/product required, accompanied by meaningful choice. **Avoid:** `I agree` with no context or technical pipeline description. **Note:** legal requirements vary; the skill does not replace jurisdiction-specific review.

## Pattern: Persian copy respects the task

**Input:** “Enable optional time filter” for a Persian app.

**Use:** label `زمان` and meaningful validation like `زمان معتبر وارد کنید.` only if invalid. **Avoid:** `پارامتر زمان انتخابی Optional بوده و مستقل از تاریخ پردازش می‌گردد.`

## Pattern: responsive reduction is not content removal

When space is limited, adjust layout, wrapping, grouping, or progressive disclosure for **secondary** information. Keep essential constraints and consequences reachable and accessible at the decision point. Never drop accessible names because visible labels are replaced with icons.

For full four-part demonstrations see [developer instruction examples](../examples/developer-instruction-examples.md).
