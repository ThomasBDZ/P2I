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

print("Remplissage table : Resultats_Oraux_Generaux_csv")
with app.app_context():  
    c = get_db().cursor()
    req = "INSERT INTO Resultats_Oraux_Generaux_csv (scei, etat, moyenne_generale, rang_classe) VALUES "

    df = pd.read_csv(os.path.join(folder_path, "Classes_MP_CMT_spe_XXXX_SCEI.csv"), sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(os.path.join(folder_path, "Classes_PC_CMT_spe_XXXX_SCEI.csv"), sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(os.path.join(folder_path, "Classes_PSI_CMT_spe_XXXX_SCEI.csv"), sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
    df = pd.read_csv(os.path.join(folder_path, "Classes_PT_CMT_spe_XXXX_SCEI.csv"), sep=";")
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
   
    df = pd.read_csv(os.path.join(folder_path, "Classes_TSI_CMT_spe_XXXX_SCEI.csv"), sep=";")
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

print("Remplissage table :Resultats_Oraux avec : Oraux_CCMP")
with app.app_context():  
    c = get_db().cursor()
    req = "INSERT INTO Resultats_Oraux (scei, mathematiques, physique, francais, anglais, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais) VALUES "

    df = pd.read_excel(os.path.join(folder_path, "Classes_MP_CMT_spe_XXXX.xlsx"), header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "
 
    df = pd.read_excel(os.path.join(folder_path, "Classes_PC_CMT_spe_XXXX.xlsx"), header=1)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\"), "
    
    df = pd.read_excel(os.path.join(folder_path, "Classes_PSI_CMT_spe_XXXX.xlsx"), header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[33]}\", \"{row[34]}\", \"{row[35]}\", \"{row[36]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")

print("Remplissage table : Resultats_Oraux avec : Oraux_CCS")
with app.app_context():
    df = pd.read_excel(os.path.join(folder_path, "Classes_TSI_CMT_spe_XXXX.xlsx"), header=1)
    tab = df.to_numpy()
    c = get_db().cursor()

    req = "INSERT INTO Resultats_Oraux (scei, mathematiques_1, mathematiques_2, phy_chi_1, phy_chi_2, phy_TP, Langue, S2I, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais) VALUES "
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[28]}\", \"{row[29]}\", \"{row[30]}\", \"{row[31]}\", \"{row[32]}\", \"{row[33]}\", \"{row[34]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")   

print("Remplissage table : Resultats_Oraux")
with app.app_context():  
    c = get_db().cursor()
    req = "INSERT INTO Resultats_Oraux (scei, QCM_info_phy, Maths, Entretien_MT, QCM_Anglais) VALUES "

    # df = pd.read_excel(os.path.join(folder_path, "Classes_MP_CMT_spe_XXXX.xlsx"), header=1)
    # tab = df.to_numpy()
    # for row in tab:
    #     req += f"(\"{row[0]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "
    
    # df = pd.read_excel(os.path.join(folder_path, "Classes_PC_CMT_spe_XXXX.xlsx"), header=1)
    # tab = df.to_numpy()
    # for row in tab:
    #     req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\"), "    
    
    # df = pd.read_excel(os.path.join(folder_path, "Classes_PSI_CMT_spe_XXXX.xlsx"), header=1)
    # tab = df.to_numpy()
    # for row in tab:
    #     req += f"(\"{row[0]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\", \"{row[28]}\"), "    
    
    df = pd.read_excel(os.path.join(folder_path, "Classes_PT_CMT_spe_XXXX.xlsx"), header=1)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\") "    
        i -= 1
        if i > 0: req += ", "
    req += ";"
    # df = pd.read_excel(os.path.join(folder_path, "Classes_TSI_CMT_spe_XXXX.xlsx"), header=1)
    # tab = df.to_numpy()
    # i = len(tab)
    # for row in tab:
    #     req += f"(\"{row[0]}\", \"{row[24]}\", \"{row[25]}\", \"{row[26]}\", \"{row[27]}\")"
    #     i -= 1
    #     if i > 0: req += ", " 
    # req += ";"
    c.execute(req)
    c.execute("COMMIT;")
print("Table remplie")

# print("Remplissage table : CMT_Oraux")
# with app.app_context():  
#     c = get_db().cursor()
#     req = "INSERT INTO Resultats_Oraux (scei, etat, moyenne_generale, rang_classe) VALUES "

#     df = pd.read_csv(os.path.join(folder_path, "Classes_MP_CMT_spe_XXXX_SCEI.csv"), sep=";")
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_csv(os.path.join(folder_path, "Classes_PC_CMT_spe_XXXX_SCEI.csv"), sep=";")
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_csv(os.path.join(folder_path, "Classes_PSI_CMT_spe_XXXX_SCEI.csv"), sep=";")
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
    
#     df = pd.read_csv(os.path.join(folder_path, "Classes_PT_CMT_spe_XXXX_SCEI.csv"), sep=";")
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\"), "
   
#     df = pd.read_csv(os.path.join(folder_path, "Classes_TSI_CMT_spe_XXXX_SCEI.csv"), sep=";")
#     tab = df.to_numpy()
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[2]}\", \"{row[5]}\", \"{row[6]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")
# print("Table remplie") 

