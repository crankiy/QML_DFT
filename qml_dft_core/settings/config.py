from __future__ import annotations

from configparser import ConfigParser
from pathlib import Path
from typing import Iterable
import json


def _resolve_orbital_spec(config: ConfigParser, project_root: Path) -> None:
    if config.has_option("dataset", "orbital_spec_file"):
        orbital_file = Path(config.get("dataset", "orbital_spec_file")).expanduser()
        if not orbital_file.is_absolute():
            orbital_file = project_root / orbital_file
        orbital_payload = json.loads(orbital_file.read_text())
        config.set("dataset", "orbital_spec", json.dumps(orbital_payload))
    elif config.has_option("dataset", "orbital_spec"):
        return
    else:
        raise ValueError("Missing orbital specification: use [dataset] orbital_spec_file or [dataset] orbital_spec")


def _validate_sections(config: ConfigParser) -> None:
    required_sections = ["paths", "dataset", "task", "runtime", "optimizer", "split", "model"]
    missing = [section for section in required_sections if not config.has_section(section)]
    if missing:
        raise ValueError(f"Missing required config sections: {', '.join(missing)}")



