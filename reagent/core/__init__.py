from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from ..protocols import (
    ParserProtocol,
    HandlerProtocol,
    ValidatorProtocol,
    NormalizedModel,
)


@dataclass
class REAgent:
    """Run the configured parser, handler and validator."""
    parser: ParserProtocol
    handler: HandlerProtocol
    validator: ValidatorProtocol

    def run_pipeline(self, path: Path) -> NormalizedModel:
        artifact = self.parser.parse(path)
        model = self.handler.handle(artifact)
        self.validator.validate(model)
        return model
