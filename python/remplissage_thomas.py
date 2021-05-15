from numpy import NAN, NaN, nan
import pandas as pd
import os
from pathlib import Path
from os.path import basename
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g
from collections import OrderedDict

folder_path = "..\dow-master\data\public"
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



database= "p2i.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db



def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


with app.app_context():

    #TABLE SERIE BAC
    print("Remplissage table : Serie bac")

    c = get_db().cursor()
    # df = pd.read_excel(filepath_inscription,header=1)
    # rows_code_bac = []
    # for index,rows in df.iterrows():
    #     rows_code_bac.append([rows['CODE_SERIE'],rows['SERIE']])
    # c.executemany("INSERT OR IGNORE INTO serie_bac (code_serie,serie) VALUES (?, ?)", (rows_code_bac))
    # c.execute("COMMIT;")

    print("Table remplie")

    #TABLE ADMISSION

    print('Remplissage table : Admission')

    c.execute("DELETE FROM admissions;") 
    df = pd.read_excel(filepath_inscription,header=1)
    req = "INSERT INTO admissions (Can_cod, admissible, admis) VALUES "
    tab = df.to_numpy()
    
    dic = {}
    for row in tab:
        dic[row[0]] = [row[0]]
        dic[row[0]].append(nan)
        dic[row[0]].append(nan)
    
    df = dico["ADMISSIBLE_MP-SPE"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]][1]=row[0]
    df = dico["ADMIS_MP-SPE"]
    tab = df.to_numpy()
    for row in tab:
        dic[row[0]][2]=row[12]

    i = len(dic)
    print(i)
    for x in dic:
        req += f"(\"{x}\",  \"{dic[x][1]}\", \"{dic[x][2]})\""
        i -= 1
        if i > 0: req += ", "
    req += ";"

    # for dirpath, dirnames, filenames in os.walk(folder_path):
    #     for filename in filenames:
    #         FilePrefix, FileExtension = os.path.splitext(filename)
    #         if ("ADMISSIBLE" in FilePrefix) and ("SPE" in FilePrefix) and ("ADMISSIBLE_ATS" not in FilePrefix) and ("ADMISSIBLE_PC" not in FilePrefix): 
    #             df = dico['ADMISSIBLE_'+select_filiere(FilePrefix)]
    #             tab = df.to_numpy()
    #             for row in tab:
    #                 dic[row[0]][1]=row[0]

            # if ("ADMIS_" in FilePrefix) and ("SPE" in FilePrefix) and ("ADMIS_ATS" not in FilePrefix) and ("ADMIS_PC" not in FilePrefix):
            #     df = dico['ADMIS_'+select_filiere(FilePrefix)]
            #     tab = df.to_numpy()
            #     for row in tab:
            #         dic[row[0]][2]=row[12]
                    #dic[row[0]].append(row[12])
     # 3 pb : le premier dans filiere PC,un can_cod introuvable dans Inscription (44232 je crois) +2e pb : longueur de liste variante dans dic + sqlite3.OperationalError: parser stack overflow
    

    #c.executemany("INSERT OR IGNORE INTO admissions (Can_cod, admissible, admis) VALUES (?, ?, ?)", dic)
    c.execute(req)
    c.execute("COMMIT;")

    print('Table remplie')





