import pandas as pd
import os
from pathlib import Path
from os.path import basename

folder_path = "C:\P2I"

dico = {}

for dirpath, dirnames, filenames in os.walk(folder_path):
  for filename in filenames:
      print(type(filename))
      FilePrefix, FileExtension = os.path.splitext(filename)
      if (FileExtension == ".xlsx"):
          dico["{0}".format(FilePrefix)] = pd.read_excel(folder_path+"\\"+basename(filename))
print(dico)
          
          


#Création de la table VILLE
"""
Inscription = pd.read_excel("C:\P2I\Inscription.xlsx")
Ville = pd.DataFrame()
Ville['CP']=Inscription['Unnamed: 14']
Ville['nom_ville'] = Inscription['Unnamed: 15']
Ville.to_excel('Ville.xlsx',index=False)

L=Ville.columns
print(L[1])


#Création de la table CANDIDAT

Admis_MP_SPE = pd.read_excel("C:\P2I\ADMIS_MP-SPE.xlsx")
Candidat = Admis_MP_SPE.copy(True)
del Candidat["rang"]
Candidat["autre_prenoms"] = Inscription['Unnamed: 3']
Candidat["francais"] = Inscription['Unnamed: 9']
Candidat["code_pays_nationalite"] = Inscription['Unnamed: 10']
Candidat["classe"] = Inscription['Unnamed: 21']
Candidat["puissance"] = Inscription['Unnamed: 22']
Candidat["code_etablissement"] = Inscription['Unnamed: 23']
Candidat["numero_ine"] = Inscription['Unnamed: 44']
Candidat["csp_mere"] = Inscription['Unnamed: 47']
Candidat["code_pays_nationalite"] = Inscription['Unnamed: 10']
Candidat["csp_pere"] = Inscription['Unnamed: 45']
Candidat["arrondissement_naissance"] = Inscription['Unnamed: 51']
Candidat["qualite"] = Inscription['Unnamed: 53']
Candidat.to_excel('Candidat.xlsx',index=False)"""

#Creation de la table CONCOURS

