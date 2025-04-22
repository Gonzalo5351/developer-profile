import unittest
import os
import json
from src.programmer_profile import ProgrammerProfile


class TestProgrammerProfile(unittest.TestCase):
    def setUp(self):
        # Crea un archivo temporal con contenido de prueba
        self.test_profile_path = "tests/test_profile.json"
        self.sample_data = {
            "nombre": "Gonzalo",
            "resumen": ["Programador Python.", "Foco en scraping."],
            "skills": [
                {"nombre": "Python", "nivel": "intermedio"},
                {"nombre": "Git", "nivel": "básico"},
            ],
            "links": {"github": "https://github.com/gonza"},
        }
        with open(self.test_profile_path, "w", encoding="utf-8") as f:
            json.dump(self.sample_data, f, indent=2)

        self.profile = ProgrammerProfile(self.test_profile_path)

    def tearDown(self):
        os.remove(self.test_profile_path)

    def test_nombre(self):
        self.assertEqual(self.profile.nombre(), "Gonzalo")

    def test_resumen(self):
        self.assertEqual(
            self.profile.resumen(), ["Programador Python.", "Foco en scraping."]
        )

    def test_skills_con_nivel(self):
        self.assertEqual(
            self.profile.skills_con_nivel(),
            [
                {"nombre": "Python", "nivel": "intermedio"},
                {"nombre": "Git", "nivel": "básico"},
            ],
        )

    def test_skills_nombres(self):
        self.assertEqual(self.profile.skills_nombres(), ["Python", "Git"])

    def test_github(self):
        self.assertEqual(self.profile.github(), "https://github.com/gonza")


if __name__ == "__main__":
    unittest.main()
