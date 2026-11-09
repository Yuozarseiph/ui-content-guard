# Complete file manifest — v1.0.0

The ZIP root is **`ui-content-guard/`**. Extract into the target skills directory; preserve the full folder hierarchy. The archive includes all paths listed below.

```text
ui-content-guard/
  .gitignore
  CHANGELOG.md
  CONTRIBUTING.md
  LICENSE
  MANIFEST.md
  README.md
  SECURITY.md
  SKILL.md
  VALIDATION.md
  agents/openai.yaml
  examples/README.md
  examples/bad-ui-examples.md
  examples/developer-instruction-examples.md
  examples/improved-ui-examples.md
  references/accessibility-and-localization.md
  references/content-audit.md
  references/content-boundaries.md
  references/design-system-consistency.md
  references/error-and-feedback-messages.md
  references/examples-and-patterns.md
  references/form-and-interaction-copy.md
  references/ux-writing-rules.md
  scripts/validate.py
  tests/acceptance-cases.md
  tests/test_skill.py
```

**File count:** 25. `SKILL.md` is the only required entry point for the open format; all other project files provide optional documentation, examples, verification, or host display metadata.

**Agent neutrality:** `SKILL.md` contains no agent-specific commands or integrations. `agents/openai.yaml` is optional presentation metadata for compatible hosts and is not necessary to use the skill.
