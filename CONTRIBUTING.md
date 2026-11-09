# Contributing

Thanks for helping improve UI Content Guard. Contributions should keep the skill portable, precise, and useful in real projects.

## Workflow

1. Open a focused issue or discussion for a behavior change, or submit a small documentation correction directly.
2. Create a topic branch and keep the change limited to one concern.
3. Update the relevant `references/` page first; change `SKILL.md` only when the agent's core decision process changes.
4. Add a realistic negative/positive example when introducing a new rule or exception.
5. Run `python3 scripts/validate.py` from the project root and review the relevant acceptance cases in `tests/acceptance-cases.md`.
6. Submit a pull request describing the problem, proposed fix, tradeoffs, and tests actually performed.

## Documentation standards

- Write precise English documentation; preserve natural localized examples in their respective language.
- Distinguish instruction, implementation behavior, and visible UI copy. Avoid claims about integrations or tools not required by the open format.
- Prefer concise, actionable language. Do not duplicate large sections across files; link to existing references.
- Every new Markdown link must resolve within the package or point to a real external resource.
- Do not add external runtime dependencies for editorial rules or simple string processing.

## Example submission rules

Every full scenario should contain **Developer instruction → Incorrect UI → Correct UI → Correct implementation behavior**. Use realistic constraints, account for error and accessibility states, and explain when *not* to remove text. Any personal or security-relevant data must be synthetic.

## Pull request expectations

Explain: (1) observed failure mode, (2) severity/user impact, (3) new behavior, (4) affected locales, (5) regression risk, (6) validation results, and (7) known limits. Do not claim manual or compatibility testing if it was not carried out.

## Quality bar

A change is acceptable when it preserves essential disclosures and access needs, uses consistent terminology, respects existing design systems, and offers implementable guidance rather than generic slogans. Maintainers may request an additional counterexample when a rule risks over-minimizing important copy.

## Code of conduct

Discuss ideas respectfully, focus criticism on observable behavior, and do not post private data or exploit details in public threads.