# # listeEtasRe   
# with app.app_context():
#     df = pd.read_excel(os.path.join(folder_path, "listeEtatsReponsesAppel.xlsx"), header=0)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM listeEtasRe;") 

#     i = len(tab)
#     req = "INSERT INTO listeEtasRe (Ata_cod, Ata_lib) VALUES "
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\")"
#         i -= 1
#         if i > 0: req += ", "
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")
    

# # voie_classe
# with app.app_context():
#     df = pd.read_excel(os.path.join(folder_path ,"Inscription.xlsx"), header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM voie_classe;") 

#     dic = {}
#     for row in tab:
#         dic[row[21]] = row[37]
#     req = "INSERT INTO voie_classe (classe, voie) VALUES "
#     i = len(dic)
#     for x in dic:
#         req += f"(\"{x}\", \"{dic[x]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req  += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# # listeVoeux   
# with app.app_context():
#     c = get_db().cursor()
#     c.execute("DELETE FROM listeVoeux;")
#     req = "INSERT INTO listeVoeux (Can_cod, Voe_rang, voe_ordre, Eco_code) VALUES "

#     df = pd.read_excel(os.path.join(folder_path, "listeVoeux_ATS.xlsx"), header=0)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
#     df = pd.read_excel(os.path.join(folder_path, "listeVoeux_MP.xlsx"), header=0)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
#     df = pd.read_excel(os.path.join(folder_path , "listeVoeux_PC.xlsx"), header=0)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
#     df = pd.read_excel(os.path.join(folder_path, "listeVoeux_PSI.xlsx"), header=0)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
#     df = pd.read_excel(os.path.join(folder_path , "listeVoeux_PT.xlsx"), header=0)
#     tab = df.to_numpy()
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
        
#     df = pd.read_excel(os.path.join(folder_path , "listeVoeux_TSI.xlsx"), header=0)
#     tab = df.to_numpy()
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# # ListeEtablissements   
# with app.app_context():
#     df = pd.read_excel(os.path.join(folder_path , "listeEtablissements.xlsx"), header=0)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM ListeEtablissements;") 

#     i = len(tab)
#     req = "INSERT INTO ListeEtablissements (Rne, type_etab, nom_etabEtab, Code_postal_etab, Pays_etablissement) VALUES "
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\", \"{row[4]}\")"
#         i -= 1
#         if i > 0: req += ", "
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

# # ListeEcoles   
# with app.app_context():
#     df = pd.read_excel(os.path.join(folder_path , "listeEcoles.xlsx"), header=0)
#     tab = df.to_numpy()
#     c = get_db().cursor()
#     c.execute("DELETE FROM ListeEcoles;") 

#     i = len(tab)
#     req = "INSERT INTO ListeEcoles (NumeroEcole, Nom_ecole) VALUES "
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[1]}\")"
#         i -= 1
#         if i > 0: req += ", "
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")

