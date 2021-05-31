import psycopg2
import datetime 
import psql
import pymongo
import mongo

#conexion con la base de datos local
myclient = pymongo.MongoClient("mongodb+srv://admin:<admin>@cluster0.zgaqv.mongodb.net/proyecto?retryWrites=true&w=majority") 
db = myclient["proyecto"] 
listenings = db["Listenings"]

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

NewTracks = [['Ay3', 'Ayo & Teo', 'Trap', '3:15', 'Ay3'],
            ['Glimmer', 'LIONE' 'Chill', '4:21', 'Glimmer'],
            ['Last Time', 'Lxst', 'Trap', '2:49', 'Lost'],
            ['When I Get There', 'Big Gigantic', 'Chill', '3:40', 'Invincible EP'],
            ['Youth', 'Dabin', 'Chill', '4:24', 'Wild Youth'],
            ['Incomplete', 'Aero Chord', 'Chill', '4:18', 'Incomplete'],
            ['Get Your Wish', 'Porter Robinson', 'Chill', '3:38', 'Nurture'],
            ['Do You Understand?', 'Shy Glizzy','Trap', '4:39', 'Do You Understand?'],
            ['Explore', 'Cosa Ky', 'Trap', '3:36', 'Explore'],
            ['Lust', 'Lil Skies', 'Trap', '2:36', 'Life of A Dark Rose'],
            ['MICHUUL', 'Duckwrth', 'Pop', '3:06', 'an XTRA UGLY Mixtape'],
            ['Stars', 'Sky', 'Pop', '3:50', 'Stars'],
            ['Brutal', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Good 4 u', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Traitor', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Drivers license', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Deja vu', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Enough for you', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['1 step forward 3 steps back', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Happier', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Favorite crime', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Hope ur ok', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Jealousy jealousy', 'Olivia Rodrigo', 'pop', '3:41', 'sour'],
            ['Ni bien ni mal', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['200 mph', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Quien tu eres', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Caro', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Tenemos que hablar', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Otra noche en Miami', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Ser bichote', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Si estuviésemos juntos', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Solo de mi', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Cuando perriabas', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['La Romana', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Como antes', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Estamos bien', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['Mia', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre'],
            ['RLNDT', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre']]

