import datetime
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import sqlalchemy as db
from app.models import Region, Bien,TypeBien


engine = create_engine('mysql+pymysql://root:root@localhost:3306/immobilier')

Session = sessionmaker(bind=engine)
session = Session()

'''
region = session.query(Region.code_INSEE_region).distinct()
for r in region.all():
	print(r)
'''


# create a Session
connection = engine.connect()
metadata = db.MetaData()
region = db.Table('region', metadata, autoload=True, autoload_with=engine)
# Print the column names
r = region.select()
result = connection.execute(r)
print(result)
for row in result:
   print (row)
