from importlib import import_module
from typing import Any


def load_object(path: str) -> Any:
    """Load a Python object from a dotted path."""
    module_path, attr = path.rsplit('.', 1)
    module = import_module(module_path)
    return getattr(module, attr)
