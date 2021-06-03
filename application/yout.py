from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from flask import g
from flask import Flask, render_template, url_for
from markupsafe import escape
import json
import os
from jinja2 import Template

app = Flask(__name__)

folder_path = os.path.join("..", "p2i.db")

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






@app.route("/ListeEtablissements")
def listeEtablissements():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ListeEtablissements)")
    c.execute("select * from ListeEtablissements")
    return render_template("/tables/ListeEtablissements.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/ListeEcoles")
def listeEcole():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ListeEcoles)")
    c.execute("select * from ListeEcoles")
    return render_template("/tables/ListeEcoles.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/listeEtasRe")
def listeEtasRe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(listeEtasRe)")
    c.execute("select * from listeEtasRe")
    return render_template("/tables/listeEtasRe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/voie_classe")
def voie_classe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(voie_classe)")
    c.execute("select * from voie_classe")
    return render_template("/tables/voie_classe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Candidat")
def Candidat():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Candidat)")
    c.execute("select * from Candidat")
    return render_template("/tables/Candidat.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/admissions")
def admissions():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(admissions)")
    c.execute("select * from admissions")
    return render_template("/tables/admissions.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/CMT_Oraux")
def CMT_Oraux():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(CMT_Oraux)")
    c.execute("select * from CMT_Oraux")
    return render_template("/tables/CMT_Oraux.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/CMT_Oraux_Spe")
def CMT_Oraux_Spe():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(CMT_Oraux_Spe)")
    c.execute("select * from CMT_Oraux_Spe")
    return render_template("/tables/CMT_Oraux_Spe.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oraux_CCS")
def Oraux_CCS():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oraux_CCS)")
    c.execute("select * from Oraux_CCS")
    return render_template("/tables/Oraux_CCS.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oraux_CCMP")
def Oraux_CCMP():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oraux_CCMP)")
    c.execute("select * from Oraux_CCMP")
    return render_template("/tables/Oraux_CCMP.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/Classes_CMT_spe_XXX")
def Classes_CMT_spe_XXX():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Classes_CMT_spe_XXX)")
    c.execute("select * from Classes_CMT_spe_XXX")
    return render_template("/tables/Classes_CMT_spe_XXX.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/inscription")
def inscription():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(inscription)")
    c.execute("select * from inscription")
    return render_template("/tables/inscription.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/pays")
def pays():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(pays)")
    c.execute("select * from pays")
    return render_template("/tables/pays.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/nation")
def nation():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(nation)")
    c.execute("select * from nation")
    return render_template("/tables/nation.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/concours")
def concours():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(concours)")
    c.execute("select * from concours")
    return render_template("/tables/concours.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/bac")
def bac():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(bac)")
    c.execute("select * from bac")
    return render_template("/tables/bac.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/serie_bac")
def serie_bac():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(serie_bac)")
    c.execute("select * from serie_bac")
    return render_template("/tables/serie_bac.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/csp")
def csp():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(csp)")
    c.execute("select * from csp")
    return render_template("/tables/csp.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Oral_autres")
def Oral_autres():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Oral_autres)")
    c.execute("select * from Oral_autres")
    return render_template("/tables/Oral_autres.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Resultat_ecrit")
def Resultat_ecrit():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Resultat_ecrit)")
    c.execute("select * from Resultat_ecrit")
    return render_template("/tables/Resultat_ecrit.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/bonification")
def bonification():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(bonification)")
    c.execute("select * from bonification")
    return render_template("/tables/bonification.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/ville")
def ville():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(ville)")
    c.execute("select * from ville")
    return render_template("/tables/ville.html", results= c.fetchall(), results2= h.fetchall())


@app.route("/listeVoeux")
def liste_voeux():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(listeVoeux)")
    c.execute("select * from listeVoeux")
    return render_template("/tables/liste_voeux.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/recherche", methods=["POST", "GET"])
def requestt():
    if request.method == "POST":
        c = get_db().cursor()
        requ= request.form["Req"]
        c.execute(requ)
        return render_template("resultat_recherche.html", results= c.fetchall())
    else:
        return render_template("recherche.html")

@app.route("/charts")
def charts():

    # Nombre de candidats par filière
    c = get_db().cursor()
    tab = c.execute("SELECT (voie_classe.voie) FROM Candidat INNER JOIN voie_classe WHERE Candidat.classe = voie_classe.classe").fetchall()
    
    chartInfo1 = {}
    chartInfo1["label"] = []
    index = {}
    for x in tab:
        if (x[0] not in chartInfo1["label"]):
            chartInfo1["label"].append(x[0])
            index[x[0]] = len(chartInfo1["label"]) - 1
    chartInfo1["data"] = [0 for i in range(len(chartInfo1["label"]))]

    for x in tab:
        chartInfo1["data"][index[x[0]]] += 1

    # proffesions des pères
    c = get_db().cursor()
    tab = c.execute("SELECT (csp.cod_csp) FROM Candidat INNER JOIN csp WHERE Candidat.csp_pere = csp.cod_csp").fetchall()

    chartInfo2 = {}
    chartInfo2["label"] = ["agriculteurs", "artisans et commerçants", "cadres", "enseignement et santé", "fonction publique", "autres", "ouvriers", "retraités", "sans travail", "non renseigné"]
    index = {}
    for i in range(10):
        index[i] = chartInfo2["label"][i]
    chartInfo2["data"] = [0 for i in range(len(chartInfo2["label"]))]

    for x in tab:
        chartInfo2["data"][x[0] % 10] += 1
    
    c = get_db().cursor()
    tab = c.execute("SELECT (csp.cod_csp) FROM Candidat INNER JOIN csp WHERE Candidat.csp_mere = csp.cod_csp").fetchall()

    for x in tab:
        chartInfo2["data"][x[0] % 10] += 1

    sum = 0
    for x in chartInfo2["data"]:
        sum += x
    
    for i in range(10):
        chartInfo2["data"][i] = round(chartInfo2["data"][i]/sum * 100, 1)


    return render_template("charts.html", chart1 = chartInfo1, chart2 = chartInfo2, tab=tab)



if __name__ == "__main__":
	app.run(debug=True)


# @app.route("/admin")
# def admin():
# 	return redirect(url_for("user", name="Admin!"))  # Now we when we go to /admin we will redirect to user with the argument "Admin!"

# @app.route("/for")
# def forr():
#     return render_template("for.html")


# @app.route("/inherit")
# def inherit():
#     return render_template("inherit.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("login.html")


# @app.route("/table")
# def table():
#     return render_template("table.html")

# @app.route("/list")
# def liste():
#     return render_template("list.html")
