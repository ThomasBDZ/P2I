import pandas as pd
import os
from pathlib import Path
from os.path import basename
import numpy as np
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g

folder_path = "dow-master/data/public"

# dico = {}
# for dirpath, dirnames, filenames in os.walk(folder_path):
#   for filename in filenames:
#       FilePrefix, FileExtension = os.path.splitext(filename)
#       if (FileExtension == ".xlsx"):
#           dico["{0}".format(FilePrefix)] = pd.read_excel(folder_path+"\\"+basename(filename))



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db

def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

database = "p2i.db"
app = Flask(__name__)
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


# bac
# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM bac;") 

#     req = "INSERT INTO bac (Can_cod, numero_ine, annee_bac, mois_bac, code_serie, mention, can_dep_bac) VALUES "
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[44]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[42]}\", \"{row[54]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# pays
# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM pays;") 

#     dic = {}
#     for row in tab:
#         dic[row[10]] = [row[8], row[11]]
#     for row in tab:
#         dic[row[16]][0] = row[17]
#     req = "INSERT INTO pays (code_pays, libele_pays, nationalite) VALUES "
#     i = len(dic)
#     for x in dic:
#         req += f"(\"{x}\", \"{dic[x][0]}\", \"{dic[x][1]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req  += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# Candidat   
# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM Candidat;") 

#     i = len(tab)
#     req = "INSERT INTO Candidat (Can_cod, Civ_lib, Nom, Prenom, autres_prenoms, date_naissance, ville_naissance, code_pays_naiss, code_pays_adr, Can_ad1, Can_ad2, Can_cod_pos, Can_mel, Can_tel, Can_por, francais, code_pays_nationalite, classe, puissance, code_etablissement, csp_mere, csp_pere, arrondissement_naissance, qualite) VALUES "
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[4]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[5]}\", \"{row[6]}\", \"{row[7]}\", \"{row[16]}\", \"{row[12]}\", \"{row[13]}\", \"{row[14]}\", \"{row[20]}\", \"{row[18]}\", \"{row[19]}\", \"{row[9]}\", \"{row[10]}\", \"{row[21]}\", \"{row[22]}\", \"{row[23]}\", \"{row[47]}\", \"{row[45]}\", \"{row[51]}\", \"{row[53]}\")"
#         i -= 1
#         if i > 0: req += ", "
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# ville
# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM ville;") 

#     dic = {}
#     for row in tab:
#         dic[row[14]] = row[15]
#     req = "INSERT INTO ville (code_postal, nom_ville) VALUES "
#     i = len(dic)
#     for x in dic:
#         req += f"(\"{x}\", \"{dic[x]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req  += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

#CMT_Oraux
# with app.app_context():
    
#     c = get_db().cursor()
#     c.execute("DELETE FROM CMT_Oraux;")
#     req = "INSERT INTO CMT_Oraux (Numerodinscription, Centre, Jury, Phys_SI, Maths, Entretien, Anglais) VALUES "

#     df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_MP.xlsx", header=1)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PC.xlsx", header=1)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PSI.xlsx", header=1)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_excel(folder_path + "\\CMT_Oraux_YYYY_PT.xlsx", header=1)
#     tab = df.to_numpy()
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\", \"{row[5]}\", \"{row[6]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

#CMT_Oraux
with app.app_context():
    
    c = get_db().cursor()
    c.execute("DELETE FROM CMT_Oraux_Spe;")
    req = "INSERT INTO CMT_Oraux_Spe (Numerodinscription, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais) VALUES "

    df = pd.read_excel(folder_path + "/Classes_MP_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "
    
    df = pd.read_excel(folder_path + "/Classes_PC_CMT_spe_XXXX.xlsx", header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\"), "    
    
    df = pd.read_excel(folder_path + "/Classes_PSI_CMT_spe_XXXX.xlsx", header=1)
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