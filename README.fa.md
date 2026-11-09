# مهارت تست نرم‌افزار — نسخه قابل انتشار در GitHub

این مخزن شامل یک **Agent Skill استاندارد** برای برنامه‌ریزی و اجرای تست‌های مجاز نرم‌افزار و تهیه گزارش مبتنی بر شواهد است. نقطه ورود Skill:

```text
skills/mandatory-software-testing/SKILL.md
```

## انتشار در GitHub

۱. یک Repository با نام پیشنهادی `mandatory-software-testing` بسازید.
۲. ZIP را استخراج کنید و **محتویات آن** را در ریشه Repository قرار دهید. ZIP را به‌جای فایل‌ها آپلود نکنید.
۳. همه مسیرها را دقیقاً حفظ کنید؛ مخصوصاً `skills/mandatory-software-testing/references/` و `.github/workflows/`.
۴. قبل از انتشار عمومی، مجوز انتشار موردنظر خود را انتخاب کرده و فایل `LICENSE` مناسب را اضافه کنید.

## نصب از روی GitHub

به‌جای `YOUR_USERNAME` نام کاربری یا سازمان GitHub را بنویسید. این دستورات به نسخه جدید GitHub CLI که `gh skill` دارد نیاز دارند.

**Codex (داخل پروژه):**

```bash
gh skill install YOUR_USERNAME/mandatory-software-testing mandatory-software-testing --agent codex --scope project
```

**GitHub Copilot (داخل پروژه):**

```bash
gh skill install YOUR_USERNAME/mandatory-software-testing mandatory-software-testing --agent github-copilot --scope project
```

روش دستی: پوشه کامل `skills/mandatory-software-testing/` را برای Codex در مسیر `.agents/skills/mandatory-software-testing/` یا برای Copilot در مسیر `.github/skills/mandatory-software-testing/` کپی کنید.

## نکات کلیدی

- ۱۶ دسته تست با مستندات جداگانه و ماتریس وابستگی‌ها موجودند.
- **Skill به‌تنهایی ابزار تست یا CI نیست** و اجرای موفق تست‌ها باید با شواهد واقعی اثبات شود.
- برای عملیات حساس، مخرب، اسکن‌های امنیتی فعال و دسترسی به محیط عملیاتی، تأیید صریح لازم است.
- نتایج شکست‌خورده یا ناپایدار نباید بدون شواهد معتبر `PASS` گزارش شوند.
- نصب Skill به معنی اجرای اجباری آن روی هر تغییر نیست؛ در صورت نیاز، سیاست CI/Repository جداگانه تعریف کنید.

برای توضیحات انگلیسی، [README.md](README.md) را ببینید.
