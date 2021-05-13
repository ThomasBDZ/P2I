BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "GrandsAnciens" (
	"ID"	INTEGER NOT NULL,
	"Nom"	TEXT NOT NULL UNIQUE,
	"Titre"	TEXT NOT NULL,
	"Description"	TEXT NOT NULL,
	"ImagePath"	TEXT NOT NULL,
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "Hobbies" (
	"ID"	INTEGER NOT NULL,
	"Nom"	TEXT NOT NULL UNIQUE,
	"Description"	TEXT NOT NULL,
	PRIMARY KEY("ID")
);
CREATE TABLE IF NOT EXISTS "GrandsAnciensZHobbies" (
	"GrandsAnciens_ID"	INTEGER NOT NULL,
	"Hobbies_ID"	INTEGER NOT NULL,
	"time"	INTEGER NOT NULL,
	PRIMARY KEY("GrandsAnciens_ID","Hobbies_ID"),
	FOREIGN KEY("GrandsAnciens_ID") REFERENCES "GrandsAnciens"("ID"),
	FOREIGN KEY("Hobbies_ID") REFERENCES "Hobbies"("ID")
);
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (1,'Abhoth','La source de l''impurete','bouillie infame ou l''on discerne d''improbables organes','images/Abhoth.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (2,'Azathoth','Le dieu aveugle et stupide','monstrueux chaos nucleaire se contorsionnant sans cesse au son d''une flute','images/Azathoth.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (3,'Cthulhu','Le Seigneur de R''lyeh','Humanoide a tete de poulpe','images/Cthulhu.png');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (4,'Dagon','Le Profond','Humanoide a tete de poisson','images/Dagon.jpeg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (5,'Hastur','Le Roi en Jaune','Humanoide dans une cape jaune avec des tentacules','images/Hastur.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (6,'Nyarlathothep','le Chaos Rampant','un homme en noir','images/Nyarlathothep.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (7,'Rhan-Tegoth','Celui assis sur le trone d''ivoire','méduse insectoide','images/RhanTegoth.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (8,'Shoggoths','Les esclaves','amas gelatineux munis d''yeux et de dents acerees','images/Shoggoths.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (9,'Shub-Niggurath','La chevre noire des bois aux mille chevreaux','masse nuageuse en ebullition','images/ShubNiggurath.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (10,'Tsathoggua','Dormeur de N''kai','crapaud velu','images/Tsathoggua.jpg');
INSERT INTO "GrandsAnciens" ("ID","Nom","Titre","Description","ImagePath") VALUES (11,'YogSothoth','Le tout en un et un en tout','conglomerat de globes iridescents toujours fluctuants','images/YogSothoth.jpg');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (1,'Macrame','Facile avec des tentacules');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (2,'Scrabble','Pas le droit aux noms propres');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (3,'Mots croises','Dans de multiples dimensions non euclidiennes bien sur');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (4,'Belote','Yog Sothoth est interdit de belote car il triche');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (5,'Cuisine','Vous ne voulez pas connaitre la recette');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (6,'Lecture','Le Necronomicon bien entendu');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (7,'Peinture','Qu''avec la couleur tombee du ciel');
INSERT INTO "Hobbies" ("ID","Nom","Description") VALUES (8,'Reseaux sociaux','La mailing list des cultistes a un succes fou');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('1','2','54');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('1','4','21');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('1','5','15');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('1','6','71');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('1','7','90');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('2','1','2');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('2','7','4');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('2','8','67');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','1','73');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','2','76');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','3','7');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','4','76');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','5','72');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('3','6','20');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('4','1','66');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('4','2','28');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('4','3','34');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('4','6','60');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('4','8','88');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('5','1','21');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('5','4','45');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('5','5','68');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('5','7','26');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('6','3','40');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('6','4','56');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('6','5','30');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('7','1','75');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('7','2','86');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('7','4','86');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('7','6','12');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('7','7','64');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('8','6','3');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('8','8','33');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('9','1','60');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('9','3','85');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('9','4','31');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('9','6','56');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('10','1','82');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('10','2','11');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('10','3','9');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('10','6','29');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('11','1','8');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('11','4','31');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('11','7','91');
INSERT INTO "GrandsAnciensZHobbies" ("GrandsAnciens_ID","Hobbies_ID","time") VALUES ('11','8','45');
COMMIT;
