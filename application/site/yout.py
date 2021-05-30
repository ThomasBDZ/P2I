from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from flask import g
from flask import Flask, render_template, url_for
from markupsafe import escape
import json

app = Flask(__name__)

DATABASE = '/home/michael/p2i_test/project-grp12/p2i.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext   #teardown permet de le faire à chaque fois à la fin
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def tables(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = [
        v[0] for v in cursor.fetchall()
        if v[0] != "sqlite_sequence"
    ]
    cursor.close()
    return tables


@app.route("/")
def home():
    c = get_db().cursor()
    db = get_db()
    t = tables(db)
    c.execute("select * from ListeEtablissements")

    return render_template('base.html', title="mon titre", results=c.fetchall(), tabl= t)


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/admin")
def admin():
	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

@app.route("/for")
def forr():
    return render_template("for.html")


@app.route("/inherit")
def inherit():
    return render_template("inherit.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/table")
def table():
    return render_template("table.html")

@app.route("/list")
def liste():
    return render_template("list.html")

@app.route("/Candidat")
def Candidat():
    return "Hello"

@app.route("/ListeEtablissements")
def listeEtablissements():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ListeEtablissements)")
    c.execute("select * from ListeEtablissements")
    return render_template("ListeEtablissements.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/ListeEcoles")
def listeEcole():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ListeEcoles)")
    c.execute("select * from ListeEcoles")
    return render_template("ListeEcoles.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/listeEtasRe")
def listeEtasRe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(listeEtasRe)")
    c.execute("select * from listeEtasRe")
    return render_template("listeEtasRe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/voie_classe")
def voie_classe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(voie_classe)")
    c.execute("select * from voie_classe")
    return render_template("voie_classe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/listeVoeux")
def liste_voeux():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(listeVoeux)")
    c.execute("select * from listeVoeux")
    return render_template("liste_voeux.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/recherche", methods=["POST", "GET"])
def requestt():
    if request.method == "POST":
        c = get_db().cursor()
        requ= request.form["Req"]
        c.execute(requ)
        return render_template("resultat_recherche.html", results= c.fetchall())
    else:
        return render_template("recherche.html")

if __name__ == "__main__":
	app.run(debug=True)
