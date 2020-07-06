# import de libraries
import pandas as pd
import numpy as np

def get_ville():
	ville = pd.read_csv(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\ville_updet31-05-2020.csv',sep =',')
	ville_empl = pd.read_csv(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\emplpost-fr04-06-2020.csv',sep =',')
	ville_merge =pd.merge(ville,ville_empl, how='inner', left_on ='Code postal' ,right_on='Code postal')
	ville_count=ville_merge[['Commune','counts']].head(10)
	
	return ville_count

	
def main():
	ville_count= get_ville()
	print (ville_count)

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e