from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager (app)
manager.add_command('db', MigrateCommand)

class Bien(db.Model):
    __tablename__ = 'bien'

    id = db.Column(db.Integer, primary_key=True)
    nbr_plan = db.Column(db.Integer)
    surface_bati_bien = db.Column(db.String(255))
    surface_non_bati_bien = db.Column(db.String(255))
    piece_bien = db.Column(db.Integer)



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

if __name__=="__main__":
    try:
        manager.run()
    except:
        pass