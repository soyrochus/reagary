from __future__ import annotations

from pathlib import Path

from ..protocols import ParserProtocol, ParsedArtifact
from .actions import ParserAction, ResourceBundle

__all__ = ["AngularJSParser", "ParserAction", "ResourceBundle"]


class AngularJSParser(ParserProtocol):
    """Very small parser that reads an AngularJS artifact."""

    def parse(self, path: Path) -> ParsedArtifact:
        """Parse ``path`` into a :class:`ParsedArtifact`.

        Parameters
        ----------
        path: Path
            File to load.

        Returns
        -------
        ParsedArtifact
            Representation of ``path`` and its textual content.
        """

        text = path.read_text()
        return ParsedArtifact(source_path=path, content=text)

