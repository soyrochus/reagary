from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml

from reagent.protocols import ParserProtocol, HandlerProtocol, ValidatorProtocol
from reagent.utils import load_object


@dataclass
class Config:
    parser: ParserProtocol
    handler: HandlerProtocol
    validator: ValidatorProtocol


def _load_from_yaml(path: Path) -> Config:
    data = yaml.safe_load(path.read_text())
    parser_cls = load_object(data["parser"])
    handler_cls = load_object(data["handler"])
    validator_cls = load_object(data["validator"])
    return Config(parser=parser_cls(), handler=handler_cls(), validator=validator_cls())


CONFIG_PATH = Path(os.environ.get("REAGENT_CONFIG_PATH", Path(__file__).with_name("config.yaml")))
CONFIG = _load_from_yaml(CONFIG_PATH)
