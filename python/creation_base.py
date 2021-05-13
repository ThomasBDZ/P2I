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
  numero_ine text,
  csp_mere integer,
  csp_pere integer,
  arrondissement_naissance integer,
  qualite text
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ville
  (
code_postal integer PRIMARY KEY,
nom_ville text

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS admissions
  (
Can_cod integer PRIMARY KEY,
admissible integer,
admis integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CMT_Oraux
  (
Numerodinscription integer PRIMARY KEY,
Centre text,
Jury text,
Phys integer,
Maths integer,
Entretie integer,
Anglais integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS CMT_Oraux_Spe
  (
Numerodinscription integer PRIMARY KEY,
QCM_info_phy integer,
Maths integer,
Entretien_MT integer,
QCM_Anglais integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Oraux_CCS
  (
Numerodinscription integer PRIMARY KEY,
mathematiques_1 double,
mathematiques_2 double,
phy_chi_1 double,
phy_chi_2 double,
phy_TP double,
Langue double,
S2I double

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Oraux_CCMP
  (
Numerodinscription integer PRIMARY KEY,
mathematiques integer,
physique integer,
francais integer,
anglais integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Classes_CMT_spe_XXX
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

cursor.execute('''CREATE TABLE IF NOT EXISTS Civilite
  (
civilite integer PRIMARY KEY,
  Civ_lib text

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pays
  (
 code_pays integer PRIMARY KEY,
  libele_pays text,
  nationalite text

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS concours
  (
 code_concours integer PRIMARY KEY,
  libelle_concours text,
  voie text

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS bac
  (
 numero_ine text PRIMARY KEY,
  annee_bac integer,
  mois_bac integer,
  code_serie integer,
  mention text,
  can_dep_bac integer

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS serie_bac
  (
 code_serie integer PRIMARY KEY,
  serie text

)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS csp
  (
 cod_csp integer PRIMARY KEY,
  lib_csp text

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
  anglais_exaequo double

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
  Informatique_pour_tous double
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS bonification
  (
bonification_ecrit integer,
  bonification_oral integer,
  puissance text PRIMARY KEY
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ListeEcoles
  (
NumeroEcole integer PRIMARY KEY,
  Nom_ecole text
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ListeEtablissements
  (
  Rne text PRIMARY KEY,
  type_etab text,
  nom_etabEtab text,
  Code_postal_etab integer,
  Pays_etablissement text
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS listeVoeux
  (
  Can_cod integer PRIMARY KEY,
  Voe_rang integer,
  voe_ordre integer,
  Eco_code integer
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS voie_classe
  (
 classe text PRIMARY KEY,
  voie text
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS listeEtasRe
  (
  Ata_cod integer PRIMARY KEY,
  Ata_lib text
)''')

connection.commit()
connection.close()