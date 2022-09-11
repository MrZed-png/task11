import json


class CandidatesManager:

    def __init__(self, path):
        self.path = path

    def __repr__(self):
        return f"CandidatesManager({self.path})"

    def load_candidates_from_json(self):
        """Выгрузка файла"""
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data

    def get_all_candidates(self):
        """возвращает список всех кандидатов"""
        candidates = self.load_candidates_from_json()
        return candidates

    def get_candidate(self, pk):
        """возвращает одного кандидата по его id"""
        candidates = self.load_candidates_from_json()
        for candidate in candidates:
            if candidate['id'] == pk:
                return candidate
        return 'Нет кандидата'

    def get_candidates_by_name(self, name):
        """возвращает кандидатов по имени"""
        candidates = self.load_candidates_from_json()
        name = name.lower()
        matching_candidates = [candidate for candidate in candidates if name in candidate['name'].lower()]
        return matching_candidates

    def get_candidates_by_skill(self, skill):
        """возвращает кандидатов по навыку"""
        candidates = self.load_candidates_from_json()
        skill = skill.lower()

        matching_candidates = []

        for candidate in candidates:
            # Разделение на строки и уменьшения регистра для более точного поиска
            # Таких как Go и Django
            candidates_skill = candidate['skills'].lower().split(", ")
            if skill in candidates_skill:
                matching_candidates.append(candidate)

        return matching_candidates

