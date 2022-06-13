import json

# Имя JSON-файла с данными кандидатов
CANDIDATES_FILENAME = 'candidates.json'


def _load_json(filename: str, encoding: str = 'utf-8'):
    """
    Читает JSON-файл и возвращает список словарей.

    :param filename: имя JSON-файла
    :param encoding: имя кодировки для кодирования или декодирования
    :return: список словарей
    """

    with open(filename, encoding=encoding) as f:
        return json.load(f)


def load_candidates():
    """
    Загружает данные кандидатов из JSON-файла в список словарей.

    :return: список словарей
    """

    return _load_json(CANDIDATES_FILENAME)


def get_candidates_preformatted(candidates_list: list[dict]) -> str:
    """Преформатированная строка кандидатов на основе списка словарей из JSON файла."""

    result = '<pre>'
    for candidate in candidates_list:
        result += f"""
            {candidate['name']}\n
            {candidate['position']}\n
            {candidate['skills']}\n
        """
    result += '</pre>'
    return result


def get_candidate_by_id(uid: int) -> dict | None:
    """
    Возвращает словарь с данными кандидата по ключу id, перебирая исходный список словарей кандидатов.

    :param uid: значение поля 'id' в словаре кандидата

    :return: словарь с данными кандидата
    """

    candidates = load_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return None


def get_candidate_by_skill(skill: str) -> list[dict]:
    """
    Возвращает список словарей с данными кандидатов у которых содержится навык, передаваемый аргументом.

    :param skill: навык для фильтрации исходного списка кандидатов

    :return: список словарей с данными кандидатов
    """

    candidates = load_candidates()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)
    return result
