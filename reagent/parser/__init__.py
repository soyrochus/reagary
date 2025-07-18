from __future__ import annotations

from pathlib import Path

from ..protocols import ParserProtocol, ParsedArtifact


class AngularJSParser(ParserProtocol):
    """Very small parser that reads an AngularJS artifact."""

    def parse(self, path: Path) -> ParsedArtifact:
        text = path.read_text()
        return ParsedArtifact(source_path=path, content=text)

