import pymongo
#conexion con la base de datos local
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Com") 
db = myclient["proyecto"] 
listenings = db["Listenings"]

#admin puede ver las canciones reproducidas en cierta fecha
def genUserListenings(user, canciones):
    listened = dict()
    for x in canciones:
        listened.update({x[0]: x[1]})
    perUser = {'user':user, 'listenings':listened}
    listenings.insert_one(perUser)

#recomendacion de 10 usuarios y tracks nuevos



#herramienta inteligente tableu o microstrategy 