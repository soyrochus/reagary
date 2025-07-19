from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from . import NormalizedModel


@dataclass
class AngularTemplateModel:
    """Normalized representation of an AngularJS HTML template."""

    path: Path
    model: NormalizedModel


@dataclass
class AngularControllerModel:
    """Representation of an AngularJS controller file."""

    path: Path
    content: str


@dataclass
class AngularComponentModel:
    """Group of template and controller describing a component."""

    name: str
    template: AngularTemplateModel
    controller: AngularControllerModel | None = None
