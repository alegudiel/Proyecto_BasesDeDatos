import psycopg2
import datetime 

#conexion a la base de datos que esta en elephntsql
con = psycopg2.connect(
    host = 'queenie.db.elephantsql.com',
    database = 'ifgilvux',
    user = 'ifgilvux',
    password = 'MRUyQ-aHX7MHs_nHxahu98Yy0yaXEiGr',
)

############################funciones para contar 
def countpl():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from playlist')
    row = cur.fetchall()
    for r in row:
        contador +=1
    return contador

def countpls():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from playlist_songs')
    row = cur.fetchall()
    for r in row:
        contador +=1
    return contador

def countSearch():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from buscador')
    row = cur.fetchall()
    for r in row:
        contador +=1
    return contador

def countCuentas():
    contador = 0
    cur = con.cursor()
    cur.execute('SELECT * from cuenta')
    row = cur.fetchall()
    for r in row:
        contador +=1
    return contador


############################funciones de interfaz
#funcion playlist
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

#funcion para verificar el login
def checkUser(user, password):
    cur = con.cursor()
    cur.execute('SELECT u.username, u.pw, c.account_state from usuario u join cuenta c on u.username=c.username')
    row = cur.fetchall()
    for r in row:
        if user == r[0] and password == r[1] and r[2] == 'V':
            return True
        if r[2] != 'V':
            print('Your user has been disabled.\n')

#funcion para aniadir un nuevo usuario a la base
def addUser(user, password, email):
    cur = con.cursor()
    cur.execute('insert into usuario values (%s, %s, %s)', (user, password, email))
    con.commit()
    return True

#funcion para verificar la suscripcion
def checkSub(user):
    cur = con.cursor()
    cur.execute('select username, user_type from cuenta where username = %s', (user,))
    row = cur.fetchall()
    if row[0][1] == 'premium':
        return 1
    if row[0][1] == 'admin':
        return 2
    if row[0][1] == 'monitorA':
        return 3
    if row[0][1] == 'monitorB':
        return 4
    else:
        return 5

#cambiar la suscripcion
def alterSub(username, newtype):
    cur = con.cursor()
    cur.execute('update cuenta set user_type = %s where username = %s', (newtype, username))
    con.commit()

#agregar una nueva suscripcion a usuarios nuevos
def newSub(username):
    cuentas = countCuentas() + 1
    cur = con.cursor()
    cur.execute("insert into cuenta values(%s, %s, %s, %s)", (cuentas, username, 'free', 'V'))
    con.commit()

#nueva busqueda
def newSearch(id, user, cancion):
    rn = datetime.datetime.now()
    cur = con.cursor()
    cur.execute('insert into buscador values(%s, %s, %s, %s)', (id, user, cancion, rn.strftime('%Y-%m-%d')))
    con.commit()

#buscar cancion
def searchSong(song):
    cur = con.cursor()
    cur.execute('select id_cancion, nombre, link, active from cancion where id_cancion = %s', (song,))
    row = cur.fetchall()
    for r in row:
        if ({r[3]}) != {'V'}:
            return False
        elif ({r[3]}) == {'V'}:
            print(f"numero {r[0]}, nombre {r[1]}, link {r[2]} \n")
            return True

#catalogorolas
def catalogo():
    cur = con.cursor()
    cur.execute('select id_cancion, nombre, artista from cancion order by id_cancion, nombre, link')
    row = cur.fetchall()
    for r in row:
        print("")
        print(f"{r[0]}, Song: {r[1]}, Artist: {r[2]} \n")

#catalogoalbumes
def catalogoalbumes():
    cur = con.cursor()
    cur.execute('select Album')
    row = cur.fetchall()
    for r in row:
        print(f" Album {r[0]} \n")

#catalogoartistas
def catalogoartistas():
    cur = con.cursor()
    cur.execute('select Artist')
    row = cur.fetchall()
    for r in row:
        print(f" Artist {r[0]}")
    
#funcion de playlists
def newPL(id, name, owner):
    cur = con.cursor()
    cur.execute('insert into playlist values (%s, %s, %s)', (id, name, owner))
    con.commit()

#aniade cancion a playlist
def addToPL(id, pl_id, song_id):
    cur = con.cursor()
    cur.execute('insert into playlist_songs values (%s, %s, %s)', (id, pl_id, song_id))
    con.commit()

