from pathlib import Path
import shutil
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from reagent.parser import ParserAction
from reagent import REAgent
from reagent_config import CONFIG

SAMPLE_HTML = Path(__file__).with_name("sample_angularjs_form.html")
SAMPLE_JS = Path(__file__).with_name("sample_angularjs_form.js")


def test_parser_action(tmp_path: Path) -> None:
    target_dir = tmp_path / "comp"
    target_dir.mkdir()
    shutil.copy(SAMPLE_HTML, target_dir / SAMPLE_HTML.name)
    shutil.copy(SAMPLE_JS, target_dir / SAMPLE_JS.name)

    agent = REAgent(CONFIG.parser, CONFIG.handler, CONFIG.validator)
    action = ParserAction(agent.parser, agent.handler, agent.validator)
    components = action.parse_directory(target_dir)
    assert len(components) == 1
    component = components[0]
    assert component.template.model.fields == ["user.name", "user.email"]
    assert component.controller is not None


