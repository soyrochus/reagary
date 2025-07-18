from __future__ import annotations

from .protocols import ApplierProtocol, NormalizedModel


class InMemoryApplier(ApplierProtocol):
    """No-op applier used for demonstration."""

    def __init__(self) -> None:
        self.applied: list[NormalizedModel] = []

    def apply(self, model: NormalizedModel) -> None:
        self.applied.append(model)
