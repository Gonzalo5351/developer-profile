import json
from typing import List

class ProgrammerProfile:
    def __init__(self, profile_path: str):
        self.path = profile_path
        self.skills = self._load_skills()

    def _load_skills(self) -> List[str]:
        with open(self.path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("skills", [])