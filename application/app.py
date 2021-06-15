from flask import Flask, render_template, url_for, redirect, request
import sqlite3
from flask import g
from flask import Flask, render_template, url_for
from markupsafe import escape
import json
import os
from jinja2 import Template

app = Flask(__name__)

folder_path = os.path.join("p2i.db")

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


@app.route("/parcours")
def parcours():
    c = get_db().cursor()
    db = get_db()
    t = tables(db)

    return render_template('/tables/parcours.html', title="mon titre", tabl= t)

@app.route("/recherches")
def recherches():
    c = get_db().cursor()
    db = get_db()
    t = tables(db)

    return render_template('/recherches.html', title="mon titre", tabl= t)


@app.route("/ListeEcoleRequete")
def ListeEcolesRequete():
    c = get_db().cursor()
    c.execute("select Nom_ecole from ListeEcoles order by Nom_ecole ")
    return render_template("/tables/ListeEcoleRequete.html", results= c.fetchall())



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
    c.execute("select * from ListeEcoles ORDER BY Nom_ecole")
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
        rec = "SELECT" + requ
        c.execute(rec)
        return render_template("/tables/resultat_recherche.html", results= c.fetchall())
    else:
        return render_template("/recherche.html")

@app.route("/rechercheParEcoles", methods=["POST", "GET"])
def requestMap():
    if request.method == "POST":
        return render_template("/tables/resultat_recherche_Ecole.html",data=json.dumps(request.form["say"]) )
    else:
        return render_template("/rechercheEcole.html")

@app.route("/rechercheID", methods=["POST", "GET"])
def requesttID():
    if request.method == "POST":
        c = get_db().cursor()
        requ= request.form["Req"]
        rec = "SELECT * FROM Candidat WHERE Candidat.Can_cod = " + requ
        c.execute(rec)
        return render_template("/tables/resultat_recherche_ID.html", results= c.fetchall())
    else:
        return render_template("/rechercheID.html")

@app.route("/rechercheParNom", methods=["POST", "GET"])
def rechercheParNom():
    if request.method == "POST":
        c = get_db().cursor()
        requ= request.form["Req"]
        rec = "SELECT * FROM Candidat WHERE Candidat.nom = " + "\"" + requ.upper() + "\""
        c.execute(rec)
        return render_template("/tables/resultat_recherche_Par_Nom.html", results= c.fetchall())
    else:
        return render_template("/rechercheParNom.html")

@app.route("/rechercheParClasses", methods=["POST", "GET"])
def rechercheParClasses():
    if request.method == "POST":
        c = get_db().cursor()
        requ= request.form["Req"]
        rec = "SELECT * FROM Candidat WHERE Candidat.classe = " + "\"" + requ.upper() + "\""
        c.execute(rec)
        return render_template("/tables/resultat_recherche_par_classe.html", results= c.fetchall())
    else:
        return render_template("/rechercheParClasses.html")


