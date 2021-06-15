import pandas as pd
import os
from pathlib import Path
from os.path import basename
import numpy as np
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g

folder_path = os.path.join("dow-master", "data", "public")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

database = os.path.join("p2i.db")
app = Flask(__name__)



###################### Emilien ###################



print("##### REMPLISSAGE COMMENCE #####")



dico = {}
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        FilePrefix, FileExtension = os.path.splitext(filename)
        if ((FilePrefix != "Inscription") and (FileExtension == ".xlsx") and ("_DD_MM_YYYY_ATS" not in FilePrefix) and ("CMT_Oraux_YYYY_" not in FilePrefix) and ("CMT_spe_XXXX" not in FilePrefix)):
            dico["{0}".format(FilePrefix)] = pd.read_excel(os.path.join(folder_path, basename(filename)))
        elif ((FileExtension == ".xlsx") and ((FilePrefix == "Inscription") or ("_DD_MM_YYYY_ATS" in FilePrefix) or ("CMT_spe_XXXX" in FilePrefix) or ("CMT_Oraux_YYYY_" in FilePrefix) )):
            dico["{0}".format(FilePrefix)] = pd.read_excel(os.path.join(folder_path, basename(filename)), header = 1)
        elif (FileExtension == ".csv"):
            dico["{0}".format(FilePrefix)] = pd.read_csv(os.path.join(folder_path, basename(filename)), sep=";")


def filiere(path): 
    a=0
    for i in path:
        if i =='_':
            break
        a +=1
    j = a+1
    for i in path[a+1:]:
        if i == "_":
            break
        j +=1
    return path[a+1:j]

def filiere_oraux(path): 
    a=0
    for i in path:
        if i =='_':
            break
        a +=1
    j = a+1
    for i in path[a+1:]:
        if i == "_":
            break
        j +=1
    c = j+1
    for i in path[j+1:]:
        if i == "_":
            break
        c +=1
    b= c+1
    for i in path[c+1:]:
        if i == "_":
            break
        b +=1
    return path[c+1:b]



print("Remplissage de la table : Candidat")   
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM Candidat;") 

    i = len(tab)
    req = "INSERT INTO Candidat (Can_cod, Civ_lib, Nom, Prenom, autres_prenoms, date_naissance, ville_naissance, code_pays_naiss, code_pays_adr, Can_ad1, Can_ad2, Can_cod_pos, Can_mel, Can_tel, Can_por, francais, code_pays_nationalite, classe, puissance, code_etablissement, csp_mere, csp_pere, arrondissement_naissance, qualite) VALUES "
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[4]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[5]}\", \"{row[6]}\", \"{row[7]}\", \"{row[16]}\", \"{row[12]}\", \"{row[13]}\", \"{row[14]}\", \"{row[20]}\", \"{row[18]}\", \"{row[19]}\", \"{row[9]}\", \"{row[10]}\", \"{row[21]}\", \"{row[22]}\", \"{row[23]}\", \"{row[47]}\", \"{row[45]}\", \"{row[51]}\", \"{row[53]}\")"
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

print("Remplissage de la table : Candidat pour ATS")   
with app.app_context():
    df = dico["ResultatEcrit_DD_MM_YYYY_ATS"]
    tab = df.to_numpy()
    c = get_db().cursor()

    i = len(tab)
    req = "INSERT INTO Candidat (Can_cod, classe) VALUES "
    for row in tab:
        req += f"(\"{row[0]}\", \"ATS\")"
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

print("Remplissage de la table : ville")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM ville;") 

    dic = {}
    for row in tab:
        dic[row[14]] = row[15]
    req = "INSERT INTO ville (code_postal, nom_ville) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

#######################################################################################################


