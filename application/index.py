from flask import Flask
from flask import g, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/students_info')
def student_info():
    c = get_db().cursor()
    c.execute("SELECT * FROM GrandsAnciens")
    tab = c.fetchall()
    return render_template('students_info.html', tab=tab)

@app.route('/search_forms', methods = ['GET', 'POST'])
def search_forms():
    if not request.method == 'POST' and not request.form.get("id") and not (request.form.get("name") and request.form.get("first_name")):
        return render_template('search_forms.html')
    elif request.form.get("id"):
        id_ = request.form.get("id")
        c = get_db().cursor()
        c.execute(f"SELECT * FROM GrandsAnciens WHERE ID = {id_}")
        tab = c.fetchall()[0]
        return render_template('results.html', id=id_, tab=tab)
    else:
        return render_template('results.html', name=request.form.get("name"), fname = request.form.get("first_name"))

@app.route("/charts", )
def charts():
    c = get_db().cursor()
    c.execute("SELECT * FROM GrandsAnciens")
    tab = c.fetchall()
    return render_template('charts.html', tab=tab)

DATABASE = '../python/p2i.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exeption):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# c = get_db().cursor()

# c.execute(requete)
# c.fetchall()

if __name__ == "__main__":
    app.run(debug=True)