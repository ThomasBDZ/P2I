CREATE TABLE `Candidat` (
  `Can_cod` integer PRIMARY KEY AUTO_INCREMENT,
  `Civ_lib` varchar(255),
  `Nom` varchar(255),
  `Prenom` varchar(255),
  `autres_prenoms` varchar(255),
  `date_naissance` text,
  `ville_naissance` varchar(255),
  `code_pays_naiss` integer,
  `Code_pays_adr` integer,
  `Can_ad1` varchar(255),
  `Can_ad2` varchar(255),
  `Can_cod_pos` integer,
  `Can_mel` varchar(255),
  `Can_tel` varchar(255),
  `Can_por` varchar(255),
  `francais` integer,
  `code_pays_nationalite` integer,
  `classe` varchar(255),
  `puissance` varchar(255),
  `code_etablissement` varchar(255),
  `numero_ine` text,
  `csp_mere` integer,
  `csp_pere` integer,
  `arrodissement_naissance` integer,
  `qualite` varchar(255)
);

CREATE TABLE `nation` (
  `code_pays` integer,
  `nationalite` varchar(255)
);

CREATE TABLE `ville` (
  `Can_cod_pos` integer PRIMARY KEY AUTO_INCREMENT,
  `Can_com` varchar(255)
);

CREATE TABLE `admissibleV2` (
  `Can_cod` integer[pk],
  `rang` integer
);

CREATE TABLE `admisV2` (
  `Can_cod` integer[pk],
  `rang` integer
);

CREATE TABLE `CMT_Oraux_YYYY_MP` (
  `Numerodinscription` varchar(255) PRIMARY KEY,
  `Centre` varchar(255),
  `Jury` varchar(255),
  `Phys` integer,
  `Maths` integer,
  `Entretien` integer,
  `Anglais` integer
);

CREATE TABLE `Classes_MP_CMT_spe_XXX` (
  `scei` integer PRIMARY KEY,
  `nom` varchar(255),
  `etat` integer,
  `total_oral` double,
  `total_points` double,
  `moyenne_generale` double,
  `rang_classe` integer
);

CREATE TABLE `Ecrit_MPV2` (
  `Can_cod` integer[pk],
  `rang` integer
);

CREATE TABLE `inscriptionv2` (
  `Code_Candidat` varchar(255) PRIMARY KEY,
  `option1` varchar(255),
  `option2` varchar(255),
  `option3` varchar(255),
  `option4` varchar(255),
  `libelle_ville_ecrit` varchar(255),
  `code_concours` integer,
  `code_etat_dosssier` integer,
  `declaration_handicap` varchar(255),
  `sujet_tipe` varchar(255)
);

CREATE TABLE `Civilite` (
  `civilite` integer,
  `Civ_lib` varchar(255)
);

CREATE TABLE `CodePostal` (
  `CP` integer PRIMARY KEY,
  `ville` varchar(255)
);

CREATE TABLE `pays` (
  `code_pays` integer PRIMARY KEY,
  `libele_pays` varchar(255)
);

CREATE TABLE `classe` (
  `classe` varchar(255) PRIMARY KEY,
  `epreuve1` varchar(255),
  `epreuve2` varchar(255),
  `epreuve3` varchar(255),
  `epreuve4` varchar(255)
);

CREATE TABLE `Concours` (
  `code_concours` integer PRIMARY KEY,
  `libelle_concours` varchar(255),
  `voie` varcahr
);

CREATE TABLE `bac` (
  `numero_ine` text PRIMARY KEY,
  `annee_bac` integer,
  `mois_bac` integer,
  `code_serie` integer,
  `mention` varchar(255),
  `can_dep_bac` integer
);

CREATE TABLE `serie_bac` (
  `code_serie` integer PRIMARY KEY,
  `serie` varchar(255)
);

CREATE TABLE `csp` (
  `cod_csp` integer PRIMARY KEY,
  `lib_csp` varchar(255)
);

CREATE TABLE `OralV2` (
  `Can_cod` integer[pk],
  `rang` integer
);

CREATE TABLE `Resultat_ecrit` (
  `Numerodinscription` integer PRIMARY KEY,
  `rang` integer,
  `total` double,
  `moyenne` double,
  `bonification` integer,
  `mathematiques` double,
  `ScPhysiques` double,
  `Francais` double,
  `SciencesIndustrielles` double,
  `Anglais` double
);

CREATE TABLE `bonification` (
  `bonification` integer,
  `puissance` texte PRIMARY KEY
);

CREATE TABLE `ListeEcoles` (
  `NumeroEcole` integer PRIMARY KEY,
  `Nom_ecole` varchar(255)
);

