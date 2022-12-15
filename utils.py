import json


def load_candidates():
    """Функция, которая загружает все данные из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def get_all():
    """Функция, которая покажет всех кандидатов"""
    return load_candidates()


def candidates_id(id):
    """Функция, которая возвращает кандидатов по id"""
    for candidate in load_candidates():
        if candidate["id"] == id:
            return candidate

    return f"Такого кандидата нет в списке"


def candidates_skill(skill):
    """Функция, которая возвращает кандидатов по навыку"""
    candidates = []
    for candidate in load_candidates():
        if skill.lower() in candidate["skills"].lower().split(', '):
            candidates.append(candidate)
    return candidates


def candidates_name(name):
    """Функция, которая возвращает кандидатов по имени"""
    for candidate in load_candidates():
        if candidate["name"].lower() == name.lower():
            return candidate
