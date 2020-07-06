#Import the necessary libraries

from geopy.geocoders import Nominatim
import pandas as pd
import numpy as np
from pprint import pprint
import requests
from datetime import date
#chargement de données

emplacement_v2= pd.read_csv(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\emplacement22-05-2020.csv',sep = ',' )

# verification de code postal existant dans mes données
emplacement_v2['Code postal'].nunique() 

#groupe pour recuperer les codes postal et leur counts

emplacement_v3 =emplacement_v2.groupby(["Code postal","Commune"]).size().reset_index(name='counts').sort_values( by='counts',ascending = False)

#mettre les code postal dans un array
emplacement_v3['Code postal'].unique()
# url du data.gov 
url = 'https://api-adresse.data.gouv.fr'
# recuperation du premiere code postal pour test

data = requests.get(url+'/search/?q=postcode=75016.0')
data.json() 

# recupere tout les code postal et le mettre en  array
coordinates = [] 
for postcode in emplacement_v3['Code postal'] :
    data = requests.get(url+'/search/?q=postcode={}'.format(postcode))
    coord = data.json()['features'][0]['geometry']['coordinates']
    coordinates.append(coord) 
	print(coordinates)
# verifier la longeur
len(coordinates)

# convertion en dataframe
data_postal = pd.DataFrame(coordinates)

# concantener les deux dataframe

emplacement_concat=pd.merge(emplacement_postal,data_postal, how ='inner', on='Code postal')
emplacement_concat

