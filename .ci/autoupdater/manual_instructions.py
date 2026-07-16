"""
Manual Instructions & Override Directives Manager for Google Fonts Auto-Updater.
Located internally within google/fonts at .ci/autoupdater/manual_instructions.py.
"""

import json
import re
from pathlib import Path
from typing import Optional, Set, Dict, Any

DEFAULT_INSTRUCTIONS_PATH = Path(__file__).parent / "manual_instructions.json"


def normalize_family_slug(name: str) -> str:
    """Normalize family name string into lowercase alphanumeric slug."""
    if not name:
        return ""
    return re.sub(r'[^a-zA-Z0-9]', '', name.lower())


class ManualInstructions:
    """
    Manages manual directives for the autoupdater:
    1) variable_updates: List of font families transitioning from static to variable.
       Existing static fonts should be removed and replaced with the new variable version.
    2) approved_for_update: List of font families reviewed and evaluated by a human to be safe to update.
    """

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or DEFAULT_INSTRUCTIONS_PATH
        self.variable_updates: Set[str] = set()
        self.approved_for_update: Set[str] = set()
        self.load()

    def load(self) -> None:
        if not self.config_path.exists():
            self.save_default()
            return
        try:
            data = json.loads(self.config_path.read_text(encoding="utf-8"))
            self.variable_updates = set(normalize_family_slug(s) for s in data.get("variable_updates", []))
            self.approved_for_update = set(normalize_family_slug(s) for s in data.get("approved_for_update", []))
        except Exception:
            pass

    def save_default(self) -> None:
        default_data = {
            "description": "Manual instructions and override directives for Google Fonts Auto-Updater",
            "variable_updates": [
                "abhayalibre",
                "cascadiacode"
            ],
            "approved_for_update": [
                "inter",
                "roboto"
            ]
        }
        self.config_path.parent.mkdir(parents=True, exist_ok=True)
        self.config_path.write_text(json.dumps(default_data, indent=2), encoding="utf-8")
        self.variable_updates = set(normalize_family_slug(s) for s in default_data["variable_updates"])
        self.approved_for_update = set(normalize_family_slug(s) for s in default_data["approved_for_update"])

    def is_variable_update_approved(self, family_name: str) -> bool:
        return normalize_family_slug(family_name) in self.variable_updates

    def is_human_approved(self, family_name: str) -> bool:
        return normalize_family_slug(family_name) in self.approved_for_update

    def get_family_directives(self, family_name: str) -> Dict[str, bool]:
        return {
            "is_variable_update": self.is_variable_update_approved(family_name),
            "is_human_approved": self.is_human_approved(family_name),
        }
