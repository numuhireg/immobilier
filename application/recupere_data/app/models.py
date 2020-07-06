# coding: utf-8

from app import db
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy



class Bien(db.Model):
    __tablename__ = 'bien'

    id_bien = db.Column(db.Integer, primary_key=True)
    nbr_plan = db.Column(db.Integer)
    surface_bati_bien = db.Column(db.Float(asdecimal=True))
    surface_non_bati_bien = db.Column(db.Float(asdecimal=True))
    piece_bien = db.Column(db.Integer)
    type_bien_id_type = db.Column(db.Integer)
    emplacement_id_emp = db.Column(db.Integer)




class Departement(db.Model):
    __tablename__ = 'departement'

    id = db.Column(db.Integer, primary_key=True)
    code_dep = db.Column(db.String(25))
    nom_dep_departement = db.Column(db.String(255))
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship("Region", back_populates="departement")



class Emplacement(db.Model):
    __tablename__ = 'emplacement'

    id = db.Column(db.Integer, primary_key=True)
    code_postal_emplacement = db.Column(db.Integer)
    nbr_voie = db.Column(db.String(25))
    type_voie = db.Column(db.String(25))
    rue_emplacement = db.Column(db.String(255))
    latitude_emplacement = db.Column(db.String(255))
    longitude_emplacement = db.Column(db.String(255))



class Region(db.Model):
    __tablename__ = 'region'

    id = db.Column(db.Integer, primary_key=True)
    code_INSEE_region = db.Column(db.Integer, nullable=False)
    nom_region_region = db.Column(db.String(255))
    nbr_dep_region = db.Column(db.Integer)
    departement = db.relationship("Departement", backref="region")



class Transaction(db.Model):
    __tablename__ = 'transaction'

    id = db.Column(db.Integer, primary_key=True)
    jour_date = db.Column(db.String(25))
    mois_date = db.Column(db.String(25))
    annee_date = db.Column(db.String(25))
    prix_bien = db.Column(db.String(255))


class TypeBien(db.Model):
    __tablename__ = 'type_bien'

    id = db.Column(db.Integer, primary_key=True)
    local_type = db.Column(db.String(255))
    code_type = db.Column(db.Integer)



class Ville(db.Model):
    __tablename__ = 'ville'

    ID = db.Column(db.Integer, primary_key=True)
    code_dep = db.Column(db.String(25))
    code_postal_ville = db.Column(db.Integer)
    nom_ville = db.Column(db.String(255))
