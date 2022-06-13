
from flask import Flask
from utils import *

app = Flask(__name__)


@app.route("/")
def page_index():
    """Главная страничка."""

    candidates: list[dict] = load_candidates()
    result: str = get_candidates_preformatted(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_candidate(uid):
    """Страничка кандидата по ключу id."""

    candidate: dict = get_candidate_by_id(uid)
    result: str = f'<img src="{candidate["picture"]}">'
    result += get_candidates_preformatted([candidate])
    return result


@app.route('/skills/<skill>')
def page_skills(skill):
    """Страничка кандидатов у которых есть один из навыков по ключу skills."""

    candidate: list[dict] = get_candidate_by_skill(skill.lower())
    result = get_candidates_preformatted(candidate)
    return result


if __name__ == "__main__":
    app.run(host='127.0.0.2', port=5000)
