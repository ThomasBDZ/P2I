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

app = Flask(__name__)
# filepath_inscription = "..\\..\\dow-master\\data\\public\\Inscription.xlsx"
# dico = {}
# for dirpath, dirnames, filenames in os.walk(folder_path):
#   for filename in filenames:
#       "print(type(filename))"
#       FilePrefix, FileExtension = os.path.splitext(filename)
#       if (FileExtension == ".xlsx"):
#           dico["{0}".format(FilePrefix, index=False)] = pd.read_excel(folder_path+"\\"+basename(filename))

# df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
# print(df.to_numpy()[0][0])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(database)
    return db



def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
        
# db=get_db()
# df = pd.read_excel(filepath_inscription,header=1)
# rows_code_bac = df[['CODE_SERIE','SERIE']]

# db.executemany("INSERT INTO serie_bac (code_serie,serie) VALUES (?, ?)", rows_code_bac)
# print("Table remplie")

database= "p2i.db"

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

# print(select_filiere("Classes_MP_CMT_spe_XXXX"))

def born_stop(L):
    aux = []
    R = []
    for i in L:
        if i =='STOP':
            R.append(aux)
            aux = []
            continue
        aux.append(i)
    return(R)


# df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
# tab = df.to_numpy()
# c = get_db().cursor()

# req = "INSERT INTO table (col1, col2, col3) VALUES "
# for row in tab:
#     req += f"({row[x]}, {row[y]}, {row[z]}),"
# req[-1] = ";"
# c.execute(req)


# df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
# tab = df.to_numpy()
# c = get_db().cursor()

# dic = {}
# for row in tab:
#     dic[row[x]] = [row[y], row[z]]
# req = "INSERT INTO table (col1, col2, col3) VALUES "
# for x in dic:
#         req += f"({x}, {dic[x][0]}, {dic[x][1]}),"
# req[-1] = ";"
# c.execute(req)


# df1 = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
# df2 = pd.read_excel(folder_path + "\\ADMISSIBLE_MP.xlsx", header=1)
# tab1 = df1.to_numpy()
# tab2 = df2.to_numpy()
# c = get_db().cursor()

# dic = {}
# for row in tab1:
#     dic[row[pk]] = [row[y], row[z]]
# for row in tab2:
#     dic[row[pk]].append(row[v]) #il faudra peut être changer le pk, car on est dans un tab différent
#     dic[row[pk]].append(row[w])
# req = "INSERT INTO table (col1, col2, col3, col4, col5) VALUES "
# for pk in dic:
#         req += f"({pk}, {dic[x][0]}, {dic[x][1]}, {dic[x][2]}, {dic[x][3]}),"
# req[-1] = ";"
# c.execute(req)


# with app.app_context():
#     df = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
#     tab = df.to_numpy()
#     c = get_db().cursor()

#     req = "INSERT INTO bac (numero_ine, annee_bac, mois_bac, code_serie, mention, can_dep_bac) VALUES "
#     i = len(tab)
#     for row in tab:
#         req += f"(\"{row[0]}\", \"{row[38]}\", \"{row[39]}\", \"{row[40]}\", \"{row[42]}\", \"{row[54]}\")"
#         i -= 1
#         if i > 0: req += ", " 
#     req += ";"
#     c.execute(req)
#     c.execute("COMMIT;")


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


with app.app_context():
    df1 = pd.read_excel(folder_path + "\\Inscription.xlsx", header=1)
    df2 = pd.read_excel(folder_path + "\\ADMISSIBLE_MP.xlsx", header=1)
    tab1 = df1.to_numpy()
    tab2 = df2.to_numpy()
    c = get_db().cursor()

    dic = {}
    for row in tab1:
        dic[row[pk]] = [row[y], row[z]]
    for row in tab2:
        dic[row[pk]].append(row[v]) #il faudra peut être changer le pk, car on est dans un tab différent
        dic[row[pk]].append(row[w])
    req = "INSERT INTO table (col1, col2, col3, col4, col5) VALUES "
    i = len(dic)
    for pk in dic:
            req += f"(\"{pk}\", \"{dic[x][0]}\", \"{dic[x][1]}\", \"{dic[x][2]}\", \"{dic[x][3]})\""
            i -= 1
            if i > 0: req += ", "
    req += ";"
    c.execute(req)
    c.execute("COMMIT;")