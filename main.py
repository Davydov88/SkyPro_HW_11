from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")    # Создание представления route главной страницы и вывода всех кандидатов
def page_index():
    candidates = utils.load_candidates()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>")   # Создание представления route для вывода кандидата по ключу с отображением его фото
def get_by_id(id):
    candidate = utils.candidates_id(id)
    return render_template("card.html", candidate=candidate)


@app.route("/candidate/<skill>")    # Создание представления route  для вывода кандидатов при вводе skills
def get_by_skill(skill):
    candidates = utils.candidates_skill(skill)
    return render_template("skill.html", candidates=candidates, skill=skill)


@app.route("/candidate/search/<name>")    # Создание представления route  для вывода кандидатов при поиске по имени
def candidates_name(name):
    candidate = utils.candidates_name(name)
    return render_template("search.html", candidate=candidate, name=name)


if __name__ == '__main__':
    app.run(debug=True)
