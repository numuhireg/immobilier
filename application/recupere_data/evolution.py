import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
#from sqlalchemy import cast, Numeric
#from sqlalchemy.sql.expression import cast
#Session = sessionmaker(bind = engine)
#session = Session()
from app.models import Region, Bien,TypeBien,Emplacement,Transaction,Ville


engine = create_engine('mysql+pymysql://root:root@localhost:3306/immobilier')

Session = sessionmaker(bind=engine)
session = Session()


q =(session.query(Emplacement,Ville).filter(Emplacement.code_postal_emplacement == Ville.code_postal_ville),
	func.count(Emplacement.code_postal_emplacement)
	.group_by(Emplacement.code_postal_emplacement)
	).all()
print(q)
   #print ("ID: {} Code: {} Name: {} Count: {}".format(e.id,e.code, v.name, v.count))



