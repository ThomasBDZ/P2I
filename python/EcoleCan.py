import pandas as pd
import os
from pathlib import Path
from os.path import basename
import numpy as np
import openpyxl
import sqlite3
from flask import Flask, Blueprint, render_template, abort, request, redirect
from flask import g
from math import *


folder_path = os.path.join("dow-master", "data", "public")

Inscription = folder_path+"\\Inscription.xlsx"

tips = pd.read_excel(Inscription, header = 1)

Classe = pd.DataFrame()

ListeVoeux = pd.DataFrame()



for dirpath, dirnames, filenames in os.walk(folder_path):
    for filename in filenames:
        FilePrefix, FileExtension = os.path.splitext(filename)
        if ((FileExtension == ".xlsx") and ("CMT_spe_XXXX" in FilePrefix)):
            df_classe = pd.read_excel(os.path.join(folder_path, basename(filename)), header = 1)
            Classe = Classe.append(df_classe, ignore_index = False)
        if ((FileExtension == ".xlsx") and ("liste" in FilePrefix)):
            df_voeux = pd.read_excel(os.path.join(folder_path, basename(filename)))
            ListeVoeux = ListeVoeux.append(df_voeux, ignore_index = False)
             

Classe.rename(columns={'login':'CODE_CANDIDAT'}, inplace = True)

ListeVoeux.rename(columns={'Can _cod':'CODE_CANDIDAT'}, inplace = True)

ListeEcole = pd.read_excel(folder_path+"\\listeEcoles.xlsx")

Nbr_ecole = len(ListeEcole.index)

ListeEcole.rename(columns={'Ecole':'Eco _cod'}, inplace = True)

inner_join_df = tips[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE" ,"ETABLISSEMENT"]].merge(Classe[["CODE_CANDIDAT", "pays", "rang_classe"]], how="inner", on="CODE_CANDIDAT")

Nbr_etudiants = len(inner_join_df.index)

inner_join_df_2 = inner_join_df[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE" ,"ETABLISSEMENT", "pays", "rang_classe"]].merge(ListeVoeux[["CODE_CANDIDAT", "Voe _ord","Eco _cod"]], how="inner", on="CODE_CANDIDAT")

inner_join_df_3 = inner_join_df_2[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE" ,"ETABLISSEMENT", "pays", "rang_classe", "Voe _ord","Eco _cod"]].merge(ListeEcole[["Eco _cod", "Nom _ecole"]], how="inner", on="Eco _cod")

inner_join_df_3.sort_values(by = ["rang_classe", "Voe _ord"], ascending = [True,True], inplace = True)


EtuParEcole = ceil(Nbr_etudiants/Nbr_ecole)

EleveDejaRecu = []

DicoEcolePlace = {}
for i in ListeEcole["Nom _ecole"]:
    DicoEcolePlace[i]=0



# candidati = inner_join_df_3[inner_join_df_3["CODE_CANDIDAT"] == 80511]
# print(candidati["CODE_CANDIDAT"].index)
# print(candidati["Nom _ecole"])

# A = candidati["Nom _ecole"].iloc[1]
# print(A)

# print(DicoEcolePlace[A])

for i in inner_join_df_3["CODE_CANDIDAT"].unique():
    candidati = inner_join_df_3[inner_join_df_3["CODE_CANDIDAT"] == i]

    for j in candidati["Nom _ecole"]:
        if DicoEcolePlace[j] <= EtuParEcole:
            inner_join_df_3.loc[candidati["CODE_CANDIDAT"].index,"Ecole intégrée"] = j
            DicoEcolePlace[j] +=1
            break
    if (Le candidat n'a aucune école :):
        Prenom = inner_join_df_3.loc[candidati["CODE_CANDIDAT"].index,"PRENOM"]
        Nom = inner_join_df_3.loc[candidati["CODE_CANDIDAT"].index,"NOM"]
        print(Prenom+" "+Nom+" n'intégre aucune école.\n")


inner_join_df_3.to_excel("Innerjoin.xlsx", index=False)
