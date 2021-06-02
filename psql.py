import psycopg2
import datetime
from random import randint, choice, random

# conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host='queenie.db.elephantsql.com',
    database='ifgilvux',
    user='ifgilvux',
    password='MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

# funciones para contar


def countpl():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from playlist')
    row = cur.fetchall()
    for r in row:
        contador += 1
    return contador

def getUsers():
    cur = con.cursor()
    cur.execute('SELECT username from cuenta where account_state = %s', ('V'))
    row = cur.fetchall()
    newarray = []
    for x in row:
        newarray.append(x[0])
    return newarray

def countpls():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from playlist_songs')
    row = cur.fetchall()
    for r in row:
        contador += 1
    return contador


def countSearch():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from buscador')
    row = cur.fetchall()
    for r in row:
        contador += 1
    return contador


def countCuentas():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from cuenta')
    row = cur.fetchall()
    for r in row:
        contador += 1
    return contador


def countSongs():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from cancion')
    row = cur.fetchall()
    for r in row:
        contador += 1
    return contador

# funciones de interfaz
# funcion playlist


def getUserId(user):
    cur = con.cursor()
    cur.execute('select id_user from cuenta where username = %s', (user,))
    row = cur.fetchall()
    return row[0][0]


def getPlaylists(user):
    cur = con.cursor()
    cur.execute('select pl_name, id_song, nombre from playlist p inner join playlist_songs ps on p.id_playlist = ps.id_pl inner join cancion c on ps.id_song = c.id_cancion where p.pl_owner = %s', (user,))
    row = cur.fetchall()
    if len(row) > 0:
        for r in row:
            print(f"Playlist: {r[0]}, song id: {r[1]}, Song: {r[2]}")
        return True
    elif len(row) == 0:
        return False

# funcion para verificar el login


def checkUser(user, password):
    cur = con.cursor()
    cur.execute('SELECT u.username, u.pw, c.account_state from usuario u join cuenta c on u.username=c.username where u.username = %s', (user,))
    row = cur.fetchall()
    if row == []:
        print('User not found, try again. \n')
        return False
    elif (row[0][0] == user and row[0][1] != password):
        print('Incorrect Password, try again. \n')
        return False
    elif (row[0][0] == user and row[0][1] == password and row[0][2] == 'F'):
        print('Your user has been disabled.\n')
        return False
    elif (row[0][0] == user and row[0][1] == password and row[0][2] == 'V'):
        return True
    else:
        print(row)

# funcion para aniadir un nuevo usuario a la base


def addUser(user, password, email):
    cur = con.cursor()
    cur.execute('insert into usuario values (%s, %s, %s)',
                (user, password, email))
    con.commit()
    return True

# funcion para verificar la suscripcion


def checkSub(user):
    cur = con.cursor()
    cur.execute(
        'select username, user_type from cuenta where username = %s', (user,))
    row = cur.fetchall()
    if row[0][1] == 'premium':
        return 1
    if row[0][1] == 'admin':
        return 2
    if row[0][1] == 'A':
        return 3
    if row[0][1] == 'B':
        return 4
    else:
        return 5

# cambiar la suscripcion


def alterSub(username, newtype, modby):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s  where username = %s',
                (newtype, modby, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), username))
    con.commit()

# agregar una nueva suscripcion a usuarios nuevos


