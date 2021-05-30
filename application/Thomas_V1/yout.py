from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from flask import g
from flask import Flask, render_template, url_for
from markupsafe import escape
import json
import os

app = Flask(__name__)

folder_path = os.path.join("..", "..", "p2i.db")

DATABASE = folder_path

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

    return render_template('index.html', title="mon titre", tabl= t)


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

@app.route("/Candidat")
def Candidat():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Candidat)")
    c.execute("select * from Candidat")
    return render_template("Candidat.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/admissions")
def admissions():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(admissions)")
    c.execute("select * from admissions")
    return render_template("admissions.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/CMT_Oraux")
def CMT_Oraux():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(CMT_Oraux)")
    c.execute("select * from CMT_Oraux")
    return render_template("CMT_Oraux.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/CMT_Oraux_Spe")
def CMT_Oraux_Spe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(CMT_Oraux_Spe)")
    c.execute("select * from CMT_Oraux_Spe")
    return render_template("CMT_Oraux_Spe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oraux_CCS")
def Oraux_CCS():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oraux_CCS)")
    c.execute("select * from Oraux_CCS")
    return render_template("Oraux_CCS.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oraux_CCMP")
def Oraux_CCMP():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oraux_CCMP)")
    c.execute("select * from Oraux_CCMP")
    return render_template("Oraux_CCMP.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/Classes_CMT_spe_XXX")
def Classes_CMT_spe_XXX():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Classes_CMT_spe_XXX)")
    c.execute("select * from Classes_CMT_spe_XXX")
    return render_template("Classes_CMT_spe_XXX.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/inscription")
def inscription():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(inscription)")
    c.execute("select * from inscription")
    return render_template("inscription.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/pays")
def pays():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(pays)")
    c.execute("select * from pays")
    return render_template("pays.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/nation")
def nation():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(nation)")
    c.execute("select * from nation")
    return render_template("nation.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/concours")
def concours():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(concours)")
    c.execute("select * from concours")
    return render_template("concours.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/bac")
def bac():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(bac)")
    c.execute("select * from bac")
    return render_template("bac.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/serie_bac")
def serie_bac():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(serie_bac)")
    c.execute("select * from serie_bac")
    return render_template("serie_bac.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/csp")
def csp():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(csp)")
    c.execute("select * from csp")
    return render_template("csp.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oral_autres")
def Oral_autres():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oral_autres)")
    c.execute("select * from Oral_autres")
    return render_template("Oral_autres.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Resultat_ecrit")
def Resultat_ecrit():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Resultat_ecrit)")
    c.execute("select * from Resultat_ecrit")
    return render_template("Resultat_ecrit.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/bonification")
def bonification():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(bonification)")
    c.execute("select * from bonification")
    return render_template("bonification.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/ville")
def ville():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ville)")
    c.execute("select * from ville")
    return render_template("ville.html", results= c.fetchall(), results2= h.fetchall())


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
