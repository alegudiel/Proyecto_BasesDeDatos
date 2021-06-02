import psycopg2
import datetime 
import psql
import pymongo
import mongo

#conexion con la base de datos local
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Com") 
db = myclient["proyecto"] 
listenings = db["Listenings"]

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

print(psql.notActive())
