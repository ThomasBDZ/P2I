import sqlite3

connection = sqlite3.connect('p2i.db')
cursor = connection.cursor()



cursor.execute('''CREATE TABLE IF NOT EXISTS Candidat
  (Can_cod integer PRIMARY KEY,
  Civ_lib text,
  Nom text,
  Prenom text,
  autres_prenoms text,
  date_naissance text,
  ville_naissance text,
  code_pays_naiss integer,
  Code_pays_adr integer,
  Can_ad1 text,
  Can_ad2 text,
  Can_cod_pos integer,
  Can_mel text,
  Can_tel text,
  Can_por text,
  francais integer,
  code_pays_nationalite integer,
  classe text,
  puissance text,
  code_etablissement text,
  csp_mere integer,
  csp_pere integer,
  arrondissement_naissance integer,
  qualite text,
  FOREIGN KEY (Can_cod) REFERENCES Resultat_ecrit (Numerodinscription),
  FOREIGN KEY (Can_cod) REFERENCES Resultats_Oraux (scei),
  FOREIGN KEY (Can_cod) REFERENCES inscription (Code_Candidat),
  FOREIGN KEY (code_pays_naiss) REFERENCES pays (code_pays)
  
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ville
  (
code_postal integer PRIMARY KEY,
nom_ville text,
FOREIGN KEY(code_postal) REFERENCES Candidat (Can_cod_pos),
FOREIGN KEY(code_postal) REFERENCES ListeEtablissements (Code_postal_etab),
FOREIGN KEY (nom_ville) REFERENCES inscription (libelle_ville_ecrit)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS admissions
  (
Can_cod integer PRIMARY KEY,
admissible integer,
admis integer,

FOREIGN KEY(Can_cod) REFERENCES Candidat(Can_cod)


)''')



cursor.execute('''CREATE TABLE IF NOT EXISTS Resultats_Oraux
  (
scei integer PRIMARY KEY,
etat integer,
moyenne_generale double,
rang_classe integer,

mathematiques double,
physique double,
francais double,
anglais double,

mathematiques_1 double,
mathematiques_2 double,
phy_chi_1 double,
phy_chi_2 double,
phy_TP double,
Langue double,
S2I double,

QCM_info_phy double,
Maths double,
Entretien_MT double,
QCM_Anglais double,
bonification integer
)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Resultats_Oraux_Generaux_csv
  (
scei integer PRIMARY KEY,
etat integer,
moyenne_generale double,
rang_classe integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS inscription
  (
Code_Candidat integer PRIMARY KEY,
option1 text,
option2 text,
option3 text,
option4 text,
epreuve1 text,
epreuve2 text,
epreuve3 text,
epreuve4 text,
libelle_ville_ecrit text,
code_concours integer,
code_etat_dosssier integer,
declaration_handicap text,
sujet_tipe text

)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS pays
  (
 code_pays integer PRIMARY KEY,
  libele_pays text,

  FOREIGN KEY (code_pays) REFERENCES Candidat (code_pays_nationalite),
  FOREIGN KEY (code_pays) REFERENCES Candidat (Code_pays_adr),
  FOREIGN KEY (libele_pays) REFERENCES ListeEtablissements (Pays_etablissement)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS nation
  (
 code_pays integer PRIMARY KEY,
  nationalite text,
  FOREIGN KEY (code_pays) REFERENCES Candidat (code_pays_nationalite),
  FOREIGN KEY (code_pays) REFERENCES Candidat (Code_pays_adr)
  FOREIGN KEY (code_pays) REFERENCES pays (Code_pays)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS concours
  (
  code_concours integer PRIMARY KEY,
  libelle_concours text,
  voie text,
  FOREIGN KEY (code_concours) REFERENCES inscription (code_concours)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS bac
  (
  Can_cod integer PRIMARY KEY,
  numero_ine text,
  annee_bac integer,
  mois_bac integer,
  code_serie integer,
  mention text,
  can_dep_bac integer,
  FOREIGN KEY (numero_ine) REFERENCES Candidat (numero_ine)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS serie_bac
  (
 code_serie integer PRIMARY KEY,
  serie text,
  FOREIGN KEY (code_serie) REFERENCES bac (code_serie)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS csp
  (
 cod_csp integer PRIMARY KEY,
  lib_csp text,
  FOREIGN KEY (cod_csp) REFERENCES Candidat (csp_mere),
  FOREIGN KEY (cod_csp) REFERENCES Candidat (csp_pere)

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Oral_autres
  (
  Can_cod integer PRIMARY KEY,
  rang integer,
  maths_harmonisees double[null],
  maths_affichees double,
  max_physique double,
  max_anglais double,
  total_oral double,
  total double,
  bonus_interclassement double,
  total_interclassement double,
  entretien_exaequo double,
  anglais_exaequo double,
  FOREIGN KEY(Can_cod) REFERENCES Candidat (Can_cod)


)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Resultat_ecrit
  (
  Numerodinscription integer PRIMARY KEY,
  rang_admissible integer,
  total double,
  moyenne double,
  mathematiques_1 double,
  mathematiques_2 double,
  physique_1 double,
  physique_2 double,
  chimie double,
  Francais double,
  Informatique_SI double,
  Langue double,
  Informatique_pour_tous double,
  bonification integer
)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS ListeEcoles
  (
  NumeroEcole integer PRIMARY KEY,
  Nom_ecole text,
  FOREIGN KEY (NumeroEcole) REFERENCES listeVoeux (Eco_code)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ListeEtablissements
  (
  Rne text,
  type_etab text,
  nom_etabEtab text,
  Code_postal_etab integer,
  Pays_etablissement text,
  FOREIGN KEY (Rne) REFERENCES Candidat (code_etablissement),
  PRIMARY KEY(Rne, nom_etabEtab)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS listeVoeux
  (
  Can_cod integer,
  Voe_rang integer,
  voe_ordre integer,
  Eco_code integer,
  FOREIGN KEY(Can_cod) REFERENCES Candidat (Can_cod),
  PRIMARY KEY(Can_cod, voe_ordre)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS voie_classe
  (
 classe text PRIMARY KEY,
  voie text,
  FOREIGN KEY (voie) REFERENCES Concours (voie),
  FOREIGN KEY (classe) REFERENCES Candidat (classe)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS listeEtasRe
  (
  Ata_cod integer PRIMARY KEY,
  Ata_lib text,
  FOREIGN KEY (Ata_cod) REFERENCES inscription (code_etat_dosssier)
)''')

connection.commit()
connection.close()
