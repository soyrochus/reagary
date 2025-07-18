from __future__ import annotations

import re

from .protocols import HandlerProtocol, ParsedArtifact, NormalizedModel


class AngularJSFormHandler(HandlerProtocol):
    """Extracts AngularJS form field names."""

    field_pattern = re.compile(r"ng-model=\"([a-zA-Z0-9_\.]+)\"")

    def handle(self, artifact: ParsedArtifact) -> NormalizedModel:
        fields = self.field_pattern.findall(artifact.content)
        return NormalizedModel(fields=fields)