print("Remplissage de la table : Resultats_Oraux_Generaux_csv")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Resultats_Oraux_Generaux_csv;") 
    req = "INSERT INTO Resultats_Oraux_Generaux_csv (scei, etat, moyenne_generale, rang_classe) VALUES "

    df = dico["Classes_MP_CMT_spe_XXXX_SCEI"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = dico["Classes_PC_CMT_spe_XXXX_SCEI"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = dico["Classes_PSI_CMT_spe_XXXX_SCEI"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = dico["Classes_PT_CMT_spe_XXXX_SCEI"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
   
    df = dico["Classes_TSI_CMT_spe_XXXX_SCEI"]
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

print("Remplissage de la table :Resultats_Oraux avec : Oraux_CCMP")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Resultats_Oraux;") 
    req = "INSERT INTO Resultats_Oraux (scei, mathematiques, physique, francais, anglais, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais, bonification) VALUES "

    df = dico["Classes_MP_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\", \"{row[41]}\"), "
 
    df = dico["Classes_PC_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[40]}\"), "
    
    df = dico["Classes_PSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\", \"{row[41]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")

print("Remplissage de la table : Resultats_Oraux avec : Oraux_CCS")
with app.app_context():
    df = dico["Classes_TSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    c = get_db().cursor()

    req = "INSERT INTO Resultats_Oraux (scei, mathematiques_1, mathematiques_2, phy_chi_1, phy_chi_2, phy_TP, Langue, S2I, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais, bonification) VALUES "
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[28]}\", \"{row[29]}\", \"{row[30]}\", \"{row[31]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[37]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

print("Remplissage de la table : Resultats_Oraux")
with app.app_context():  
    c = get_db().cursor()
    req = "INSERT INTO Resultats_Oraux (scei, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais, bonification) VALUES "

    df = dico["Classes_PT_CMT_spe_XXXX"]
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[36]}\") "    
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")

print("Remplissage de la table : Resultats_Oraux avec ATS")
with app.app_context():  
    c = get_db().cursor()
    req = "INSERT INTO Resultats_Oraux (scei, MathsATS, PhysiqueATS, Genie_electriqueATS, Genie_mecaniqueATS, LangueATS, bonification) VALUES "

    df = dico["ResultatOral_DD_MM_YYYY_ATS"]
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[6]}\", \"{row[7]}\", \"{row[8]}\", \"{row[9]}\", \"{row[10]}\", \"{row[4]}\") "    
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")


########################################################################################################

print("Remplissage de la table : inscription")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM inscription;") 

    req = "INSERT INTO inscription (Code_Candidat, option1, option2, option3, option4, epreuve1, epreuve2, epreuve3, epreuve4, libelle_ville_ecrit, code_concours, code_etat_dosssier, declaration_handicap, sujet_tipe) VALUES "
    i = len(tab)
    for row in tab:
        tipe = row[43]
        if row[43][0] == '"': tipe = tipe[1:len(tipe)-2]
        req += f"(\"{row[0]}\", \"{row[27]}\", \"{row[29]}\", \"{row[31]}\", \"{row[33]}\", \"{row[26]}\", \"{row[28]}\", \"{row[30]}\", \"{row[32]}\", \"{row[34]}\", \"{row[35]}\", \"{row[49]}\", \"{row[52]}\", \"{tipe}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage de la table : pays")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM pays;") 

    dic = {}
    for row in tab:
        dic[row[7]] = row[8]
        dic[row[16]] = row[17]
    req = "INSERT INTO pays (code_pays, libele_pays) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage de la table : nation")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM nation;") 

    dic = {}
    for row in tab:
        dic[row[10]] = row[11]
    req = "INSERT INTO nation (code_pays, nationalite) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   




print("Remplissage de la table : concours")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM concours;") 

    dic = {}
    for row in tab:
        dic[row[35]] = [row[36], row[37]]
    req = "INSERT INTO concours (code_concours, libelle_concours, voie) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage de la table : bac")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM bac;") 

    req = "INSERT INTO bac (Can_cod, numero_ine, annee_bac, mois_bac, code_serie, mention, can_dep_bac) VALUES "
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[42]}\", \"{row[54]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   




print("Remplissage de la table : serie_bac")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM serie_bac;") 

    dic = {}
    for row in tab:
        dic[row[40]] = row[41]
    req = "INSERT INTO serie_bac (code_serie, serie) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   


