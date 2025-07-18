from pathlib import Path

from reagent import REAgent
from reagent_config import CONFIG


def main(path: str) -> None:
    agent = REAgent(CONFIG.parser, CONFIG.handler, CONFIG.validator)
    model = agent.run_pipeline(Path(path))
    if model.validation_report:
        print(model.validation_report.to_json())


if __name__ == "__main__":
    import sys

    main(sys.argv[1])
