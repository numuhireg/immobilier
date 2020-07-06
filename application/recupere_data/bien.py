import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from app.models import Region, Bien,TypeBien


engine = create_engine('mysql+pymysql://root:root@localhost:3306/immobilier')

Session = sessionmaker(bind=engine)
session = Session()


#biens = session.query(Bien.type_bien_id_type).distinct()
#for b in biens.all():
#	print(b)

q = (session.query(Bien.type_bien_id_type, 
	func.count(Bien.type_bien_id_type))
    .group_by(Bien.type_bien_id_type)
     ).all()
print(type(q))
print(q)


