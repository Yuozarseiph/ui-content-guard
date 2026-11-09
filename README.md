# UI Content Guard

**Agent-agnostic UX writing and UI content review skill** · v1.0.0 · MIT

UI Content Guard helps AI-assisted software workflows separate developer instructions and implementation details from intentional, necessary user-facing copy. It targets a common failure mode: a developer asks for behavior, and the generated UI displays the developer's explanation instead of implementing it cleanly.

> Implement what the developer explains. Do not display the developer's explanation to the end user.

## Why it exists

Developer notes such as “these two filters operate independently” are requirements about behavior, **not necessarily text for an interface**. Repeating them under controls increases visual noise and can obscure important warnings. Conversely, deleting every helper or disclosure can make a product unsafe or inaccessible. UI Content Guard makes that distinction explicit.

## Features

- Classification of five content types: developer instructions, product requirements, implementation details, UI copy, and technical documentation.
- A necessity test that retains safety, privacy, consent, financial, accessibility, and validation information.
- Practical patterns for fields, dialogs, statuses, dashboards, permissions, uploads, and onboarding.
- Review guidance for full interactions, not only strings in isolation.
- Persian/RTL and multilingual guidance with real microcopy examples.
- Severity-based content audits with concrete remediation.
- Progressive reference material, implementation checklists, and deterministic repository validation.

## Before / after

**Developer request:** “Date and time filters are optional and must work independently.”

**Before (wrong UI):**
> Date and time are optional and work independently. You can use one, both, or neither.

**After (correct UI):**
- `Date` — date control
- `Time` — time control

**Required implementation:** all four valid combinations work, no field is implicitly required, and clear selection works independently. Add guidance only if actual use shows ambiguity.

**Developer request:** “Deletion cannot be undone.”

**Wrong reaction:** Delete the explanatory text and leave an ambiguous button.

**Correct UI:** `Delete workspace` with a confirmation that says “Delete this workspace and its files? This can't be undone.” The confirmation remains essential.

For additional realistic cases see [bad UI](examples/bad-ui-examples.md), [improved UI](examples/improved-ui-examples.md), and [instruction-to-implementation](examples/developer-instruction-examples.md).

## Installation: any compatible host

1. Extract the archive. Its root contains the `ui-content-guard/` directory.
2. Place the **entire directory** in a skills location supported by your AI agent or automation environment (consult that host's current documentation).
3. Ensure the host discovers `ui-content-guard/SKILL.md`; retain the `references/` and `examples/` folders so linked guidance remains available.
4. Ask the host to use **UI Content Guard** when implementing or auditing UI. Hosts supporting skill discovery may activate it automatically based on its `description`; invocation syntax varies.

The core `SKILL.md` follows the [open Agent Skills specification](https://agentskills.io/specification). No SDK, network service, framework, or proprietary feature is required. **Compatibility depends on whether a particular host supports the open format and local skill discovery.** This project does not guarantee integration with every agent product.

### Optional installation examples

The following are **host-specific paths**, not host-specific instructions inside the skill:

| Host | Repository installation | User-level installation |
| --- | --- | --- |
| Codex (current local skill locations) | `<repo>/.agents/skills/ui-content-guard/` | `~/.agents/skills/ui-content-guard/` |
| Claude Code (manual local folder) | `<repo>/.claude/skills/ui-content-guard/` | `~/.claude/skills/ui-content-guard/` |

For example, after extracting the ZIP from the repository root:

```sh
mkdir -p .agents/skills
cp -R ui-content-guard .agents/skills/ui-content-guard
```

For user-level Codex installation:

```sh
mkdir -p "$HOME/.agents/skills"
cp -R ui-content-guard "$HOME/.agents/skills/ui-content-guard"
```

Other compatible agents may use different discovery paths. Consult their documentation rather than assuming the examples above are universal. `agents/openai.yaml` is **optional presentation metadata only** for hosts that recognize it; it adds no behavior, tools, or dependencies to the portable skill.

## Usage

Example natural-language tasks (no proprietary command syntax required):

- “Apply UI Content Guard to the settings form and remove redundant helper text while retaining validation and consent.”
- “Audit this dashboard for implementation details accidentally exposed as UI copy.”
- “Improve the Persian microcopy for these permission and upload states; preserve RTL and accessibility.”
- “Implement independent optional date and time filters without a paragraph describing the engineering logic.”

A useful review output identifies **location, issue, severity, proposed fix, behavior check**, and any evidence gaps. For code changes, preserve design-system patterns and report only validations actually run.

## How the skill operates

1. Inspect interface conventions and required behavior.
2. Classify developer instructions vs. product policy vs. UI copy.
3. Apply the content necessity test.
4. Write or change the minimal *sufficient* copy and implement behavior.
5. Audit accessibility, localization, failure states, and consequential actions.
6. Verify against the acceptance cases and explain remaining uncertainty.

## Project structure

```text
ui-content-guard/
├── SKILL.md                      # Portable instruction entry point
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CHANGELOG.md
├── SECURITY.md
├── .gitignore
├── agents/openai.yaml            # Optional host-specific display metadata
├── references/                  # Load-on-demand guidance
│   ├── content-boundaries.md
│   ├── ux-writing-rules.md
│   ├── examples-and-patterns.md
│   ├── accessibility-and-localization.md
│   ├── content-audit.md
│   ├── form-and-interaction-copy.md
│   ├── error-and-feedback-messages.md
│   └── design-system-consistency.md
├── examples/                    # Before/after implementation scenarios
│   ├── README.md
│   ├── bad-ui-examples.md
│   ├── improved-ui-examples.md
│   └── developer-instruction-examples.md
├── scripts/validate.py          # Optional stdlib-only repository checks
└── tests/
    ├── acceptance-cases.md       # Prompt-based review cases
    └── test_skill.py             # Validator regression tests
```

## Validation

From the skill directory:

```sh
python3 scripts/validate.py
```

The included checker examines core metadata, naming, internal Markdown links, document presence, license markers, and acceptance-case coverage. **It does not evaluate language-model reasoning or guarantee correct runtime outputs.** Use the [acceptance cases](tests/acceptance-cases.md) for qualitative evaluation in any chosen compatible host. The checker is a contributor convenience, not a dependency for using the skill.

## Supported agents and portability

The project targets **the open Agent Skills directory format**, not one AI vendor. It can be supplied to any tool that supports that format, but activation, routing, and tool-access policies are controlled by each host. No agent-specific invocation or proprietary API appears in the main skill instructions. Optional metadata is isolated under `agents/`.

## Limitations

- The skill is guidance, not an automatic runtime UI sanitizer, translation engine, or accessibility certification.
- A language model can still misclassify content; critical policy and risk disclosures require product/legal review when appropriate.
- Full audits need access to real components, states, translations, and behavior. Text-only reviews have narrower evidence.
- Host-specific compatibility and model-quality tests must be run in those hosts; repository validation alone cannot establish them.

## Contributing and licensing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the process, [SECURITY.md](SECURITY.md) for private vulnerability reports, and [CHANGELOG.md](CHANGELOG.md) for release history. Licensed under the [MIT License](LICENSE), © 2026 UI Content Guard Contributors.