CREATE TABLE `ListeEtablissements` (
  `Rne` texte PRIMARY KEY,
  `type_etab` varchar(255),
  `nom_etabEtab` varchar(255),
  `Code_postal_etab` integer,
  `Pays_etablissement` varchar(255)
);

CREATE TABLE `listeVoeux_MP` (
  `Can_cod` integer PRIMARY KEY,
  `Voe_rang` integer,
  `voer_ordre` integer,
  `Eco_code` integer
);

CREATE TABLE `voie_classe` (
  `classe` varchar(255),
  `voie` varchar(255)
);

CREATE TABLE `listeEtasRe` (
  `Ata_cod` integer,
  `Ata_lib` varchar(255)
);

ALTER TABLE `admissibleV2` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Candidat` (`Can_cod`);

ALTER TABLE `admisV2` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Candidat` (`Can_cod`);

ALTER TABLE `Candidat` ADD FOREIGN KEY (`Can_cod`) REFERENCES `CMT_Oraux_YYYY_MP` (`Numerodinscription`);

ALTER TABLE `Ecrit_MPV2` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Candidat` (`Can_cod`);

ALTER TABLE `OralV2` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Candidat` (`Can_cod`);

ALTER TABLE `ville` ADD FOREIGN KEY (`Can_cod_pos`) REFERENCES `Candidat` (`Can_cod_pos`);

ALTER TABLE `listeVoeux_MP` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Candidat` (`Can_cod`);

ALTER TABLE `ville` ADD FOREIGN KEY (`Can_cod_pos`) REFERENCES `ListeEtablissements` (`Code_postal_etab`);

ALTER TABLE `Concours` ADD FOREIGN KEY (`code_concours`) REFERENCES `inscriptionv2` (`code_concours`);

ALTER TABLE `serie_bac` ADD FOREIGN KEY (`code_serie`) REFERENCES `bac` (`code_serie`);

ALTER TABLE `Candidat` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Resultat_ecrit` (`Numerodinscription`);

ALTER TABLE `Candidat` ADD FOREIGN KEY (`Can_cod`) REFERENCES `Classes_MP_CMT_spe_XXX` (`scei`);

ALTER TABLE `Candidat` ADD FOREIGN KEY (`Can_cod`) REFERENCES `inscriptionv2` (`Code_Candidat`);

ALTER TABLE `pays` ADD FOREIGN KEY (`code_pays`) REFERENCES `Candidat` (`code_pays_nationalite`);

ALTER TABLE `pays` ADD FOREIGN KEY (`code_pays`) REFERENCES `nation` (`code_pays`);

ALTER TABLE `voie_classe` ADD FOREIGN KEY (`classe`) REFERENCES `classe` (`classe`);

ALTER TABLE `voie_classe` ADD FOREIGN KEY (`voie`) REFERENCES `Concours` (`voie`);

ALTER TABLE `voie_classe` ADD FOREIGN KEY (`classe`) REFERENCES `Candidat` (`classe`);

ALTER TABLE `bonification` ADD FOREIGN KEY (`puissance`) REFERENCES `Candidat` (`puissance`);

ALTER TABLE `csp` ADD FOREIGN KEY (`cod_csp`) REFERENCES `Candidat` (`csp_mere`);

ALTER TABLE `csp` ADD FOREIGN KEY (`cod_csp`) REFERENCES `Candidat` (`csp_pere`);

ALTER TABLE `ville` ADD FOREIGN KEY (`Can_com`) REFERENCES `inscriptionv2` (`libelle_ville_ecrit`);

ALTER TABLE `Civilite` ADD FOREIGN KEY (`Civ_lib`) REFERENCES `Candidat` (`Civ_lib`);

ALTER TABLE `pays` ADD FOREIGN KEY (`code_pays`) REFERENCES `Candidat` (`Code_pays_adr`);

ALTER TABLE `classe` ADD FOREIGN KEY (`classe`) REFERENCES `Candidat` (`classe`);

ALTER TABLE `bac` ADD FOREIGN KEY (`numero_ine`) REFERENCES `Candidat` (`numero_ine`);

ALTER TABLE `ListeEcoles` ADD FOREIGN KEY (`NumeroEcole`) REFERENCES `listeVoeux_MP` (`Eco_code`);

ALTER TABLE `pays` ADD FOREIGN KEY (`libele_pays`) REFERENCES `ListeEtablissements` (`Pays_etablissement`);

ALTER TABLE `ListeEtablissements` ADD FOREIGN KEY (`Rne`) REFERENCES `Candidat` (`code_etablissement`);

ALTER TABLE `listeEtasRe` ADD FOREIGN KEY (`Ata_cod`) REFERENCES `inscriptionv2` (`code_etat_dosssier`);
