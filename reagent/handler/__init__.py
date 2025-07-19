from __future__ import annotations

import re

from ..protocols import HandlerProtocol, ParsedArtifact, NormalizedModel


class AngularJSFormHandler(HandlerProtocol):
    """Extracts AngularJS form field names."""

    field_pattern = re.compile(r"ng-model=\"([a-zA-Z0-9_\.]+)\"")

    def handle(self, artifact: ParsedArtifact) -> NormalizedModel:
        """Produce a :class:`NormalizedModel` from ``artifact``.

        Parameters
        ----------
        artifact: ParsedArtifact
            Parsed HTML template.

        Returns
        -------
        NormalizedModel
            Model containing any ``ng-model`` field names.
        """

        fields = self.field_pattern.findall(artifact.content)
        return NormalizedModel(fields=fields)

