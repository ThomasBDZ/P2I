import pandas as pd
import os
from pathlib import Path
from os.path import basename
import numpy as np
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g

folder_path = "..\\dow-master\\data\\public"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

database = "..\\p2i.db"
app = Flask(__name__)



###################### Emilien ###################



print("##### REMPLISSAGE COMMENCE #####")


print("Remplissage table : Candidat")   
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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



print("Remplissage table : ville")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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



print("Remplissage table : CMT_Oraux")
with app.app_context():
    c = get_db().cursor()
    c.execute("DELETE FROM CMT_Oraux;")
    req = "INSERT INTO CMT_Oraux (Numerodinscription, Centre, Jury, Phys_SI, Maths, Entretien, Anglais) VALUES "

    df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_MP.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PC.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PSI.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PT.xlsx", header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage table : CMT_Oraux_Spe")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM CMT_Oraux_Spe;")
    req = "INSERT INTO CMT_Oraux_Spe (Numerodinscription, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais) VALUES "

    df = pd.read_excel(folder_path + "\\Classes_MP_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "
    
    df = pd.read_excel(folder_path + "\\Classes_PC_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\"), "    
    
    df = pd.read_excel(folder_path + "\\Classes_PSI_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "    
    
    df = pd.read_excel(folder_path + "\\Classes_PT_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\"), "    
   
    df = pd.read_excel(folder_path + "\\Classes_TSI_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage table : Oraux_CCS")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Classes_TSI_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM Oraux_CCS;") 

    req = "INSERT INTO Oraux_CCS (Numerodinscription, mathematiques_1, mathematiques_2, phy_chi_1, phy_chi_2, phy_TP, Langue, S2I) VALUES "
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[28]}\", \"{row[29]}\", \"{row[30]}\", \"{row[31]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   



print("Remplissage table : Oraux_CCMP")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Oraux_CCMP;")
    req = "INSERT INTO Oraux_CCMP (Numerodinscription, mathematiques, physique, francais, anglais) VALUES "

    df = pd.read_excel(folder_path + "\\Classes_MP_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\"), "
 
    df = pd.read_excel(folder_path + "\\Classes_PC_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\"), "
    
    df = pd.read_excel(folder_path + "\\Classes_PSI_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   




print("Remplissage table : CMT_Oraux")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Classes_CMT_spe_XXX;")
    req = "INSERT INTO Classes_CMT_spe_XXX (scei, etat, moyenne_generale, rang_classe) VALUES "

    df = pd.read_csv(folder_path + "\\Classes_MP_CMT_spe_XXXX_SCEI.csv", sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(folder_path + "\\Classes_PC_CMT_spe_XXXX_SCEI.csv", sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(folder_path + "\\Classes_PSI_CMT_spe_XXXX_SCEI.csv", sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(folder_path + "\\Classes_PT_CMT_spe_XXXX_SCEI.csv", sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
   
    df = pd.read_csv(folder_path + "\\Classes_TSI_CMT_spe_XXXX_SCEI.csv", sep=";")
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




print("Remplissage table : inscription")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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



print("Remplissage table : pays")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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



print("Remplissage table : nation")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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




print("Remplissage table : concours")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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



print("Remplissage table : bac")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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




print("Remplissage table : serie_bac")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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


print("Remplissage table : ListeEcoles")
with app.app_context():
    df = pd.read_excel(folder_path + "\\ListeEcoles.xlsx")
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


print("Remplissage table : csp")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
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




print("Remplissage table : Oral_Autres")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Oral_autres;")
    req = "INSERT INTO Oral_autres (Can_cod, rang, maths_harmonisees, maths_affichees, max_physique, max_anglais, total_oral, total, bonus_interclassement, total_interclassement, entretien_exaequo, anglais_exaequo) VALUES "

    df = pd.read_excel(folder_path + "\\Classes_MP_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[49]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\", \"{row[47]}\"), "
    
    df = pd.read_excel(folder_path + "\\Classes_PC_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[48]}\", \"{row[37]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\"), "
    
    df = pd.read_excel(folder_path + "\\Classes_PSI_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[49]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\", \"{row[43]}\", \"{row[44]}\", \"{row[45]}\", \"{row[46]}\", \"{row[47]}\"), "
    
    df = pd.read_excel(folder_path + "\\Classes_PT_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[37]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[41]}\", \"{row[42]}\"), "
   
    df = pd.read_excel(folder_path + "\\Classes_TSI_CMT_spe_XXXX.xlsx", header=1)
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



print("Remplissage table : ResultatEcrit")
with app.app_context():  
    c = get_db().cursor()
    c.execute("DELETE FROM Resultat_ecrit;")

    req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, mathematiques_1, mathematiques_2, physique_1, physique_2, chimie, Francais, Informatique_SI, Langue, Informatique_pour_tous) VALUES "
    dic = {}
    df = pd.read_excel(folder_path + "\\Classes_MP_CMT_spe_XXXX.xlsx", header=1)
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
    df = pd.read_excel(folder_path + "\\Classes_PC_CMT_spe_XXXX.xlsx", header=1)
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
    df = pd.read_excel(folder_path + "\\Classes_PSI_CMT_spe_XXXX.xlsx", header=1)
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
    df = pd.read_excel(folder_path + "\\Classes_PT_CMT_spe_XXXX.xlsx", header=1)
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
    df = pd.read_excel(folder_path + "\\Classes_TSI_CMT_spe_XXXX.xlsx", header=1)
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

    # ids = c.execute("SELECT Numerodinscription FROM Resultat_ecrit").fetchall()
    # print(ids)
    # df = pd.read_excel(folder_path + "\\ResultatEcrit_DD_MM_YYYY_ATS.xlsx", header=1)
    # req = "INSERT INTO Resultat_ecrit (Numerodinscription, rang_admissible, total, moyenne, mathematiques_1, physique_1, Francais, Informatique_SI, Langue) VALUES "
    # i = 0
    # for row in tab:
    #     print((row[0],) in ids)
    #     if (row[0],) not in ids:
    #         if i > 0: req += ", "
    #         i += 1
    #         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[5]}\", \"{row[6]}\", \"{row[7]}\", \"{row[8]}\", \"{row[9]}\")"
             
    # req += ";"
    # print(req[len(req)-50:])
    # c.execute(req)

c.execute("COMMIT;")
print("Table remplie")   


print("Remplissage table : bonification")
with app.app_context():
    df = pd.read_excel(folder_path + "\\Classes_MP_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM bonification;") 

    dic = {}
    for row in tab:
        dic[row[12]] = row[41]
    req = "INSERT INTO bonification (puissance, bonification) VALUES "
    i = len(dic)
    for x in dic:
        req += f"(\"{x}\", \"{dic[x]}\")"
        i -= 1
        if i > 0: req += ", " 
    req  += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")



################# Michael ############################



print("Remplissage table : listeEtatRe")
with app.app_context():
    df = pd.read_excel(folder_path + "/listeEtatsReponsesAppel.xlsx", header=1)
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


print("Remplissage table : voie_classe")
with app.app_context():
    df = pd.read_excel(folder_path + "/Inscription.xlsx", header=1)
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM voie_classe;") 

    dic = {}
    for row in tab:
        dic[row[21]] = row[37]
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


print("Remplissage table : listeVoeux")  
with app.app_context():
    c = get_db().cursor()
    c.execute("DELETE FROM listeVoeux;") 
    req = "INSERT INTO listeVoeux (Can_cod, Voe_rang, voe_ordre, Eco_code) VALUES "

    df = pd.read_excel(folder_path + "/listeVoeux_ATS.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(folder_path + "/listeVoeux_MP.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(folder_path + "/listeVoeux_PC.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(folder_path + "/listeVoeux_PSI.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(folder_path + "/listeVoeux_PT.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
        
    df = pd.read_excel(folder_path + "/listeVoeux_TSI.xlsx", header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")


print("Remplissage table : ListeEtablissements")  
with app.app_context():
    df = pd.read_excel(folder_path + "/listeEtablissements.xlsx", header=1)
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



################ Thomas ##################



filepath_inscription = "..\dow-master\data\public\Inscription.xlsx"
app = Flask(__name__)

def select_filiere(st): #selectionne la filière dans le nom d'un fichier
    c=0
    for i in st:
        if i =='_':
            break
        c +=1
    j = c+1
    for i in st[c+1:]:
        if i == "_":
            break
        j +=1
    return st[c+1:j]


dico = {}
for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        FilePrefix, FileExtension = os.path.splitext(filename)
        if (FileExtension == ".xlsx"):
            dico["{0}".format(FilePrefix)] = pd.read_excel(folder_path+"\\"+basename(filename))



with app.app_context():

    # TABLE SERIE BAC
    print("Remplissage table : Serie_bac")

    c = get_db().cursor()
    df = pd.read_excel(filepath_inscription,header=1)
    rows_code_bac = []
    for index,rows in df.iterrows():
        rows_code_bac.append([rows['CODE_SERIE'],rows['SERIE']])
    c.executemany("INSERT OR IGNORE INTO serie_bac (code_serie,serie) VALUES (?, ?)", (rows_code_bac))
    c.execute("COMMIT;")

    print("Table remplie")

    # TABLE ADMISSION

    print('Remplissage table : Admission')

    c.execute("DELETE FROM admissions;") 
    df = pd.read_excel(filepath_inscription,header=1)
    
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
                df = dico['ADMISSIBLE_'+select_filiere(FilePrefix)]
                tab = df.to_numpy()
                for row in tab:
                    if row[0] not in dic:
                        print(f"ERREUR : Le candidat {row[0]} n'est pas inscrit")
                    else:
                        dic[row[0]][0]=row[0]


            if ("ADMIS_" in FilePrefix) and ("SPE" in FilePrefix) and ("ADMIS_ATS" not in FilePrefix):
                df = dico['ADMIS_'+select_filiere(FilePrefix)]
                tab = df.to_numpy()
                for row in tab:
                    if row[0] not in dic:
                        print(f"ERREUR : Le candidat {row[0]} n'est pas inscrit")
                    else:
                        dic[row[0]][1]=row[12]
     # 1 pb : Can_cod 44232 introuvable dans Inscription mais présent dans ADMIS_PC
    

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
