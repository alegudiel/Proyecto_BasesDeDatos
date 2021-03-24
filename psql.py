import psycopg2

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

#funciones de interfaz
def checkUser(user, password):
    cur = con.cursor()
    cur.execute('SELECT username, pw from usuario')
    row = cur.fetchall()
    for r in row:
        if user == r[0] and password == r[1]:
            return True

#funciones de administrador que alteran la tabla
#agrega canciones a la base de datos
def agregarCancion(id, name, artist, genre, time, album, date, link):
    cur = con.cursor()
    cur.execute('insert into cancion values ($s, $s, $s, $s, $s, $s, $s, $s)', (id, name, artist, genre, time, album, date, link))
    cur.close

#modifica una cancion
def alterSong(song, newvalue):
    cur = con.cursor()
    cur.execute('update cancion set artist = $s where nombre = $s', (newvalue, song))

#borrar cancion
def delSong(song):
    cur = con.cursor()
    cur.execute('delete from cancion where nombre = $s', (song))

#funciones de admin, muestran valores
#albumes mas recientes
def albumesRecientes():
    cur = con.cursor()
    cur.execute('SELECT album, fecha_lanzamiento FROM cancion c WHERE c.fecha_lanzamiento BETWEEN $s and $s group by album, fecha_lanzamiento order by fecha_lanzamiento desc', ['2021-03-21', '2021-03-27'])
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Album {r[1]}, Lanzamiento {r[2]}")

#artista con mayor produccion musical
def mostProd():
    cur = con.cursor()
    cur.execute('select artista , count(artista) from Cancion group by artista order by count(artista) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Artista {r[1]}, Lanzamientos {r[2]}")

def popularGen():
    cur = con.cursor()
    cur.execute('select genero , count(genero) from Cancion group by genero order by count(genero) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Fenero {r[1]}, Canciones {r[2]}")

def mostActive():
    cur = con.cursor()
    cur.execute('select id_user, count(id_user) from Buscador group by id_user order by count(id_user) desc limit 5')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, id_user {r[1]}, Busquedas {r[2]}")


#cerrar la conexion
#con.close()