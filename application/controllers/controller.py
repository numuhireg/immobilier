# import de libraries
import pandas as pd
import numpy as np

def get_emplacement():
	emplacement = pd.read_csv(r'D:\Bureau\Formation Simplon\projet_chef_oeuvre\fichier_charg_sql\emplacefinal04-06-2020.csv',sep =',')
	emplacement_geo=emplacement .groupby(['code','latitude','longitude']).size().reset_index(name='counts').sort_values( by='counts',ascending = False)
	lat = emplacement_geo['latitude'].tolist()
	long = emplacement_geo['longitude'].tolist()
	count = emplacement_geo['counts'].tolist()
	location = np.array(list(zip(lat,long)))
	return location, count

	
def main():
	location, count = get_emplacement()
	print(f"{location}\t{count}")

if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		raise e