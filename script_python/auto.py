#!/usr/bin/env python

import pandas as pd, re, os, requests, datetime
from models import Region, Departement, Ville, TypeBien, Transaction, Emplacement, Bien, db
from datetime import datetime
from geopy.geocoders import Nominatim



DATA_PATHFILE = "data/marche_immobilier.csv"

class Geocoder:
    # Here will be the instance stored.
    __instance = None
    __geolocator = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Geocoder.__instance == None:
            Geocoder()
        return Geocoder.__instance 

    @staticmethod
    def get_location(address_string):
        Geocoder.getInstance()
        latitude, longitude = (None, None)
        try:
            location = Geocoder.__geolocator.geocode(address_string)
            latitude, longitude = location.latitude, location.longitude
        except Exception as e:
            raise e
        return latitude, longitude

    def __init__(self):
        """ Virtually private constructor. """
        if Geocoder.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Geocoder.__instance = self
            Geocoder.__geolocator = Nominatim()

def format_address(numero, type_voie, nom_voie, code_postal, city):
    nom_voie = re.sub(r'^CHEM\s', '', nom_voie)
    type_voie = re.sub(r'^CHE$', 'CHEMIN', type_voie)
    type_voie = re.sub(r'^MTE$', 'MONTÉE', type_voie)
    type_voie = re.sub(r'^LOT$', 'LOTISSEMENT', type_voie)
    type_voie = re.sub(r'^RES$', 'RESIDENCE', type_voie)
    return f"{numero} {type_voie} {nom_voie}, {code_postal} {city}"


def insert_transaction():
    df = pd.read_csv(DATA_PATHFILE)
    dfTransaction = df[['Date_mutation', 'Valeur_fonciere']]

    # Get the unique values (rows)
    dfTransaction = dfTransaction.drop_duplicates()
    dfTransaction.columns = ['date', 'prix']
    datetime_format = '%d/%m/%Y'
    print(dfTransaction.head())
    dfTransaction = dfTransaction.dropna()
    
    for _, row in dfTransaction.iterrows():
        # date_string = row['date']
        date = datetime.strptime(row['date'], datetime_format)
        prix = float(row['prix'].replace(',', '.')) if isinstance(row['prix'], str) else row['prix']
        transaction = Transaction(date=date, prix=prix)
        db.session.add(transaction)
    db.session.commit() # This is needed to write the changes to database
    
    # print(df.iloc[:3])

def insert_emplacement():
    df = pd.read_csv(DATA_PATHFILE)
    df = df.dropna()
    df = df.drop_duplicates()
    # df = df.head(32)
    print(len(df.index))
    for _, row in df.iterrows():
        city = row['Commune']
        code_postal = int(row['Code_postal'])
        nombre_voie = int(row['No voie'])
        type_voie = row['Type de voie']
        nom_voie = row['Voie']

        address_string = format_address(nombre_voie, type_voie, nom_voie, code_postal, city)
        try:
            ville = db.session.query(Ville).filter_by(code_postal=code_postal, nom=city).first()
            latitude, longitude = Geocoder.get_location(address_string)
            emplacement = Emplacement(code_postal=code_postal, nombre_voie=nombre_voie, type_voie=type_voie, rue=nom_voie, latitude=latitude, longitude=longitude, complete=address_string, ville=ville)
            db.session.add(emplacement)
            db.session.commit()
            # print(f"({latitude}, {longitude}) -- #{type_voie}# #{nom_voie}# {address_string}")
        except Exception as e:
            # print(f"{e.args}")
            db.session.rollback()
            pass
        finally:
            db.session.close()

def insert_bien():
    df = pd.read_csv(DATA_PATHFILE)
    df = df.dropna()
    df = df.drop_duplicates()
    datetime_format = '%d/%m/%Y'
    for _, row in df.iterrows():
        date = datetime.strptime(row['Date_mutation'], datetime_format)
        prix = float(row['Valeur_fonciere'].replace(',', '.')) if isinstance(row['Valeur_fonciere'], str) else row['Valeur_fonciere']
        transaction = db.session.query(Transaction).filter_by(date=date, prix=prix).first()

        local_type = row['Type_local']
        type_bien = db.session.query(TypeBien).filter_by(local_type=local_type).first()

        city = row['Commune']
        code_postal = int(row['Code_postal'])
        numero_voie = int(row['No voie'])
        type_voie = row['Type de voie']
        nom_voie = row['Voie']

        complete_address = format_address(numero_voie, type_voie, nom_voie, code_postal, city)
        print(complete_address)
        try:
            emplacement = db.session.query(Emplacement).filter_by(complete=complete_address).first()

            numero_plan = row['No plan']
            surface_bati = float(row['Surface reelle bati'])
            surface_non_bati = float(row['Surface terrain'])
            nombre_pieces = int(row['Nombre_pieces'])
            bien = Bien(numero_plan=numero_plan, surface_bati=surface_bati, surface_non_bati=surface_non_bati, nombre_pieces=nombre_pieces, transaction=transaction, type_bien=type_bien, emplacement=emplacement)
            db.session.add(bien)
            db.session.commit()
        except Exception as e:
            print(f"{e.args}")
            db.session.rollback()
            pass
        finally:
            db.session.close()

def download():
    if not os.path.exists("data"):
        os.makedirs("data")

    now = datetime.datetime.now()
    url = f'https://static.data.gouv.fr/resources/demandes-de-valeurs-foncieres/20200416-115822/valeursfoncieres-{now.year}.txt'
    data = requests.get(url, allow_redirects = True)
    with open(DATA_PATHFILE, "wb") as fp:
        fp.write(data.content)
    return os.stat(DATA_PATHFILE).st_size != 0

def main():
    if download():
        insert_transaction()
        insert_emplacement()
        insert_bien()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        raise e
