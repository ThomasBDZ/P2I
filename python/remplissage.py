import pandas as pd
import os
from pathlib import Path
from os.path import basename
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g

folder_path = "C:\\Users\\thoma\Documents\\TN\P2I\\project-grp12\\dow\\data\\public"
filepath_inscription = "C:\\Users\\thoma\Documents\\TN\P2I\\project-grp12\\dow\\data\\public\\Inscription.xlsx"
dico = {}
for dirpath, dirnames, filenames in os.walk(folder_path):
  for filename in filenames:
      "print(type(filename))"
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
        
"""db=get_db()
df = pd.read_excel(filepath_inscription,header=1)
rows_code_bac = df[['CODE_SERIE','SERIE']]

db.executemany("INSERT INTO serie_bac (code_serie,serie) VALUES (?, ?)", rows_code_bac)
print("Table remplie")"""


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

print(select_filiere("Classes_MP_CMT_spe_XXXX"))

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


