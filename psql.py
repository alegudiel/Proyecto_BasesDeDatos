import psycopg2

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)
#funciones de interfaz
#funcion para verificar el login
def checkUser(user, password):
    cur = con.cursor()
    cur.execute('SELECT username, pw from usuario')
    row = cur.fetchall()
    for r in row:
        if user == r[0] and password == r[1]:
            return True

#funcion para aniadir un nuevo usuario a la base
def addUser(user, password, email):
    cur = con.cursor()
    cur.execute('insert into usuario values (%s, %s, %s)', (user, password, email))
    con.commit()
    return True

#buscar cancion
def searchSong(song):
    cur = con.cursor()
    cur.execute('select id_cancion, nombre, link from cancion where id_cancion = %s', (song))
    row = cur.fetchall()
    for r in row:
        print(f"numero {r[0]}, nombre {r[1]}, link {r[2]}")

#catalogo
def catalogo():
    cur = con.cursor()
    cur.execute('select id_cancion, nombre, link from cancion order by id_cancion, nombre, link')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Cancion {r[1]}, Link {r[2]}")

#funciones de administrador que alteran la tabla
#agrega canciones a la base de datos
def agregarCancion(id, name, artist, genre, time, album, date, link):
    cur = con.cursor()
    cur.execute('insert into cancion values (%s, %s, %s, %s, %s, %s, %s, %s)', (id, name, artist, genre, time, album, date, link))

#modifica una cancion
def alterSong(song, newvalue):
    cur = con.cursor()
    cur.execute('update cancion set artist = %s where nombre = %s', (newvalue, song))

#borrar cancion
def delSong(song):
    cur = con.cursor()
    cur.execute('delete from cancion where nombre = %s', (song))

#funciones de admin, muestran valores
#albumes mas recientes
def albumesRecientes():
    cur = con.cursor()
    cur.execute('SELECT album, fecha_lanzamiento FROM cancion c WHERE c.fecha_lanzamiento BETWEEN %s and %s group by album, fecha_lanzamiento order by fecha_lanzamiento desc', ['2021-03-21', '2021-03-27'])
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

#genero mas popular
def popularGen():
    cur = con.cursor()
    cur.execute('select genero , count(genero) from Cancion group by genero order by count(genero) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Fenero {r[1]}, Canciones {r[2]}")

#usuario mas activo
def mostActive():
    cur = con.cursor()
    cur.execute('select id_user, count(id_user) from Buscador group by id_user order by count(id_user) desc limit 5')
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, id_user {r[1]}, Busquedas {r[2]}")