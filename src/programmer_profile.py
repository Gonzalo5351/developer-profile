import json
from typing import List

class ProgrammerProfile:
    def __init__(self, profile_path: str):
        self.skills = self._load_skills(profile_path)

    def _load_skills(self, path: str) -> List[str]:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("skills", [])
