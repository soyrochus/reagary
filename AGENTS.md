# Prompt: REAgent Ingestion Engine POC (Python, Protocol-driven, Configurable)

**Context**
You are an advanced Python architect and developer. Build a Proof of Concept (POC) for the REAgent Ingestion Engine, demonstrating the complete ingestion pipeline from Parser through Validator. Your implementation must align with the provided high-level architecture, focus on separation of concerns, full configurability, and extensibility.

**Implementation constraints:**

* Programming language: **Python** (>=3.10)
* Base module/package: `reagent`
* Project management via **uv** (for dependencies and scripts)
* The POC must be executable via a CLI runner, but core logic (everything in `reagent/`) must be entirely decoupled from CLI or web interface code.
* All critical component boundaries must be defined using clear, well-documented Python **Protocols** (PEP 544 or `typing_extensions.Protocol`).
* All configuration (pipeline composition, schemas, etc.) is loaded via a separate `reagent_config` module—no hardcoded paths or parameters in the core.
* Data objects exchanged between components must be Python dataclasses or Pydantic models.

---

**Scope and Workflow:**
Your POC must implement the following pipeline (see architecture and sequence diagrams in the reference PDFs):

1. **Ingestion Controller**

   * The orchestrator. Accepts an input path and configuration object, initializes the pipeline, and executes it. All dependencies are resolved via `CONFIG`.

2. **Parser**

   * Converts source code (for POC: AngularJS JS+HTML form artifact) into a technology-specific partial data tree (AST or similar).
   * Must use a clearly defined `ParserProtocol`.

3. **Handler**

   * Receives the parsed data tree and maps it to a normalized, technology-agnostic model (e.g., SES: Schema-Entity-State).
   * Must use a configurable schema/ontology loaded from config.
   * Protocol: `HandlerProtocol`.

4. **Validator**

   * Checks the normalized model against the configured schema/ontology and business rules.
   * Produces a structured report (errors, warnings, suggestions).
   * Protocol: `ValidatorProtocol` and `ValidationReportProtocol`.

5. **Applier** (optional in POC)

   * Would apply the validated model to a mock/in-memory model repository. For POC, just provide the interface.

6. **Artifacts and Data Flow**

   * All outputs at each stage (parsed tree, model, validation report) must be inspectable and serializable.

---

**Technical Requirements:**

* Package: `reagent`
* Configuration: `reagent_config` (singleton CONFIG object, loaded at process start)
* No hardcoded paths or parameters in the library—everything is parameterized or injected.
* All protocols/interfaces documented with Python docstrings.
* Well-typed: use type hints everywhere; prefer dataclasses/Pydantic for models.
* Tests: include a working pipeline test and minimal AngularJS sample artifact.
* CLI runner: `/cli_runner.py` (only invokes core code, no logic inside).
* Readme with installation, architecture, and usage.

---

**Project Structure Example:**

```
reagent/
  __init__.py
  core.py           # Controller & pipeline orchestrator
  parser.py         # Parser(s) & protocol
  handler.py        # Handler(s) & protocol
  validator.py      # Validator(s) & protocol
  applier.py        # Applier (optional for POC)
  models.py         # Dataclasses/Pydantic schemas
  protocols.py      # Protocol definitions
  utils.py
reagent_config/
  __init__.py       # CONFIG loader (YAML/env)
tests/
  test_pipeline.py  # E2E test
  sample_angularjs_form.js
  sample_angularjs_form.html
cli_runner.py
README.md
pyproject.toml
```

---

**Acceptance Criteria:**

* The POC ingests a minimal AngularJS artifact, parses and normalizes it, validates the result, and emits a validation report (no storage, no interface logic in core).
* All component interfaces are clear, well-documented, and testable.
* Configuration is external (YAML/JSON, env), never hardcoded in core code.
* Tests must run and pass with `pytest`.
* Code is idiomatic Python, extensible for additional technologies.

---

**Example Usage:**

```python
from reagent import REAgent
from reagent_config import CONFIG
from pathlib import Path

model = REAgent(CONFIG).run_pipeline(Path("tests/sample_angularjs_form.js"))
report = model.validation_report
print(report.to_json())
```

---

**Your deliverable should fully realize these architectural, interface, and modularity principles, enabling future extension and integration as specified in the reference documents.**
