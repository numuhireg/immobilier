# import de libraries
import pandas as pd
import numpy as np

def get_annee():
	year_bien = pd.read_csv(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\resutl_fr24-06-2020.csv',sep =',')
	year_group=year_bien[['Date_mutation','Valeur_fonciere','Type_local','Nombre_pieces','Code_postal','Commune','Code_departement']]
	# choix d' appartement
	bien_prix = year_group[year_group['Type_local']=='Appartement']
	bien_prix_3p_tout= bien_prix[bien_prix['Nombre_pieces']==3]
	bien_prix_3p = bien_prix_3p_tout[bien_prix_3p_tout['Valeur_fonciere']>='200000']
	
	#convertion de type en datetime
	bien_prix_3p['Dateformat'] = pd.to_datetime(bien_prix_3p['Date_mutation'])
	#bien_prix_3p_group =bien_prix_3p.groupby(['Dateformat', 'Commune'])['Valeur_fonciere'].count().reset_index().sort_values( by='Valeur_fonciere',ascending=False).head(10)
	return bien_prix_3p

	
def main():
	bien_prix_3p= get_annee()
	print(bien_prix_3p)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e