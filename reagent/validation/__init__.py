from __future__ import annotations

import json
from dataclasses import dataclass
from typing import List

from ..protocols import (
    ValidatorProtocol,
    ValidationReportProtocol,
    ValidationMessage,
    NormalizedModel,
)


@dataclass
class ValidationReport(ValidationReportProtocol):
    messages: List[ValidationMessage]

    def is_valid(self) -> bool:
        return not [m for m in self.messages if m.level == "error"]

    def to_json(self) -> str:
        return json.dumps([m.__dict__ for m in self.messages])


class SimpleValidator(ValidatorProtocol):
    """Validates that at least one field exists."""

    def validate(self, model: NormalizedModel) -> ValidationReportProtocol:
        messages: List[ValidationMessage] = []
        if not model.fields:
            messages.append(ValidationMessage(level="error", message="No fields detected"))
        else:
            messages.append(ValidationMessage(level="info", message=f"Detected {len(model.fields)} fields"))
        report = ValidationReport(messages)
        model.validation_report = report
        return report