print("Remplissage de la table : ListeEcoles")
with app.app_context():
    df = dico["listeEcoles"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM ListeEcoles;") 

    dic = {}
    for row in tab:
        dic[row[0]] = row[1]
    req = "INSERT INTO ListeEcoles (NumeroEcole, Nom_ecole) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   


print("Remplissage de la table : csp")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM csp;") 

    dic = {}
    for row in tab:
        dic[row[45]] = row[46]
        dic[row[47]] = row[48]
    req = "INSERT INTO csp (cod_csp, lib_csp) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   




print("Remplissage de la table : Oral_Autres")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Oral_autres;")
    req = "INSERT INTO Oral_autres (Can_cod, rang, maths_harmonisees, maths_affichees, max_physique, max_anglais, total_oral, total, bonus_interclassement, total_interclassement, entretien_exaequo, anglais_exaequo) VALUES "

    df = dico["Classes_MP_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[49]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\", \"{row[47]}\"), "
    
    df = dico["Classes_PC_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[48]}\", \"{row[37]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\"), "
    
    df = dico["Classes_PSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[49]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\", \"{row[47]}\"), "
    
    df = dico["Classes_PT_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[37]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\"), "
   
    df = dico["Classes_TSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[37]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage de la table : Resultat_Ecrit")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Resultat_ecrit;")

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, chimie, Francais, Informatique_SI, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = dico["Classes_MP_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]] = [row[24], row[23], row[15], row[16], row[17], row[18], row[19], row[20], row[14], row[13], row[21]]
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]}\", \"{dic[x][4]}\", \"{dic[x][5]}\", \"{dic[x][6]}\", \"{dic[x][7]}\", \"{dic[x][8]}\", \"{dic[x][9]}\", \"{dic[x][10]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, chimie, Francais, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = dico["Classes_PC_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]] = [row[23], row[22], row[14], row[15], row[16], row[17], row[18], row[19], row[13], row[20]]
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]}\", \"{dic[x][4]}\", \"{dic[x][5]}\", \"{dic[x][6]}\", \"{dic[x][7]}\", \"{dic[x][8]}\", \"{dic[x][9]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, chimie, Francais, Informatique_SI, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = dico["Classes_PSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]] = [row[24], row[23], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[13], row[21]]
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]}\", \"{dic[x][4]}\", \"{dic[x][5]}\", \"{dic[x][6]}\", \"{dic[x][7]}\", \"{dic[x][8]}\", \"{dic[x][9]}\", \"{dic[x][10]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, Francais, Informatique_SI, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = dico["Classes_PT_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]] = [row[23], row[22], row[13], row[14], row[15], row[16], row[19], row[18], row[20], row[17]]
        i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]}\", \"{dic[x][4]}\", \"{dic[x][5]}\", \"{dic[x][6]}\", \"{dic[x][7]}\", \"{dic[x][8]}\", \"{dic[x][9]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, Francais, Informatique_SI, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = dico["Classes_TSI_CMT_spe_XXXX"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]] = [row[23], row[22], row[13], row[14], row[15], row[16], row[17], row[19], row[18], row[20]]
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]}\", \"{dic[x][4]}\", \"{dic[x][5]}\", \"{dic[x][6]}\", \"{dic[x][7]}\", \"{dic[x][8]}\", \"{dic[x][9]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")

    
print("Table remplie")