@app.route("/résultat_ecrit")
def moygene():
    ecrit = ['mathematiques_1', 'mathematiques_2', 'physique_1', 'physique_2']
    c = get_db().cursor()
    c.execute("select mathematiques_1 from Resultat_ecrit")
    results= c.fetchall()
    moy1 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy1 = moy1 + i
                a+=1
    moy1 = moy1 /a
    h = get_db().cursor()
    h.execute("select mathematiques_2 from Resultat_ecrit")
    results= h.fetchall()
    moy2 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy2 = moy2 + i
                a+=1
    moy2 = moy2 / a
    cc = get_db().cursor()
    cc.execute("select physique_1 from Resultat_ecrit")
    results= cc.fetchall()
    moy3 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy3 = moy3 + i
                a+=1
    moy3 = moy3 / a
    ccc = get_db().cursor()
    ccc.execute("select physique_2 from Resultat_ecrit")
    results= ccc.fetchall()
    moy4 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy4 = moy4 + i
                a+=1
    moy4 = moy4 / a
    cccc = get_db().cursor()
    cccc.execute("select chimie from Resultat_ecrit")
    results= cccc.fetchall()
    moy5 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy5 = moy5 + i
                a+=1
    moy5 = moy5 / a
    ccccc = get_db().cursor()
    ccccc.execute("select Francais from Resultat_ecrit")
    results= ccccc.fetchall()
    moy6 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy6 = moy6 + i
                a+=1
    moy6 = moy6 / a
    cccccc = get_db().cursor()
    cccccc.execute("select Informatique_SI from Resultat_ecrit")
    results= cccccc.fetchall()
    moy7 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy7 = moy7 + i
                a+=1
    moy7 = moy7 / a
    ccccccc = get_db().cursor()
    ccccccc.execute("select Langue from Resultat_ecrit")
    results= ccccccc.fetchall()
    moy8 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy8 = moy8 + i
                a+=1
    moy8 = moy8 / a
    cccccccc = get_db().cursor()
    cccccccc.execute("select Informatique_pour_tous from Resultat_ecrit")
    results= cccccccc.fetchall()
    moy9 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None :
                moy9 = moy9 + i
                a+=1
    moy9 = moy9 / a
    moy = {}
    moy["labels"] = ["mathematiques 1", "mathematiques 2", "phhysique 1", "physique 2", "chimie", "français", "option info ou SI", "llangue", "IPT"]
    moy["data"] = [moy1, moy2, moy3, moy4, moy5, moy6, moy7, moy8, moy9]
    return render_template("Resultat_ecrit.html",moy=moy)



@app.route("/Resultats_Oraux")
def Resultats_Oraux():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Resultats_Oraux)")
    c.execute("select * from Resultats_Oraux")
    return render_template("/tables/Resultats_Oraux.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/Resultats_Oraux_Generaux_csv")
def Resultats_Oraux_Generaux_csv():
    c = get_db().cursor()
    h = get_db().cursor()
    h.execute("PRAGMA table_info(Resultats_Oraux_Generaux_csv)")
    c.execute("select * from Resultats_Oraux_Generaux_csv")
    return render_template("/tables/Resultats_Oraux_Generaux_csv.html", results= c.fetchall(), results2= h.fetchall())

@app.route("/liste_ecoles")
def liste_ecoles():
    c = get_db().cursor()
    c.execute("select nom_etabEtab from ListeEtablissements")
    return render_template("/liste_ecoles.html", results= c.fetchall())

