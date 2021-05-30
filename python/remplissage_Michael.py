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

# listeEtasRe   
with app.app_context():
    df = pd.read_excel(os.path.join(folder_path, "listeEtatsReponsesAppel.xlsx"), header=0)
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
    

# voie_classe
with app.app_context():
    df = pd.read_excel(os.path.join(folder_path ,"Inscription.xlsx"), header=1)
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

# listeVoeux   
with app.app_context():
    c = get_db().cursor()
    c.execute("DELETE FROM listeVoeux;")
    req = "INSERT INTO listeVoeux (Can_cod, Voe_rang, voe_ordre, Eco_code) VALUES "

    df = pd.read_excel(os.path.join(folder_path, "listeVoeux_ATS.xlsx"), header=0)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(os.path.join(folder_path, "listeVoeux_MP.xlsx"), header=0)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(os.path.join(folder_path , "listeVoeux_PC.xlsx"), header=0)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(os.path.join(folder_path, "listeVoeux_PSI.xlsx"), header=0)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
    
    df = pd.read_excel(os.path.join(folder_path , "listeVoeux_PT.xlsx"), header=0)
    tab = df.to_numpy()
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\"), "
        
    df = pd.read_excel(os.path.join(folder_path , "listeVoeux_TSI.xlsx"), header=0)
    tab = df.to_numpy()
    i = len(tab)
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\", \"{row[2]}\", \"{row[3]}\")"
        i -= 1
        if i > 0: req += ", " 
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")

# ListeEtablissements   
with app.app_context():
    df = pd.read_excel(os.path.join(folder_path , "listeEtablissements.xlsx"), header=0)
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

# ListeEcoles   
with app.app_context():
    df = pd.read_excel(os.path.join(folder_path , "listeEcoles.xlsx"), header=0)
    tab = df.to_numpy()
    c = get_db().cursor()
    c.execute("DELETE FROM ListeEcoles;") 

    i = len(tab)
    req = "INSERT INTO ListeEcoles (NumeroEcole, Nom_ecole) VALUES "
    for row in tab:
        req += f"(\"{row[0]}\", \"{row[1]}\")"
        i -= 1
        if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")

