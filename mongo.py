import pymongo
import datetime
#conexion con la base de datos local
db = pymongo.MongoClient("mongodb+srv://admin:<admin>@cluster0.zgaqv.mongodb.net/proyecto?retryWrites=true&w=majority") 

db = myclient["proyecto"] 
listenings = db["Listenings"]

#admin puede ver las canciones reproducidas en cierta fecha
def genUserListenings(user, canciones):
    now = datetime.datetime.now()
    for x in canciones:
        listened= {
            "user": user,
            
            "listened":{
                "cancion": x[0],
                "fecha": now
            }
        }
    listenings.insert_one(listened)


#recomendacion de 10 usuarios y tracks nuevos



#herramienta inteligente tableu o microstrategy 