print("Remplissage de la table : listeEtatRe")
with app.app_context():
    df = dico["listeEtatsReponsesAppel"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM listeEtasRe;") 

    i = len(tab)
    req = "INSERT INTO listeEtasRe (Ata_cod, Ata_lib) VALUES "
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\")"
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   


print("Remplissage de la table : voie_classe")
with app.app_context():
    df = dico["Inscription"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM voie_classe;") 

    dic = {}
    for row in tab:
        dic[row[21]] = row[37]
    dic["ATS"] = "ATS"
    req = "INSERT INTO voie_classe (classe, voie) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")


print("Remplissage de la table : listeVoeux")  
with app.app_context():
    c = get_db().cursor()
    c.execute("DELETE FROM listeVoeux;") 
    req = "INSERT INTO listeVoeux (Can_cod, Voe_rang, voe_ordre, Eco_code) VALUES "

    i=1
    j=0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            FilePrefix, FileExtension = os.path.splitext(filename)
            if ("listeVoeux_" in FilePrefix):
                j+=1 # COMPTE LE NOMBRE DE FICHIERS DE CE TYPE DANS LE REPERTOIRE
        for filename in filenames:
            FilePrefix, FileExtension = os.path.splitext(filename)
            if ("listeVoeux_" in FilePrefix):
                df = dico["listeVoeux_"+filiere(FilePrefix)]
                tab = df.to_numpy()
                if(i != j):
                    i+=1
                    for row in tab:
                        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
                else:
                    k = len(tab)
                    for row in tab:
                        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\")"
                        k -= 1
                        if k > 0: req += ", "
                    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")

print("Remplissage de la table : ListeEtablissements")  
with app.app_context():
    df = dico["listeEtablissements"]
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM ListeEtablissements;") 

    i = len(tab)
    req = "INSERT INTO ListeEtablissements (Rne, type_etab, nom_etabEtab, Code_postal_etab, Pays_etablissement) VALUES "
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\")"
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")




with app.app_context():

    # TABLE SERIE BAC
    print("Remplissage de la de la table : Serie_bac")

    c = get_db().cursor()
    df = dico["Inscription"]
    rows_code_bac = []
    for index,rows in df.iterrows():
        rows_code_bac.append([rows['CODE_SERIE'],rows['SERIE']])
    c.executemany("INSERT OR IGNORE INTO serie_bac (code_serie,serie) VALUES (?, ?)", (rows_code_bac))
    c.execute("COMMIT;")

    print("Table remplie")

    # TABLE ADMISSION

    print('Remplissage table : Admission')

    c.execute("DELETE FROM admissions;") 
    df = dico["Inscription"]
    
    tab = df.to_numpy()
    
    dic = {}
    for row in tab:
        dic[row[0]] = []
        dic[row[0]].append(None)
        dic[row[0]].append(None)

    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            FilePrefix, FileExtension = os.path.splitext(filename)
            if ("ADMISSIBLE" in FilePrefix) and ("SPE" in FilePrefix) and ("ADMISSIBLE_ATS" not in FilePrefix): 
                df = dico['ADMISSIBLE_'+filiere(FilePrefix)]
                tab = df.to_numpy()
                for row in tab:
                    if row[0] not in dic:
                        print(f"ERREUR : Le candidat {row[0]} n'est pas inscrit")
                    else:
                        dic[row[0]][0]=row[0]


            if ("ADMIS_" in FilePrefix) and ("SPE" in FilePrefix) and ("ADMIS_ATS" not in FilePrefix):
                df = dico['ADMIS_'+filiere(FilePrefix)]
                tab = df.to_numpy()
                for row in tab:
                    if row[0] not in dic:
                        print(f"ERREUR : Le candidat {row[0]} n'est pas inscrit")
                    else:
                        dic[row[0]][1]=row[12]
    

    code_tab = c.execute("SELECT Code_Candidat FROM inscription")
    req = "INSERT INTO admissions (Can_cod, admissible, admis) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\",  \"{dic[x][0]}\", \"{dic[x][1]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")

    print('Table remplie')

print("##### REMPLISSAGE TERMINE #####")















###########################################################################################################################
### TEMPLATE POUR REMPLIR ###
###########################################################################################################################

# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()

#     req = "INSERT INTO bac (numero_ine, annee_bac, mois_bac, code_serie, mention, can_dep_bac) VALUES "
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[42]}\", \"{row[54]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

###############

# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM pays;") 

#     dic = {}
#     for row in tab:
#         dic[row[10]] = [row[8], row[11]]
#     req = "INSERT INTO pays (code_pays, libele_pays, nationalite) VALUES "
#     i = len(dic)
#     for x in dic:
#         req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req  += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

###############

# with app.app_context():
#     df1 = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     df2 = pd.read_excel(folder_path + "\\ADMISSIBLE_MP.xlsx") 
#     tab1 = df1.to_numpy()
#     tab2 = df2.to_numpy()
#     c = get_db().cursor()

#     dic = {}
#     for row in tab1:
#         dic[row[pk]] = [row[y], row[z]]
#     for row in tab2:
#         dic[row[pk]].append(row[v]) #il faudra peut être changer le pk, car on est dans un tab différent
#         dic[row[pk]].append(row[w])
#     req = "INSERT INTO table (col1, col2, col3, col4, col5) VALUES "
#     i = len(dic)
#     for pk in dic:
#             req += f"(\"{pk}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]})\""
#             i -= 1
#             if i > 0: req += ", "
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

###########################################################################################################################