@app.route("/résultat_oral")
def moygeneo():
    c = get_db().cursor()
    c.execute("select mathematiques from Resultats_Oraux")
    results= c.fetchall()
    moy1 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy1 = moy1 + i
                a+=1
    moy1 = moy1 /a
    h = get_db().cursor()
    h.execute("select physique from Resultats_Oraux")
    results= h.fetchall()
    moy2 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy2 = moy2 + i
                a+=1
    moy2 = moy2 / a
    cc = get_db().cursor()
    cc.execute("select francais from Resultats_Oraux")
    results= cc.fetchall()
    moy3 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy3 = moy3 + i
                a+=1
    moy3 = moy3 / a
    ccc = get_db().cursor()
    ccc.execute("select anglais from Resultats_Oraux")
    results= ccc.fetchall()
    moy4 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy4 = moy4 + i
                a+=1
    moy4 = moy4 / a
    cccc = get_db().cursor()
    cccc.execute("select mathematiques_1 from Resultats_Oraux")
    results= cccc.fetchall()
    moy5 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy5 = moy5 + i
                a+=1
    moy5 = moy5 / a
    ccccc = get_db().cursor()
    ccccc.execute("select mathematiques_2 from Resultats_Oraux")
    results= ccccc.fetchall()
    moy6 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy6 = moy6 + i
                a+=1
    moy6 = moy6 / a
    cccccc = get_db().cursor()
    cccccc.execute("select phy_chi_1 from Resultats_Oraux")
    results= cccccc.fetchall()
    moy7 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy7 = moy7 + i
                a+=1
    moy7 = moy7 / a
    ccccccc = get_db().cursor()
    ccccccc.execute("select phy_chi_2 from Resultats_Oraux")
    results= ccccccc.fetchall()
    moy8 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy8 = moy8 + i
                a+=1
    moy8 = moy8 / a
    cccccccc = get_db().cursor()
    cccccccc.execute("select phy_TP from Resultats_Oraux")
    results= cccccccc.fetchall()
    moy9 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy9 = moy9 + i
                a+=1
    moy9 = moy9 / a
    c6 = get_db().cursor()
    c6.execute("select Langue from Resultats_Oraux")
    results= c6.fetchall()
    moyc6 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc6 = moyc6 + i
                a+=1
    moyc6 = moyc6 / a
    c5 = get_db().cursor()
    c5.execute("select S2I from Resultats_Oraux")
    results= c5.fetchall()
    moyc5 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc5 = moyc5 + i
                a+=1
    moyc5 = moyc5 / a
    c4 = get_db().cursor()
    c4.execute("select QCM_info_phy from Resultats_Oraux")
    results= c4.fetchall()
    moyc4 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc4 = moyc4 + i
                a+=1
    moyc4 = moyc4 / a
    c3 = get_db().cursor()
    c3.execute("select Maths from Resultats_Oraux")
    results= c3.fetchall()
    moyc3 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc3 = moyc3 + i
                a+=1
    moyc3 = moyc3 / a
    c2 = get_db().cursor()
    c2.execute("select Entretien_MT from Resultats_Oraux")
    results= c2.fetchall()
    moyc2 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc2 = moyc2 + i
                a+=1
    moyc2 = moyc2 / a
    c1 = get_db().cursor()
    c1.execute("select QCM_Anglais from Resultats_Oraux")
    results= c1.fetchall()
    moyc1 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc1 = moyc1 + i
                a+=1
    moyc1 = moyc1 / a
    moy = {}
    moy["data"] = [moy1, moy2, moy3, moy4, moy5, moy6, moy7, moy8, moy9, moyc1, moyc2, moyc3, moyc4, moyc5, moyc6]
    moy["labels"] = ["maths", "physique", "français", "anglais", "mathematiques 1", "mathematiques 2", "phhysique chimie 1", "physique chimie 2", "TP de physique", "langue", "S2I", "QCM info physique", "Maths", "Entretien", "QCM Anglais"]
    return render_template("resultat_oral.html",moy=moy)


@app.route("/liste_ecoles/<eco>")
def lilip(eco):
    c = get_db().cursor()
    return render_template("eco.html", eco=eco)


@app.route("/résultats_ecrit")
def moyge():
    c = get_db().cursor()
    c.execute("select mathematiques_1 from Resultat_ecrit")
    results= c.fetchall()
    moy1 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy1 = moy1 + i
                a+=1
    moy1 = moy1 /a
    h = get_db().cursor()
    h.execute("select mathematiques_2 from Resultat_ecrit")
    results= h.fetchall()
    moy2 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy2 = moy2 + i
                a+=1
    moy2 = moy2 / a
    cc = get_db().cursor()
    cc.execute("select physique_1 from Resultat_ecrit")
    results= cc.fetchall()
    moy3 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy3 = moy3 + i
                a+=1
    moy3 = moy3 / a
    ccc = get_db().cursor()
    ccc.execute("select physique_2 from Resultat_ecrit")
    results= ccc.fetchall()
    moy4 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy4 = moy4 + i
                a+=1
    moy4 = moy4 / a
    cccc = get_db().cursor()
    cccc.execute("select chimie from Resultat_ecrit")
    results= cccc.fetchall()
    moy5 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy5 = moy5 + i
                a+=1
    moy5 = moy5 / a
    ccccc = get_db().cursor()
    ccccc.execute("select Francais from Resultat_ecrit")
    results= ccccc.fetchall()
    moy6 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy6 = moy6 + i
                a+=1
    moy6 = moy6 / a
    cccccc = get_db().cursor()
    cccccc.execute("select Informatique_SI from Resultat_ecrit")
    results= cccccc.fetchall()
    moy7 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy7 = moy7 + i
                a+=1
    moy7 = moy7 / a
    ccccccc = get_db().cursor()
    ccccccc.execute("select Langue from Resultat_ecrit")
    results= ccccccc.fetchall()
    moy8 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy8 = moy8 + i
                a+=1
    moy8 = moy8 / a
    cccccccc = get_db().cursor()
    cccccccc.execute("select Informatique_pour_tous from Resultat_ecrit")
    results= cccccccc.fetchall()
    moy9 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None :
                moy9 = moy9 + i
                a+=1
    moy9 = moy9 / a
    moy = {}
    moy["labels"] = ["mathematiques 1", "mathematiques 2", "phhysique 1", "physique 2", "chimie", "français", "option info ou SI", "llangue", "IPT"]
    moy["data"] = [moy1, moy2, moy3, moy4, moy5, moy6, moy7, moy8, moy9]
    return render_template("Resultat_ecrit.html", moy=moy)


