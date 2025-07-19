from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List

from ..protocols import (
    HandlerProtocol,
    ParserProtocol,
    ValidatorProtocol,
)
from ..models import (
    AngularComponentModel,
    AngularControllerModel,
    AngularTemplateModel,
)


@dataclass
class ResourceBundle:
    """Collection of files representing an AngularJS component."""

    template: Path
    controller: Path | None = None


class ParserAction:
    """Parse a directory of AngularJS resources into component models."""

    def __init__(
        self,
        parser: ParserProtocol,
        handler: HandlerProtocol,
        validator: ValidatorProtocol,
    ) -> None:
        self.parser = parser
        self.handler = handler
        self.validator = validator

    def parse_directory(self, directory: Path) -> List[AngularComponentModel]:
        """Parse ``directory`` and return component models."""

        components: List[AngularComponentModel] = []
        for html_file in directory.glob("*.html"):
            js_file = html_file.with_suffix(".js")
            bundle = ResourceBundle(
                template=html_file, controller=js_file if js_file.exists() else None
            )
            artifact = self.parser.parse(bundle.template)
            model = self.handler.handle(artifact)
            self.validator.validate(model)
            template_model = AngularTemplateModel(path=bundle.template, model=model)
            controller_model = None
            if bundle.controller:
                controller_model = AngularControllerModel(
                    path=bundle.controller, content=bundle.controller.read_text()
                )
            components.append(
                AngularComponentModel(
                    name=html_file.stem,
                    template=template_model,
                    controller=controller_model,
                )
            )
        return components
