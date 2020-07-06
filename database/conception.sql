### effacer le database

drop database immobilier;

#### creation de database
create database immobilier;

use immobilier;

 ### creation table region
 
DROP TABLE IF EXISTS region ;
CREATE TABLE region (id_reg INT AUTO_INCREMENT NOT NULL,
code_INSEE_region INT(11) NOT NULL ,
nom_region_region VARCHAR(50),
nbr_dep_region INT(11),
PRIMARY KEY (id_reg)) ENGINE=InnoDB;


### creatation table type_bien

DROP TABLE IF EXISTS type_bien;

CREATE TABLE type_bien (id_type INT AUTO_INCREMENT NOT NULL,
 local_type VARCHAR(50),
 code_type INT(11),
 PRIMARY KEY (id_type)) ENGINE=InnoDB;


###creation table departement
# donner un mon specifique

DROP TABLE IF EXISTS departement ;
CREATE TABLE departement (id_dep INT AUTO_INCREMENT NOT NULL,
code_dep VARCHAR(25),
nom_dep_departement VARCHAR(25),
code_INSEE_region VARCHAR(11),
region_id_reg INT(11),
PRIMARY KEY (id_dep)
) ENGINE=InnoDB;


### creation table ville

DROP TABLE IF EXISTS ville ;
CREATE TABLE ville (id_ville INT AUTO_INCREMENT NOT NULL,
code_dep VARCHAR(25),
code_postal_ville INT(25),
nom_ville VARCHAR(50),
departement_id_dep INT(11),
PRIMARY KEY (id_ville)) ENGINE=InnoDB;
 

###creation table emplacement


DROP TABLE IF EXISTS emplacement ;
CREATE TABLE emplacement (id_emp INT AUTO_INCREMENT NOT NULL,
code_postal_emplacement INT(11),
nbr_voie VARCHAR (11),
type_voie VARCHAR (25),
rue_emplacement VARCHAR(50),
latitude_emplacement VARCHAR(25),
longitude_emplacement VARCHAR(25),
id_ville INT (11),
PRIMARY KEY (id_emp)) ENGINE=InnoDB;

###  creatation table  bien

DROP TABLE IF EXISTS bien ;

CREATE TABLE bien (id_bien INT AUTO_INCREMENT NOT NULL,
 nbr_plan INT (25),
 surface_bati_bien FLOAT(25),
 surface_non_bati_bien FLOAT(25),
 piece_bien INT(25),
 type_bien_id_type INT(11),
 emplacement_id_emp INT(11),
 PRIMARY KEY (id_bien)) ENGINE=InnoDB;
 
 

### creation table transaction

DROP TABLE IF EXISTS transaction ;
CREATE TABLE transaction (id_trans INT AUTO_INCREMENT NOT NULL,
jour_date VARCHAR (25),
mois_date VARCHAR(25),
annee_date VARCHAR(25),
prix_bien VARCHAR(50),
PRIMARY KEY (id_trans)) ENGINE=InnoDB;

### creation une table de liaison  N to N bien_has_transaction

DROP TABLE IF EXISTS bien_has_transaction ;
CREATE TABLE IF NOT EXISTS bien_has_transaction (
bien_id_bien INT(11) NOT NULL,
bien_type_bien_id_type INT(11) NOT NULL,
transaction_id_trans INT(11) NOT NULL,
PRIMARY KEY (bien_id_bien, bien_type_bien_id_type, transaction_id_trans))ENGINE=InnoDB;

## ajouter la clé secondaire sur la table departement

ALTER TABLE departement
 ADD CONSTRAINT FK_departement_region FOREIGN KEY (region_id_reg) REFERENCES region(id_reg);
 
### ajoute cle secondaire sur la table ville

ALTER TABLE ville
ADD CONSTRAINT fk_ville_departement FOREIGN KEY (departement_id_dep) REFERENCES departement(id_dep);

### ajoute cle secondaire sur la table emplacement

ALTER TABLE emplacement
ADD CONSTRAINT fk_emplacement_ville FOREIGN KEY (id_ville) REFERENCES ville(id_ville);

### ajoute cle secondaire table bien
 ALTER TABLE bien
 ADD CONSTRAINT FK_bien_type_bien FOREIGN KEY (type_bien_id_type) REFERENCES type_bien (id_type);
 
 ALTER TABLE bien
 ADD CONSTRAINT FK_bien_emplacement FOREIGN KEY (emplacement_id_emp) REFERENCES emplacement (id_emp);
 

###  ajoute les cles secondaire sur la tarable de liason 
  
ALTER TABLE bien_has_transaction
ADD CONSTRAINT fk_bien_has_transaction_transaction FOREIGN KEY (transaction_id_trans) REFERENCES transaction(id_trans);

ALTER TABLE bien_has_transaction
ADD CONSTRAINT fk_bien_has_transaction_bien FOREIGN KEY (bien_id_bien) REFERENCES bien(id_bien);


## chargement table region

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/region-fr08-05-2020.csv"
into table immobilier.region
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code_INSEE_region,nom_region_region, nbr_dep_region);


## chargement table type_bien irihuta cyane


LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/type_local.csv"
into table immobilier.type_bien
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(local_type,Code_type);


## chargement table transaction

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/transaction19-05-2020.csv"
into table immobilier.transaction
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(jour_date,mois_date,annee_date,prix_bien);

## chargement table departement

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/departement_upted.csv"
into table immobilier.departement
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code_dep,nom_dep_departement,code_INSEE_region,region_id_reg);


## chargement table ville

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/ville_updet31-05-2020.csv"
into table immobilier.ville
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code_dep,code_postal_ville,nom_ville,departement_id_dep);


## chargement table  emplacement test
LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/emplacefinal04-06-2020.csv"
into table immobilier.emplacement
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code_postal_emplacement,nbr_voie,type_voie,rue_emplacement,latitude_emplacement,longitude_emplacement,id_ville);



## chargement du table bien iratinda igir 4 min

LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/bien31-05-2020.csv"
into table immobilier.bien
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(nbr_plan,surface_bati_bien,surface_non_bati_bien,piece_bien,type_bien_id_type,emplacement_id_emp);


LOAD DATA INFILE "C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/b_h_t31-05-2020.csv"
into table immobilier.bien_has_transaction
Fields TERMINATED by ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(bien_id_bien, bien_type_bien_id_type, transaction_id_trans);






