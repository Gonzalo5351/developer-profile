import json

class ProgrammerProfile:
    def __init__(self, profile_path="perfil.json"):
        """Carga el perfil del programador desde un archivo JSON."""
        self.profile_path = profile_path
        self.skills = self.load_profile()

    def load_profile(self):
        """Carga los datos del perfil desde el JSON."""
        try:
            with open(self.profile_path, "r", encoding="utf-8") as file:
                return json.load(file).get("skills", [])
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def matches(self, job):
        """
        Verifica si una oferta de trabajo coincide con los conocimientos del programador.
        - job: Un diccionario con al menos la clave "descripcion".
        - Retorna True si hay coincidencias, False en caso contrario.
        """
        job_desc = job.get("descripcion", "").lower()
        return any(skill.lower() in job_desc for skill in self.skills)

    def add_skill(self, skill):
        """Agrega una nueva habilidad al perfil y actualiza el JSON."""
        if skill not in self.skills:
            self.skills.append(skill)
            self.save_profile()

    def save_profile(self):
        """Guarda el perfil actualizado en el JSON."""
        with open(self.profile_path, "w", encoding="utf-8") as file:
            json.dump({"skills": self.skills}, file, indent=4, ensure_ascii=False)
