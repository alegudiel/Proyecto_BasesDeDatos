import psycopg2
import datetime
import psql
import pymongo
import random

# conexion con la base de datos local
myclient = pymongo.MongoClient(
    "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Com")
db = myclient["proyecto"]
listenings = db["Listenings"]

# conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host='queenie.db.elephantsql.com',
    database='ifgilvux',
    user='ifgilvux',
    password='MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

# counter = 0
# usuarios = psql.getUsers()
# cantCanciones = psql.countSongs()
# start_date = datetime.date(2020, 1, 1)
# end_date = datetime.date(2021, 5, 31)
# time_between_dates = end_date - start_date
# days_between_dates = time_between_dates.days
# while counter < 200:
#     random_number_of_days = random.randrange(days_between_dates)
#     random_date = start_date + datetime.timedelta(days=random_number_of_days)
#     newID = psql.countSearch() + 1
#     larola = random.randint(1, cantCanciones)
#     psql.simulSearch(newID, random.choice(usuarios), larola, random_date)
print(psql.usersRecommends())