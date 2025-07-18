from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, runtime_checkable, List


@dataclass
class ParsedArtifact:
    """Output of the Parser step."""

    source_path: Path
    content: str


@dataclass
class NormalizedModel:
    """Technology-agnostic representation produced by Handler."""

    fields: List[str]
    validation_report: "ValidationReportProtocol | None" = None


@dataclass
class ValidationMessage:
    level: str
    message: str


@runtime_checkable
class ParserProtocol(Protocol):
    """Parser that converts a source artifact to a ParsedArtifact."""

    def parse(self, path: Path) -> ParsedArtifact:
        ...


@runtime_checkable
class HandlerProtocol(Protocol):
    """Handler that normalizes the parsed artifact."""

    def handle(self, artifact: ParsedArtifact) -> NormalizedModel:
        ...


@runtime_checkable
class ValidationReportProtocol(Protocol):
    """Report returned by a Validator."""

    messages: List[ValidationMessage]

    def is_valid(self) -> bool:
        ...

    def to_json(self) -> str:
        ...


@runtime_checkable
class ValidatorProtocol(Protocol):
    """Validator that checks a NormalizedModel."""

    def validate(self, model: NormalizedModel) -> ValidationReportProtocol:
        ...


@runtime_checkable
class ApplierProtocol(Protocol):
    """Optional application step."""

    def apply(self, model: NormalizedModel) -> None:
        ...
