# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Bien(db.Model):
    __tablename__ = 'bien'

    id_bien = db.Column(db.Integer, primary_key=True)
    nbr_plan = db.Column(db.Integer)
    surface_bati_bien = db.Column(db.Float(asdecimal=True))
    surface_non_bati_bien = db.Column(db.Float(asdecimal=True))
    piece_bien = db.Column(db.Integer)
    type_bien_id_type = db.Column(db.Integer)
    emplacement_id_emp = db.Column(db.Integer)



class BienHasTransaction(db.Model):
    __tablename__ = 'bien_has_transaction'

    bien_id_bien = db.Column(db.Integer, primary_key=True, nullable=False)
    bien_type_bien_id_type = db.Column(db.Integer, primary_key=True, nullable=False)
    transaction_id_trans = db.Column(db.Integer, primary_key=True, nullable=False)



class Departement(db.Model):
    __tablename__ = 'departement'

    id_dep = db.Column(db.Integer, primary_key=True)
    code_dep = db.Column(db.String(25))
    nom_dep_departement = db.Column(db.String(25))
    code_INSEE_region = db.Column(db.String(11))
    region_id_reg = db.Column(db.ForeignKey('region.id_reg'), index=True)

    region = db.relationship('Region', primaryjoin='Departement.region_id_reg == Region.id_reg', backref='departements')



class Emplacement(db.Model):
    __tablename__ = 'emplacement'

    id_emp = db.Column(db.Integer, primary_key=True)
    code_postal_emplacement = db.Column(db.Integer)
    nbr_voie = db.Column(db.String(11))
    type_voie = db.Column(db.String(25))
    rue_emplacement = db.Column(db.String(50))
    latitude_emplacement = db.Column(db.String(25))
    longitude_emplacement = db.Column(db.String(25))
    id_ville = db.Column(db.Integer)



class Region(db.Model):
    __tablename__ = 'region'

    id_reg = db.Column(db.Integer, primary_key=True)
    code_INSEE_region = db.Column(db.Integer, nullable=False)
    nom_region_region = db.Column(db.String(50))
    nbr_dep_region = db.Column(db.Integer)



class Transaction(db.Model):
    __tablename__ = 'transaction'

    id_trans = db.Column(db.Integer, primary_key=True)
    jour_date = db.Column(db.String(25))
    mois_date = db.Column(db.String(25))
    annee_date = db.Column(db.String(25))
    prix_bien = db.Column(db.String(50))



class TypeBien(db.Model):
    __tablename__ = 'type_bien'

    id_type = db.Column(db.Integer, primary_key=True)
    local_type = db.Column(db.String(50))
    code_type = db.Column(db.Integer)



class Ville(db.Model):
    __tablename__ = 'ville'

    id_ville = db.Column(db.Integer, primary_key=True)
    code_dep = db.Column(db.String(25))
    code_postal_ville = db.Column(db.Integer)
    nom_ville = db.Column(db.String(50))
    departement_id_dep = db.Column(db.ForeignKey('departement.id_dep'), index=True)

    departement = db.relationship('Departement', primaryjoin='Ville.departement_id_dep == Departement.id_dep', backref='villes')
