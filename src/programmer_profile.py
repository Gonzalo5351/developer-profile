import json
from typing import List, Dict


class ProgrammerProfile:
    def __init__(self, profile_path: str):
        self.path = profile_path
        with open(self.path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def nombre(self) -> str:
        return self.data.get("nombre", "")

    def resumen(self) -> List[str]:
        return self.data.get("resumen", [])

    def skills_con_nivel(self) -> List[Dict[str, str]]:
        return self.data.get("skills", [])

    def skills_nombres(self) -> List[str]:
        return [skill["nombre"] for skill in self.skills_con_nivel()]

    def tags(self) -> List[str]:
        return self.data.get("tags", [])

    def valores(self) -> List[str]:
        return self.data.get("valores", [])

    def github(self) -> str:
        return self.data.get("links", {}).get("github", "")

    def linkedin(self) -> str:
        return self.data.get("links", {}).get("linkedin", "")

    def portafolio_web(self) -> str:
        return self.data.get("links", {}).get("portafolio_web", "")

    def links_destacados(self) -> List[str]:
        return self.data.get("links", {}).get("repositorios_destacados", [])

    def objetivos(self) -> List[str]:
        return self.data.get("objetivos", [])