def newSub(username):
    rn = datetime.datetime.now()
    cuentas = countCuentas() + 1
    cur = con.cursor()
    cur.execute("insert into cuenta values(%s, %s, %s, %s, %s, %s, %s)", (cuentas,
                                                                          username, 'free', 'V', 6, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S')))
    con.commit()

# nueva busqueda


def newSearch(id, user, cancion):
    # fecha actual para guardar registro en la base de datos
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('insert into buscador values(%s, %s, %s, %s)',
                (id, user, cancion, rn.strftime('%Y-%m-%d')))
    con.commit()

# busqueda simulada


def simulSearch(id, user, cancion, dategg):
    # fecha actual para guardar registro en la base de datos
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('insert into buscador values(%s, %s, %s, %s)', (id, user, cancion, dategg))
    con.commit()


# buscar cancion


def searchSong(song):
    cur = con.cursor()
    cur.execute(
        'select id_cancion, nombre, link, active from cancion where id_cancion = %s', (song,))
    row = cur.fetchall()
    for r in row:
        if ({r[3]}) != {'V'}:
            return False
        elif ({r[3]}) == {'V'}:
            print(f"numero {r[0]}, nombre {r[1]}, link {r[2]} \n")
            return True

# catalogorolas


def catalogo():
    cur = con.cursor()
    cur.execute(
        'select id_cancion, nombre, artista from cancion order by id_cancion, nombre, link')
    row = cur.fetchall()
    for r in row:
        print("")
        print(f"{r[0]}, Song: {r[1]}, Artist: {r[2]} \n")

# catalogoalbumes


def catalogoalbumes():
    cur = con.cursor()
    cur.execute('select Album')
    row = cur.fetchall()
    for r in row:
        print(f" Album {r[0]} \n")

# catalogoartistas


def catalogoartistas():
    cur = con.cursor()
    cur.execute('select Artista from cancion')
    row = cur.fetchall()
    for r in row:
        print(f" Artist {r[0]}")


def usuarios():
    cur = con.cursor()
    cur.execute('select username from cuenta')
    row = cur.fetchall()
    for r in row:
        print(f" Username {r[0]}")
# funcion de playlists


def newPL(id, name, owner):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('insert into playlist values (%s, %s, %s, %s, %s, %s)', (id,
                                                                         name, owner, owner, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S')))
    con.commit()

# aniade cancion a playlist


def addToPL(id, pl_id, song_id):
    cur = con.cursor()
    cur.execute('insert into playlist_songs values (%s, %s, %s)',
                (id, pl_id, song_id))
    con.commit()

# funciones de administrador que alteran las tablas
# agrega canciones a la base de datos


def agregarCancion(id, name, artist, genre, time, album, date, link, modBy):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('insert into cancion values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, name,
                                                                                                artist, genre, time, album, date, link, 'V', modBy, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S')))
    con.commit()

# modifica una cancion


def alterSong(song, newvalue, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set artista = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s  where id_cancion = %s',
                (newvalue, username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), song))
    con.commit()

# modifica un album


def alteralbum(song, newvalue, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set album = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where id_cancion = %s',
                (newvalue, username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), song))
    con.commit()

# modifica una cancion


def alternameSong(song, newvalue, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set nombre = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where id_cancion = %s',
                (newvalue, username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), song))
    con.commit()

# modifica un artista


def alterartist(song, newvalue, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set artista = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where id_cancion= %s',
                (newvalue, username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), song))
    con.commit()

# inactivar cancion


def inactiveSong(song, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set active = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where id_cancion = %s',
                ('F', username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), song))
    con.commit()

# borrar album


def delalbum(album, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update Album set updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where nombre = %s',
                (username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), album))
    con.commit()
    cur.execute('delete from Album where nombre = %s', (album))

# borrar artista


def delartist(artist, username):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('update cancion set updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where artista = %s',
                (username, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), artist))
    con.commit()
    cur.execute('delete from cancion where artista = %s', (artist))
    con.commit()


def modUserType(user, type, modBY):
    rn = datetime.datetime.now()
    cur = con.cursor()
    if type == '1':
        cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where username = %s',
                    ('free', modBY, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), user))
    elif type == '2':
        cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where username = %s',
                    ('premium', modBY, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), user))
    elif type == '3':
        cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where username = %s',
                    ('admin', modBY, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), user))
    elif type == '4':
        cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where username = %s',
                    ('A', modBY, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), user))
    elif type == '5':
        cur.execute('update cuenta set user_type = %s, updated_by = %s, lastupdatedd = %s, lastupdatedt = %s where username = %s',
                    ('B', modBY, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), user))
    con.commit()

    # funciones de admin, muestran valores
# albumes mas recientes


def albumesRecientes():
    cur = con.cursor()
    cur.execute('SELECT album, fecha_lanzamiento FROM cancion c WHERE c.fecha_lanzamiento BETWEEN %s and %s group by album, fecha_lanzamiento order by fecha_lanzamiento desc', ('2021-03-21', '2021-03-27'))
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Album {r[1]}, Launched {r[2]}\n")

# artista con mayor produccion musical


