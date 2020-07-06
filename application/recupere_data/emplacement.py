import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy import cast, Numeric
#from sqlalchemy.sql.expression import cast
#import sqlalchemy as db
from app.models import Region, Bien,TypeBien,Emplacement


engine = create_engine('mysql+pymysql://root:root@localhost:3306/immobilier')

Session = sessionmaker(bind=engine)
session = Session()


q = (session.query(Emplacement.code_postal_emplacement, cast(Emplacement.latitude_emplacement,Numeric(10, 4)),cast(Emplacement.longitude_emplacement,Numeric(10, 4)),
	func.count(Emplacement.code_postal_emplacement))
    .group_by(Emplacement.code_postal_emplacement)
     ).all()
print(type(q))
print(q)


