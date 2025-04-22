import os
import json
import pytest
from src.programmer_profile import ProgrammerProfile


@pytest.fixture
def profile(tmp_path):
    """Crea un archivo de perfil temporal para testear."""
    path = tmp_path / "test_profile.json"

    data = {
        "nombre": "Gonzalo",
        "resumen": ["Programador Python.", "Foco en scraping."],
        "skills": [
            {"nombre": "Python", "nivel": "intermedio"},
            {"nombre": "Git", "nivel": "básico"},
        ],
        "links": {"github": "https://github.com/gonza"},
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    return ProgrammerProfile(path)


def test_nombre(profile):
    assert profile.nombre() == "Gonzalo"


def test_resumen(profile):
    assert profile.resumen() == ["Programador Python.", "Foco en scraping."]


def test_skills_con_nivel(profile):
    assert profile.skills_con_nivel() == [
        {"nombre": "Python", "nivel": "intermedio"},
        {"nombre": "Git", "nivel": "básico"},
    ]


def test_skills_nombres(profile):
    assert profile.skills_nombres() == ["Python", "Git"]


def test_github(profile):
    assert profile.github() == "https://github.com/gonza"