def mostProd():
    cur = con.cursor()
    cur.execute(
        'select artista , count(artista) from Cancion group by artista order by count(artista) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"Artist: {r[0]},  Songs: {r[1]}\n")

# genero mas popular


def popularGen():
    cur = con.cursor()
    cur.execute(
        'select genero , count(genero) from Cancion group by genero order by count(genero) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"Genre: {r[0]}, Songs: {r[1]}\n")

# usuario mas activo


def mostActive():
    cur = con.cursor()
    cur.execute(
        'select Usuario, count(Usuario) as busquedas from Buscador group by Usuario order by count(Usuario) desc limit 5')
    row = cur.fetchall()
    for r in row:
        print(f"Username {r[0]}, Searches {r[1]}\n")

# total de reproducciones por semana


def weekViews(inicio, final, song):
    cur = con.cursor()
    cur.execute('Select nombre, count(nombre) from buscador b right join cancion c on b.id_cancion = c.id_cancion where nombre = %s and b.fecha_busqueda between %s and %s group by c.nombre order by count(c.nombre) desc', (song, inicio, final))
    row = cur.fetchall()
    for r in row:
        print(f"Song: {r[0]}, Views This week: {r[1]}\n")

# x artistas con mas reproducciones entre la fecha


def dateArtists(cant, inicio, final):
    cur = con.cursor()
    cur.execute('Select artista, count(artista) from buscador b right join cancion c on b.id_cancion = c.id_cancion where fecha_busqueda between %s and %s group by artista order by count(artista) desc limit %s', (inicio, final, cant))
    row = cur.fetchall()
    for r in row:
        print(f"\nArtista: {r[0]}, Reproducciones: {r[1]}\n")

# reproducciones de genero en las fechas ingresadas


def genreViewsIn(genre, inicio, final):
    cur = con.cursor()
    cur.execute('Select genero, count(genero) from buscador b right join cancion c on b.id_cancion = c.id_cancion where genero = %s and fecha_busqueda between %s and %s group by genero', (genre, inicio, final))
    row = cur.fetchall()
    for r in row:
        print(f"Genere: {r[0]}, Views: {r[1]}\n")

# Top x canciones con mas reproducciones de artista


def topArtistSongs(cant, artist):
    cur = con.cursor()
    cur.execute('Select nombre, artista, count(nombre) from buscador b right join cancion c on b.id_cancion = c.id_cancion where artista = %s group by nombre, artista order by count desc limit %s', (artist, cant))
    row = cur.fetchall()
    for r in row:
        print(f"Song: {r[0]}, Artist: {r[1]}, views: {r[2]}\n")

# funcion de las comisiones


def comisiones(artist, inicio, final):
    cur = con.cursor()
    cur.execute('select artista, count(artista) from cancion c left join buscador b on c.id_cancion = b.id_cancion where artista = %s and fecha_busqueda between %s and %s group by c.artista', (artist, inicio, final))
    row = cur.fetchall()
    repros = row[0][1]
    revenue = repros * 0.5
    for r in row:
        print(f'revenue for artist: {r[0]}, is: $', revenue)


def bitacora():
    cur = con.cursor()
    cur.execute('select accion, fecha, hora, username, change from bitacora b inner join cuenta c on b.updated_by = c.id_user order by fecha')
    row = cur.fetchall()
    for r in row:
        print(
            f'\nAction: {r[0]}, Date:{r[1]}, Time:{r[2]}, modified By:{r[3]}, change:{r[4]}')

#devuelve un array con las canciones escuchadas por el usuario en las fechas dadas
def userListenings(user, date):
    cur = con.cursor()
    cur.execute('select c.nombre, count(b.id_cancion) as repros from buscador b left join cancion c on b.id_cancion = c.id_cancion where usuario ilike %s and fecha_busqueda < %s group by c.nombre, b.fecha_busqueda order by b.fecha_busqueda desc', (user, date))
    row = cur.fetchall()
    return row

# funciones de la parte final (3)

def notActive():
    newarray = list()
    cur = con.cursor()
    cur.execute("select id_cancion from cancion where active = 'F'")
    row = cur.fetchall()
    for x in row:
        newarray.append(int(x[0]))
    return newarray

#para sacar las canciones random
def genSongs(qty, adminId):
    cur = con.cursor()
    rn = datetime.datetime.now()
    notActiveSongs = notActive()
    counter = 0
    while counter < qty:
        index = randint(0, len(notActiveSongs))
        newSong = notActiveSongs.pop(index)
        cur.execute("update cancion set active = 'V', updated_by = %s, lastupdatedd = %s, lastupdatedt=%s where id_cancion = %s", (adminId, rn.strftime('%Y-%m-%d'), rn.strftime('%H:%M:%S'), newSong))
    con.commit()

#para generar las reproducciones aleatorias
def genListenings(qty, date):
    counter = 0
    usuarios = getUsers()
    cantCanciones = countSongs()
    while counter <= qty:
        larola = randint(1, cantCanciones)
        newID = countSearch() +1
        simulSearch(newID, choice(usuarios), larola, date)
        counter += 1


#jalar la info del csv
def cancionesPan():
    import pandas as pd
    with open("songs.csv", encoding="utf-8" ) as f:
        texto = f.read()
    f.close()
    cancion = texto.split("\n")
