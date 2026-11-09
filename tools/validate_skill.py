#!/usr/bin/env python3
"""Validate the structure and linked local reference files of this Agent Skill."""

from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: python -m pip install 'PyYAML>=6,<7'")

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "mandatory-software-testing"
SKILL_MD = SKILL_DIR / "SKILL.md"
ERRORS = []


def check(condition, message):
    if not condition:
        ERRORS.append(message)


def check_links(path):
    body = path.read_text(encoding="utf-8")
    for destination in re.findall(r"\]\(([^)]+)\)", body):
        if destination.startswith(("https://", "http://", "mailto:", "#")):
            continue
        pathname = destination.split("#", 1)[0]
        pathname = pathname.split("?", 1)[0]
        if pathname and not (path.parent / pathname).exists():
            ERRORS.append(f"Broken link in {path.relative_to(ROOT)}: {destination}")


def main():
    check(SKILL_MD.is_file(), "Missing skills/mandatory-software-testing/SKILL.md")
    if not SKILL_MD.is_file():
        return 1
    source = SKILL_MD.read_text(encoding="utf-8")
    header = re.match(r"\A---\s*\n(.*?)\n---\s*\n", source, re.DOTALL)
    check(header is not None, "SKILL.md must begin with YAML frontmatter")
    if header is None:
        return 1
    try:
        metadata = yaml.safe_load(header.group(1))
    except yaml.YAMLError as error:
        ERRORS.append(f"YAML frontmatter is invalid: {error}")
        return 1
    check(isinstance(metadata, dict), "Frontmatter must be a YAML object")
    if not isinstance(metadata, dict):
        return 1
    name = metadata.get("name")
    description = metadata.get("description")
    check(name == SKILL_DIR.name, "Frontmatter name must match skill directory")
    check(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)) and len(name) <= 64,
          "Invalid name: use 1–64 lowercase characters, digits and hyphens")
    check(isinstance(description, str) and 1 <= len(description) <= 1024,
          "description must be a non-empty string of up to 1024 characters")
    for field, limit in (("compatibility", 500),):
        val = metadata.get(field)
        check(val is None or (isinstance(val, str) and len(val) <= limit), f"Invalid {field} field")
    if "metadata" in metadata:
        extra = metadata["metadata"]
        check(isinstance(extra, dict) and all(isinstance(k, str) and isinstance(v, str) for k, v in extra.items()),
              "metadata must be a string-to-string mapping")
    check(bool(source[header.end():].strip()), "SKILL.md must contain instructions after the metadata")

    refs = SKILL_DIR / "references"
    check(refs.is_dir(), "Missing references/ directory")
    expected = ["00-agent-contract.md", "TEST-DEPENDENCY-MATRIX.md"]
    expected += [
        "01-unit-testing.md", "02-integration-testing.md", "03-system-testing.md",
        "04-end-to-end-testing.md", "05-acceptance-testing.md", "06-smoke-testing.md",
        "07-sanity-testing.md", "08-regression-testing.md", "09-performance-testing.md",
        "10-load-testing.md", "11-stress-testing.md", "12-security-testing.md",
        "13-usability-testing.md", "14-compatibility-testing.md", "15-exploratory-testing.md",
        "16-alpha-beta-testing.md",
    ]
    for name in expected:
        check((refs / name).is_file(), f"Missing reference: {name}")
    check((SKILL_DIR / "agents" / "openai.yaml").is_file(), "Missing optional interface metadata used by this repository")
    for md_file in ROOT.rglob("*.md"):
        check_links(md_file)
    if ERRORS:
        print("Validation FAILED:")
        for error in ERRORS:
            print(f" - {error}")
        return 1
    print(f"Validation PASSED: {SKILL_DIR.relative_to(ROOT)}")
    print(f"References: {len(list(refs.glob('*.md')))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