############################funciones de administrador que alteran las tablas
#agrega canciones a la base de datos
def agregarCancion(id, name, artist, genre, time, album, date, link):
    cur = con.cursor()
    cur.execute('insert into cancion values (%s, %s, %s, %s, %s, %s, %s, %s, %s)', (id, name, artist, genre, time, album, date, link, 'V'))

#modifica una cancion
def alterSong(song, newvalue):
    cur = con.cursor()
    cur.execute('update cancion set artista = %s where id_cancion = %s', (newvalue, song))

#modifica un album
def alteralbum(song,newvalue):
    cur=con.cursor()
    cur.execute('update cancion set album = %s where id_cancion = %s',(newvalue , song))

#modifica una cancion
def alternameSong(song,newvalue):
    cur = con.cursor()
    cur.execute('update cancion set nombre = %s where id_cancion = %s', (newvalue , song))

#modifica un artista
def alterartist(song,newvalue):
    cur = con.cursor()
    cur.execute('update cancion set artista = %s where id_cancion= %s', (newvalue , song))

#borrar cancion
def inactiveSong(song):
    cur = con.cursor()
    cur.execute('update cancion set active = %s where id_cancion = %s', ('F', song))

#borrar album
def delalbum(album):
    cur = con.cursor()
    cur.execute('delete from Album where nombre = %s',(album))

#borrar artista
def delartist(artist):
    cur = con.cursor()
    cur.execute('delete from Artist where nombre = %s',(artist))


    #funciones de admin, muestran valores
#albumes mas recientes
def albumesRecientes():
    cur = con.cursor()
    cur.execute('SELECT album, fecha_lanzamiento FROM cancion c WHERE c.fecha_lanzamiento BETWEEN %s and %s group by album, fecha_lanzamiento order by fecha_lanzamiento desc', ('2021-03-21', '2021-03-27'))
    row = cur.fetchall()
    for r in row:
        print(f"{r[0]}, Album {r[1]}, Launched {r[2]}\n")

#artista con mayor produccion musical
def mostProd():
    cur = con.cursor()
    cur.execute('select artista , count(artista) from Cancion group by artista order by count(artista) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"Artist: {r[0]},  Songs: {r[1]}\n")

#genero mas popular
def popularGen():
    cur = con.cursor()
    cur.execute('select genero , count(genero) from Cancion group by genero order by count(genero) desc limit 1')
    row = cur.fetchall()
    for r in row:
        print(f"Genere: {r[0]}, Songs: {r[1]}\n")

#usuario mas activo
def mostActive():
    cur = con.cursor()
    cur.execute('select Usuario, count(Usuario) as busquedas from Buscador group by Usuario order by count(Usuario) desc limit 5')
    row = cur.fetchall()
    for r in row:
        print(f"Username {r[0]}, Searches {r[1]}\n")

#total de reproducciones por semana
def weekViews(inicio, final):
    cur = con.cursor()
    cur.execute('Select nombre, count(nombre) from buscador right join cancion on id_cancion = id_cancion where fecha_busqueda in between %s and %s', (inicio, final))
    row = cur.fetchall()
    for r in row:
        print(f"Song: {r[0]}, Views This week: {r[1]}\n")

#x artistas con mas reproducciones entre la fecha
def dateArtists(cant, inicio, final):
    cur = con.cursor()
    cur.execute('Select artist, count(id_cancion) from buscador right join cancion on id_cancion = id_cancion where fecha_busqueda in between %s and %s limit %s', (inicio, final, cant))
    row = cur.fetchall()
    for r in row:
        print(f"Artista: {r[0]}, Reproducciones: {r[1]}\n")

#reproducciones de genero en las fechas ingresadas
def genreViewsIn(genre, inicio, final):
    cur = con.cursor()
    cur.execute('Select genre, count(genre) from buscador right join cancion on id_cancion = id_cancion where genre = %s and fecha_busqueda in between %s and %s ', (genre, inicio, final))
    row = cur.fetchall()
    for r in row:
        print(f"Genere: {r[0]}, Views: {r[1]}\n")

#Top x canciones con mas reproducciones de artista
def topArtistSongs(cant, artist):
    cur = con.cursor()
    cur.execute('Select nombre, artista, count(nombre) from buscador right join cancion on id_cancion = id_cancion where artista = %s limit %s', (artist, cant))
    row = cur.fetchall()
    for r in row:
        print(f"Genere: {r[0]}, Views: {r[1]}\n")
