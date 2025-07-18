from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from reagent import REAgent
from reagent_config import CONFIG


SAMPLE_HTML = Path(__file__).with_name("sample_angularjs_form.html")


def test_pipeline(tmp_path):
    agent = REAgent(CONFIG.parser, CONFIG.handler, CONFIG.validator)
    model = agent.run_pipeline(SAMPLE_HTML)
    assert model.validation_report is not None
    assert model.validation_report.is_valid()
    assert model.fields
