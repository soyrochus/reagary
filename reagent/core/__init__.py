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
        """Run the full ingestion pipeline on ``path``.

        Parameters
        ----------
        path: Path
            Location of the source artifact to parse.

        Returns
        -------
        NormalizedModel
            The validated model produced from ``path``.
        """

        artifact = self.parser.parse(path)
        model = self.handler.handle(artifact)
        self.validator.validate(model)
        return model
