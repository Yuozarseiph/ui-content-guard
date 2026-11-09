# Accessibility, multilingual content, and Persian/RTL

Minimal visual copy must **not** mean inaccessible controls, missing guidance, or silent status changes. Treat accessibility information as content even if it is not visibly rendered.

## Semantic and interaction requirements

- Prefer semantic controls (`button`, `label`, `input`, `fieldset`, `legend`, relevant headings) over click handlers on generic elements.
- Give every control a programmatically determinable **accessible name**. Icon-only buttons need a name that describes the action (`Show password`, `Hide password`, `Remove file`).
- Associate visible labels with input controls; placeholders are not stable accessible labels.
- Use descriptions only when they add a constraint or consequence; associate them using appropriate platform mechanisms (for web, e.g. `aria-describedby`).
- Ensure keyboard focus is visible, activation and dismissal work with keyboard, and hidden/disabled controls do not become traps.
- For dialogs, move focus to a suitable element, contain focus as required by the platform's modal semantics, and restore focus on dismissal where sensible.
- For validation, expose errors as text and associate them with fields. Do not rely on border color, icons, or toast-only feedback.
- Announce relevant async status, errors, and completion through platform-appropriate status semantics (for web, e.g. `role="status"` / `role="alert"` where appropriate). Avoid excessive live-region chatter.
- Never hide irreversible consequences only in a tooltip or inaccessible hover content.
- Check zoom, large type, text wrapping, contrast, target size, and responsive reflow; concise copy can still truncate.

## Persian writing guidance

Write natural Persian, not word-by-word translations of English. Choose consistent terms and verb forms suitable for the product's tone. Use Persian punctuation, spacing, and half-spaces deliberately (e.g., `می‌شود`, `نمی‌توانید`, `تأیید`). Prefer active, direct messages.

| Context | Natural Persian | Avoid |
| --- | --- | --- |
| Save | `ذخیره` / `تغییرات ذخیره شد.` | `عملیات ذخیره‌سازی با موفقیت به انجام رسید.` |
| Empty projects | `هنوز پروژه‌ای ندارید.` | `هیچ داده‌ای در دیتابیس یافت نشد.` |
| Invalid email | `ایمیل معتبر وارد کنید.` | `فرمت پارامتر ایمیل نامعتبر می‌باشد.` |
| Limit | `فقط فایل PDF تا ۱۰ مگابایت` | `فایل‌هایی با فرمت PDF و با حجم کمتر یا مساوی مقدار 10MB مجاز می‌باشند.` |
| Delete warning | `این کار قابل بازگشت نیست.` | `لطفاً به اطلاع داشته باشید که عملیات فوق برگشت‌ناپذیر است.` |
| Processing | `در حال پردازش…` | `در حال انجام پروسه پردازش اطلاعات در پس‌زمینه…` |
| Show password | `نمایش رمز عبور` | `کلیک کنید تا فیلد پسورد قابلیت مشاهده پیدا کند.` |
| Permission denied | `فقط مدیران می‌توانند این بخش را ویرایش کنند.` | `طبق Policy backend دسترسی ندارید.` |
| Required field | `نام پروژه را وارد کنید.` | `فیلد نام پروژه نمی‌تواند null باشد.` |
| Consent | `با انتخاب «موافقم»، اجازه می‌دهم اطلاعاتم برای [هدف مشخص] استفاده شود.` | `برای ادامه این گزینه را بزنید.` (بدون توضیح رضایت) |

## Bidi and mixed-script data

- Set page/element direction from the locale, not the language of the prompt. Use `dir="rtl"` for actual RTL contexts and `dir="auto"` for content whose direction varies.
- Isolate embedded Latin identifiers, email addresses, URLs, token-like *nonsecret* IDs, and code with suitable bidi isolation (`<bdi>`, `dir="ltr"`, or platform equivalents) so punctuation and ordering remain legible.
- Keep identifiers and technical codes intact. Avoid translating product codes or rewriting URLs.
- Use locale-aware number, date, time, and currency formatting. Do not assume all Persian interfaces must use one digit style; follow product and locale settings consistently.
- Do not hard-code punctuation/spacing around interpolated variables that can reorder in RTL; test with realistic mixed-script values.
- Support variable-length translations and meaningful plural forms (`۱ فایل`, `۲ فایل`) according to the localization framework.
- Keep accessible labels in the UI locale; a Persian icon-only control should have a Persian accessible name, even if the developer prompt was English.

## A practical HTML example

```html
<div dir="rtl" lang="fa">
  <label for="document">بارگذاری مدرک</label>
  <p id="file-rule">فقط فایل PDF تا ۱۰ مگابایت</p>
  <input id="document" type="file" accept="application/pdf"
         aria-describedby="file-rule" />
  <button type="button" aria-label="نمایش رمز عبور">…</button>
  <p role="status">در حال پردازش…</p>
  <p>شناسه: <bdi dir="ltr">INV-1042</bdi></p>
</div>
```

This is an **illustration** only: it does not implement file validation, password visibility, async behavior, or an integrated form. A label and focusable control must be wired to real behavior. Do not misrepresent snippets as tested components.

## Cross-language rule

A developer might write in Persian for an English-language application, or in English for a Persian application. **The product UI locale wins for user-facing text.** Keep implementation notes in the language best suited to the engineering team, but never render them as the UI's explanation.
