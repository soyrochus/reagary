# AGENTS.md

## Purpose

This file defines repository-wide and directory-specific coding, testing, and documentation policies. All automated code generation agents (including OpenAI Codex) must adhere to these rules unless explicitly overridden by user instruction.

---

## 1. Code Style & Structure

- All code must conform to [Black](https://black.readthedocs.io/) (Python) / [Prettier](https://prettier.io/) (JS/TS) formatting.
- Variable, function, and class names must be descriptive and use snake_case (Python) or camelCase (JS/TS).
- No magic numbers: all constants must be named.
- Functions should be pure unless stateful logic is required.
- All public funtions/methods/entities should be typed
- Use Pydantic for data withruntime validation, serialization, or more advanced features.
- Use @dataclass for simple, lightweight containers.

---

## 2. Service Architecture


---

## 3. Testing & Validation

- All new and modified code must include corresponding unit tests (pytest).
- Run `pytest tests/` (Python) before submitting PRs.
- Run mypy before submitting PRs.
- PRs must not reduce code coverage (check with `pytest --cov` or equivalent).

---

## 4. Documentation

- Each public function, class, and API endpoint must have a docstring or JSDoc comment.


---

## 5. PR/Commit Policy

- PR title must be descriptive and follow the pattern: `[Type] Brief description`
- Include a "Testing Done" section in PR body, describing validation steps performed.
- Do not commit commented-out code or unused variables.

---

## 6. Linting/CI/Type checking

- All code must pass static analysis using `ruff` (Python).
- Type checking must be performed using mypy
- Automated CI checks defined in `.github/workflows/ci.yml` must pass before merging.

---

## 7. Security

- Never commit credentials, secrets, or API keys.
- All external input must be validated and sanitized.

---

## 8. Directory-specific Rules

<!-- Place additional rules for submodules/services here as needed -->
# Example:
# /services/auth:
# - Use OAuth2 for authentication.
# - All endpoints require JWT validation.
- all modules in the /reagent directory, implementing "reagent" as a root module
- do not use a "src" root
- tests in the /test directory

---

## 9. Exceptions

If a particular generation request requires deviation from these standards, user/system instructions take precedence and should state the exception explicitly.

---

# End of AGENTS.md
