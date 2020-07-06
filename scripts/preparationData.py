#Import the necessary libraries
import pandas as pd
import numpy as np
from datetime import date

# Lecture de fichier csv sauvegarde sur mon pc
result_contat= pd.read_csv(r'D:\Bureau\Formation Simplon\immobilier_paris\immob_v1\dataImmobilier_fr.csv',sep = ',' )

commune_geographique= pd.read_csv(r'D:\Bureau\Formation Simplon\immobilier_paris\données_francais\communes2020.csv',sep = ',' )
departement= pd.read_csv(r'D:\Bureau\Formation Simplon\immobilier_paris\données_francais\departements-francais.csv',sep =',')
region_name= pd.read_csv(r'D:\Bureau\Formation Simplon\immobilier_paris\données_francais\regions-francaises.csv',sep =',')
# Nombre de ville trouve dans dataframe
commune= result_contat.groupby(['Code departement','Code postal','Commune']).size().reset_index(name='counts').sort_values( by='counts',ascending = False)

# NOMBRE DE COMMUNE EXISTANT DANS MES DONNEES
len(commune)
# Séléction de certaine colonnes
ville =commune[['Code departement','Code postal','Commune']]

# verification des commune unique
len(ville.Commune.unique())

# renome la colonne d'intersection avec le dataframe commune_geographique 
ville_renome =ville.rename(columns={'Code departement':'dep'})
ville_renome
#merge entre ville et commune_geographique

region = pd.merge(ville_renome,df_geographie,on='dep')


#preparation table bien
bien  = result_contat[['No plan','Surface reelle bati','Surface terrain','Nombre pieces principales']]
#remplacer les NAN pour eviter les soucis de chargements
bien_cleaned= bien.fillna(0)

#preparation table type_bien
type_bien = result_contat[['No plan','Type local','Code type local']]
type_bien_sql= type_bien.groupby(['Type local','Code type local']).size().reset_index(name='counts').sort_values( by='counts',ascending = False)
type_bien_sql=type_bien_sql[['Type local','Code type local']]

#preparation table transaction
transaction = result_contat[['No plan','Date mutation','Valeur fonciere']]
transaction['nbr_date'] = transaction['Date mutation'].str.split('/')
transaction[['jour','mois','annee']] = pd.DataFrame(transaction.nbr_date.tolist(), index= transaction.index)
transaction_final=transaction[['jour','mois','annee','Valeur fonciere']]

#preparation departement
dep_result= result_contat.groupby(['Code departement']).size().reset_index(name='counts')
dep = departement[['Identifiant;NUMÉRO_departement','CHEF;LIEU','REGION']]
dep['nbr_dep'] = dep['Identifiant;NUMÉRO_departement'].str.split(';')
dep[['dep_nbr_deb','code_dep']] = pd.DataFrame(dep.nbr_dep.tolist(), index= dep.index)
dep_immob = pd.merge(commune, dep, left_on="Code departement", right_on="code_dep")
departement_modified = dep_immob[['Code departement','CHEF;LIEU','REGION']]
dep_ok = pd.merge(departement_modified,departements, left_on="REGION", right_on="REGION")
# preparation table region
regions= region_name[['Code INSEE5','Région','Nombre de départements']]

#preparation table emplacement
address_geo= pd.read_excel(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\adress_text.xlsx',sep =',')
emplacement_sql=address_geo[['Code postal','Latitude','Longitude']]
emplacement_test= pd.merge(emplacement_sql,result_contat,how='left' ,on=['Code postal'])
ok_emplacement=emplacement_test[['Code postal','No voie','Type de voie','Voie','Latitude','Longitude']]


