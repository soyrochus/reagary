"""Re-export commonly used models for convenience."""

from ..protocols import ParsedArtifact, NormalizedModel, ValidationMessage
from .angular import (
    AngularComponentModel,
    AngularControllerModel,
    AngularTemplateModel,
)

__all__ = [
    "ParsedArtifact",
    "NormalizedModel",
    "ValidationMessage",
    "AngularTemplateModel",
    "AngularControllerModel",
    "AngularComponentModel",
]

