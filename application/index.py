from flask import Flask
from flask import g, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students_info')
def student_info():
    # squelette de la page
    template = render_template('students_info.html')

    # génération de la première ligne du tableau
    table = "<table>"
    table += "<tr>"
    table += "<th>identifiant</th>"
    table += "<th>nom</th>"
    table += "<th>prénom</th>"
    table += "</tr>"

    # génération du tableau, à modifier pour y isérer les données de la DB
    for i in range(5):
        table += "<tr>"
        for j in range(3):
            table += f"<td>[{i}, {j}]</td>"
        table += "</tr>"
    table += "</table>"

    # création de ce qui est retourné. template[270] est là ou doit être inséré le tableau dans le squelette, la méthode n'est pas élégante/propre, j'aimerais trouver une alternative pas trop complexe.
    page = template[:270] + table + template[270:]
    return page

# def get_db():
#     db = getattr(g, '_database', None)
#     if db is None:
#         db = g._database = sqlite3.connect(DATABASE)
#     return db

@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()