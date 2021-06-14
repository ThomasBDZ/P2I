from typing import final
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
        if ((FileExtension == ".xlsx") and ("listeVoe" in FilePrefix)):
            df_voeux = pd.read_excel(os.path.join(folder_path, basename(filename)))
            ListeVoeux = ListeVoeux.append(df_voeux, ignore_index = False)

Classe.rename(columns={'login':'CODE_CANDIDAT'}, inplace = True)

ListeVoeux.rename(columns={'Can _cod':'CODE_CANDIDAT'}, inplace = True)

ListeEcole = pd.read_excel(folder_path+"\\listeEcoles.xlsx")

Nbr_ecole = len(ListeEcole.index)

ListeEcole.rename(columns={'Ecole':'Eco _cod'}, inplace = True)

inner_join_df = tips[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE", "LIBELLE_PAYS", "CODE_PAYS","ETABLISSEMENT"]].merge(Classe[["CODE_CANDIDAT","n_demi","total_avec_interclassement", "rang_classe"]], how="inner", on="CODE_CANDIDAT")

Nbr_etudiants = len(inner_join_df.index)

inner_join_df_2 = inner_join_df[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE" ,"ETABLISSEMENT", "LIBELLE_PAYS", "CODE_PAYS","n_demi","total_avec_interclassement", "rang_classe"]].merge(ListeVoeux[["CODE_CANDIDAT", "Voe _ord","Eco _cod"]], how="inner", on="CODE_CANDIDAT")

inner_join_df_3 = inner_join_df_2[["CODE_CANDIDAT", "NOM", "PRENOM", "VOIE" ,"ETABLISSEMENT", "LIBELLE_PAYS", "CODE_PAYS","n_demi","total_avec_interclassement","rang_classe", "Voe _ord","Eco _cod"]].merge(ListeEcole[["Eco _cod", "Nom _ecole"]], how="inner", on="Eco _cod")

inner_join_df_3.sort_values(by = ["rang_classe", "Voe _ord"], ascending = [True,True], inplace = True)


EtuParEcole = ceil(Nbr_etudiants/Nbr_ecole) #Ici 26 élèves par école


DicoEcolePlace = {}
for i in ListeEcole["Nom _ecole"]:
    DicoEcolePlace[i]=0


for i in inner_join_df_3["CODE_CANDIDAT"].unique():
    candidati = inner_join_df_3[inner_join_df_3["CODE_CANDIDAT"] == i] #select where code_candidat = i

    for j in candidati["Nom _ecole"]:
        if DicoEcolePlace[j] <= EtuParEcole:
            inner_join_df_3.loc[candidati["CODE_CANDIDAT"].index,"Ecole intégrée"] = j
            DicoEcolePlace[j] +=1
            break

ListeIntegre = pd.DataFrame(columns = inner_join_df_3.columns)

k=1
for i in inner_join_df_3["CODE_CANDIDAT"].unique():
    candidati = inner_join_df_3[inner_join_df_3["CODE_CANDIDAT"] == i]
    ListeIntegre.loc[k] = (candidati.loc[candidati.index[0]])
    k+=1

ListeIntegre.to_excel("ListeDesIntegres.xlsx", index=False)


#################################################################################################################
## ICI ON CREE LA TABLE QUI NOUS PERMET DE FAIRE LA CARTE GEOGRAPHIQUE DES INTEGRES ##
#################################################################################################################

dico_pays = {}
dico_pays["Gabon"] = "ga","-1.0000","11.7500"
dico_pays["Maroc"] = "ma","32.0000","-5.0000"
dico_pays["Tunisie"] = "tn","34.0000","9.0000"
dico_pays["Japon"] = "jp","36.0000","138.0000"
dico_pays["Côte D'Ivoire"] = "ci", "8.0000","-5.0000"
dico_pays["Espagne"] = "es","40.0000","-4.0000"
dico_pays["Luxembourg"] = "lu", "49.7500","6.1667"
dico_pays["Canada"] = "ca","60.0000","-95.0000"
dico_pays["Mauritanie"] = "mr","20.0000","-12.0000"
dico_pays["Monaco"] = "mc", "43.7333","7.4000"
dico_pays["Pakistan"] = "pk", "30.0000","70.0000"
dico_pays["Grande-Bretagne"] = "gb","54.0000","-2.0000"
dico_pays["Allemagne"] = "de", "51.0000","9.0000"
dico_pays["Andorre"] = "ad","42.5000","1.5000"
dico_pays["Liban"] = "lb","33.8333","35.8333"
dico_pays["Sénégal"] = "sn","14.0000","-14.0000"
dico_pays["Etats-Unis"] = "us","38.0000","-97.0000"
dico_pays["Belgique"] = "be","50.8333","4.0000"
dico_pays["Italie"] = "it","42.8333","12.8333"


Listepays = []
ListeEcole = ['LIBELLE_PAYS', 'country_id','latitude','longitude']
Codepays = []
latitude =[]
longitude = []

for i in inner_join_df_3["LIBELLE_PAYS"].unique():
    Listepays.append(i)

for i in inner_join_df_3["Ecole intégrée"].unique():
    ListeEcole.append(i)

for row in Listepays:
    Codepays.append(dico_pays[row][0])
    latitude.append(dico_pays[row][1])
    longitude.append(dico_pays[row][2])



final = pd.DataFrame({
     'LIBELLE_PAYS':
     Listepays,
     'country_id':
     Codepays,
     'latitude':
     latitude,
     'longitude':
     longitude
 }, index=Listepays, columns=ListeEcole)
final = final.fillna(0) # Remplie le tableau avec des 0


for i in inner_join_df_3["CODE_CANDIDAT"].unique():
    candidati = inner_join_df_3[inner_join_df_3["CODE_CANDIDAT"] == i]
    A = candidati["LIBELLE_PAYS"]
    for a in A.unique():
        for j in candidati["Ecole intégrée"].unique():
            final.loc[a,j] +=1

            break

final.to_csv("Admis_geo.csv", index=False)