@app.route("/liste_ecoles/<eco>/résultat_ecrit")
def moygecoe(eco):
    c = get_db().cursor()
    c.execute("select Resultat_ecrit.mathematiques_1 from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= c.fetchall()
    moy1 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy1 = moy1 + i
                a+=1
    if a!=0:
        moy1 = moy1 /a
    else: moy1 = 0
    h = get_db().cursor()
    h.execute("select Resultat_ecrit.mathematiques_2 from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= h.fetchall()
    moy2 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy2 = moy2 + i
                a+=1
    if a!=0:
        moy2 = moy2 /a
    else: moy2 = 0
    cc = get_db().cursor()
    cc.execute("select Resultat_ecrit.physique_1 from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= cc.fetchall()
    moy3 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy3 = moy3 + i
                a+=1
    if a!=0:
        moy3 = moy3 /a
    else: moy3 = 0
    ccc = get_db().cursor()
    ccc.execute("select Resultat_ecrit.physique_2 from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= ccc.fetchall()
    moy4 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy4 = moy4 + i
                a+=1
    if a!=0:
        moy4 = moy4 /a
    else: moy4 = 0
    cccc = get_db().cursor()
    cccc.execute("select Resultat_ecrit.chimie from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= cccc.fetchall()
    moy5 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy5 = moy5 + i
                a+=1
    if a!=0:
        moy5 = moy5 /a
    else: moy5 = 0
    ccccc = get_db().cursor() 
    ccccc.execute("select Resultat_ecrit.Francais from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= ccccc.fetchall()
    moy6 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy6 = moy6 + i
                a+=1
    if a!=0:
        moy6 = moy6 /a
    else: moy6 = 0
    cccccc = get_db().cursor()
    cccccc.execute("select Resultat_ecrit.Informatique_SI from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= cccccc.fetchall()
    moy7 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy7 = moy7 + i
                a+=1
    if a!=0:
        moy7 = moy7 /a
    else: moy7 = 0
    ccccccc = get_db().cursor()
    ccccccc.execute("select Resultat_ecrit.Langue from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= ccccccc.fetchall()
    moy8 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None:
                moy8 = moy8 + i
                a+=1
    if a!=0:
        moy8 = moy8 /a
    else: moy8 = 0
    cccccccc = get_db().cursor()
    cccccccc.execute("select Resultat_ecrit.Informatique_pour_tous from Resultat_ecrit join Candidat on Resultat_ecrit.Numerodinscription=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco + "'")
    results= cccccccc.fetchall()
    moy9 = 0
    a=0
    for sub in results:
        for i in sub:
            if i != None :
                moy9 = moy9 + i
                a+=1
    if a!=0:
        moy9 = moy9 /a
    else: moy9 = 0
    moy = {}
    moy["labels"] = ["mathematiques 1", "mathematiques 2", "phhysique 1", "physique 2", "chimie", "français", "option info ou SI", "llangue", "IPT"]
    moy["data"] = [moy1, moy2, moy3, moy4, moy5, moy6, moy7, moy8, moy9]
    return render_template("Resultat_ecrit.html", eco=eco,moy=moy)

@app.route("/liste_ecoles/<eco>/Candidats acceptés")
def moy2(eco):
    c = get_db().cursor()
    return render_template("eco.html", eco=eco,results= c.fetchall())

@app.route("/liste_ecoles/<eco>/résultat_Oraux")
def moy3(eco):
    c = get_db().cursor()
    c.execute("select Resultats_Oraux.mathematiques from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c.fetchall()
    moy1 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy1 = moy1 + i
                a+=1
    if a!=0:
        moy1 = moy1 /a
    else: moy1 = 0
    h = get_db().cursor()
    h.execute("select Resultats_Oraux.physique from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= h.fetchall()
    moy2 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy2 = moy2 + i
                a+=1
    if a!=0:
        moy2 = moy2 /a
    else: moy2 = 0
    cc = get_db().cursor()
    cc.execute("select Resultats_Oraux.francais from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= cc.fetchall()
    moy3 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy3 = moy3 + i
                a+=1
    if a!=0:
        moy3 = moy3 /a
    else: moy3 = 0
    ccc = get_db().cursor()
    ccc.execute("select Resultats_Oraux.anglais from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= ccc.fetchall()
    moy4 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy4 = moy4 + i
                a+=1
    if a!=0:
        moy4 = moy4 /a
    else: moy4 = 0
    cccc = get_db().cursor()
    cccc.execute("select Resultats_Oraux.mathematiques_1 from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= cccc.fetchall()
    moy5 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy5 = moy5 + i
                a+=1
    if a!=0:
        moy5 = moy5 /a
    else: moy5 = 0
    ccccc = get_db().cursor()
    ccccc.execute("select Resultats_Oraux.mathematiques_2 from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= ccccc.fetchall()
    moy6 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy6 = moy6 + i
                a+=1
    if a!=0:
        moy6 = moy6 /a
    else: moy6 = 0
    cccccc = get_db().cursor()
    cccccc.execute("select Resultats_Oraux.phy_chi_1 from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= cccccc.fetchall()
    moy7 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy7 = moy7 + i
                a+=1
    if a!=0:
        moy7 = moy7 /a
    else: moy7 = 0
    ccccccc = get_db().cursor()
    ccccccc.execute("select Resultats_Oraux.phy_chi_2 from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= ccccccc.fetchall()
    moy8 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy8 = moy8 + i
                a+=1
    if a!=0:
        moy8 = moy8 /a
    else: moy8 = 0
    cccccccc = get_db().cursor()
    cccccccc.execute("select Resultats_Oraux.phy_TP from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= cccccccc.fetchall()
    moy9 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moy9 = moy9 + i
                a+=1
    if a!=0:
        moy9 = moy9 /a
    else: moy9 = 0
    c6 = get_db().cursor()
    c6.execute("select Resultats_Oraux.Langue from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c6.fetchall()
    moyc6 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc6 = moyc6 + i
                a+=1
    if a!=0:
        moyc6 = moyc6 /a
    else: moyc6 = 0
    c5 = get_db().cursor()
    c5.execute("select Resultats_Oraux.S2I from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c5.fetchall()
    moyc5 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc5 = moyc5 + i
                a+=1
    if a!=0:
        moyc5 = moyc5 /a
    else: moyc5 = 0
    c4 = get_db().cursor()
    c4.execute("select Resultats_Oraux.QCM_info_phy from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c4.fetchall()
    moyc4 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc4 = moyc4 + i
                a+=1
    if a!=0:
        moyc4 = moyc4 /a
    else: moyc4 = 0
    c3 = get_db().cursor()
    c3.execute("select Resultats_Oraux.Maths from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c3.fetchall()
    moyc3 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc3 = moyc3 + i
                a+=1
    if a!=0:
        moyc3 = moyc3 /a
    else: moyc3 = 0
    c2 = get_db().cursor()
    c2.execute("select Resultats_Oraux.Entretien_MT from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c2.fetchall()
    moyc2 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc2 = moyc2 + i
                a+=1
    if a!=0:
        moyc2 = moyc2 /a
    else: moyc2 = 0
    c1 = get_db().cursor()
    c1.execute("select Resultats_Oraux.QCM_Anglais from Resultats_Oraux join Candidat on Resultats_Oraux.scei=Candidat.Can_cod join ListeEtablissements on Candidat.code_etablissement= ListeEtablissements.Rne where ListeEtablissements.nom_etabEtab = '" + eco +"'")
    results= c1.fetchall()
    moyc1 = 0
    a=0
    for sub in results:
        for i in sub:
            if type(i)==float:
                moyc1 = moyc1 + i
                a+=1
    if a!=0:
        moyc1 = moyc1 /a
    else: moyc1 = 0
    moy = {}
    moy["data"] = [moy1, moy2, moy3, moy4, moy5, moy6, moy7, moy8, moy9, moyc1, moyc2, moyc3, moyc4, moyc5, moyc6]
    moy["labels"] = ["mathematiques 1", "mathematiques 2", "phhysique 1", "physique 2", "chimie", "français", "option info ou SI", "llangue", "IPT"]
    return render_template("resultat_oral.html",moy=moy)


@app.route("/charts")
def charts():

    ################ Nombre de candidats par filière ################
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

    ################ profesions des parents ################
    c = get_db().cursor()
    tab = c.execute("SELECT (csp.cod_csp) FROM Candidat INNER JOIN csp WHERE Candidat.csp_pere = csp.cod_csp").fetchall()

    chartInfo2 = {}
    chartInfo2["label"] = ["agriculteurs", "artisans et commerçants", "cadres", "enseignement et santé", "fonction publique", "autres", "ouvriers", "retraités", "sans travail", "non renseigné"]
    index = {}
    for i in range(10):
        index[i] = chartInfo2["label"][i]
    chartInfo2["data"] = [0 for i in range(len(chartInfo2["label"]))]
    # pères
    for x in tab:
        chartInfo2["data"][x[0] % 10] += 1
    
    c = get_db().cursor()
    tab = c.execute("SELECT (csp.cod_csp) FROM Candidat INNER JOIN csp WHERE Candidat.csp_mere = csp.cod_csp").fetchall()
    # mères
    for x in tab:
        chartInfo2["data"][x[0] % 10] += 1

    # conversion en pourcentages
    sum = 0
    for x in chartInfo2["data"]:
        sum += x
    
    for i in range(10):
        chartInfo2["data"][i] = round(chartInfo2["data"][i]/sum * 100, 1)

    ################ nombre d'admissibles par pays ################

    c = get_db().cursor()
    tab = c.execute('SELECT pays.libele_pays FROM Candidat JOIN admissions ON Candidat.Can_cod = admissions.Can_cod JOIN pays ON pays.code_pays = Candidat.code_pays_nationalite WHERE admissions.admissible != "None";').fetchall()
    chartInfo3 = {}
    chartInfo3["label"] = []
    index = {}
    for x in tab:
        if (x[0] not in chartInfo3["label"]):
            chartInfo3["label"].append(x[0])
            index[x[0]] = len(chartInfo3["label"]) - 1
    chartInfo3["data"] = [0 for i in range(len(chartInfo3["label"]))]

    for x in tab:
        chartInfo3["data"][index[x[0]]] += 1

    ################ nombre d'admis par pays ################

    c = get_db().cursor()
    tab = c.execute('SELECT pays.libele_pays FROM Candidat JOIN admissions ON Candidat.Can_cod = admissions.Can_cod JOIN pays ON pays.code_pays = Candidat.code_pays_nationalite WHERE admissions.admis != "None";').fetchall()
    
    chartInfo4 = {}
    chartInfo4["label"] = []
    index = {}
    for x in tab:
        if (x[0] not in chartInfo4["label"]):
            chartInfo4["label"].append(x[0])
            index[x[0]] = len(chartInfo4["label"]) - 1
    chartInfo4["data"] = [0 for i in range(len(chartInfo4["label"]))]

    for x in tab:
        chartInfo4["data"][index[x[0]]] += 1
    
    

    return render_template("charts.html", chart1 = chartInfo1, chart2 = chartInfo2, chart3 = chartInfo3, chart4 = chartInfo4)





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
