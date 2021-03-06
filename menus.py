import psql as db
import datetime
import mongo as mdb

# try catch para fechas e ints de los menus

# menu reproduccion para usuarios gratis
def freeMenu(user, contador):
    while contador < 4:
        print("What do you want to do? ")
        print("1. Listen to music \n2. Subscribe\n3. Exit")
        menu2 = int(input())
        if (menu2 == 1 and contador != 3):
            # muestra el catalogo
            db.catalogo()
            # pregunta por la cancion
            cancion = input('Enter the song number: \n')
            if(db.searchSong(cancion)):
                # asigna un id automatico para mejor orden en la base
                cuenta = db.countSearch() + 1
                # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                db.newSearch(cuenta, user, cancion)
            elif(db.searchSong(cancion) == False):
                print("Sorry, this song is not available in this moment. \n")
        elif(menu2 == 1 and contador == 3):
            print('Please upgrade your subscription: \n')
            subMenu()
            subsMenu(user)
            break
        elif(menu2 == 2):
            subMenu()
            subsMenu(user)
            break
        else:
            break

# menu reproduccion usuarios suscritos


def subsMenu(user):
    while True:
        print("\nCurrent Subscription: Premium\n")
        print("What do you want to do? ")
        print("1. Listen to music \n2. Playlists \n3. Top 10 new Songs \n4. Exit")
        menu2 = int(input())
        if (menu2 == 1):
            # muestra el catalogo
            db.catalogo()
            # pregunta por la cancion
            cancion = input('Enter the song number: \n')
            if(db.searchSong(cancion)):
                # asigna un id automatico para mejor orden en la base
                cuenta = db.countSearch() + 1
                # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                db.newSearch(cuenta, user, cancion)
            elif(db.searchSong(cancion) == False):
                print("Sorry, this song is not available in this moment. \n")
        if(menu2 == 2):
            while True:
                de = int(input(
                    '\n1. Create Playlist \n2. Add Song to Playlist \n3. Show Playlists\n4. Exit\n'))
                if de == 1:
                    pid = db.countpl() + 1
                    name = input('Playlist name \n')
                    db.newPL(pid, name, user)
                elif de == 2:
                    db.catalogo()
                    id = db.countpls() + 1
                    play_id = input('\nPlaylist id ')
                    song_id = int(input('\nSong to your playlist \n'))
                    db.addToPL(id, play_id, song_id)
                elif de == 3:
                    print('\nThese are your playlists ', user)
                    if (db.getPlaylists(user)):
                        cancion = input('Enter the song number: \n')
                        if(db.searchSong(cancion)):
                            # asigna un id automatico para mejor orden en la base
                            cuenta = db.countSearch() + 1
                            # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                            db.newSearch(cuenta, user, cancion)
                        elif(db.searchSong(cancion) == False):
                            print(
                                "Sorry, this song is not available in this moment. \n")
                    else:
                        new = input(
                            'You do not have playlists, do you want to create a new one? Y/n \n')
                        if new == 'y' or 'Y':
                            id = db.countpl() + 1
                            name = input('Playlist name \n')
                            db.newPL(id, name, user)
                        else:
                            break
                else:
                    break
        if(menu2 == 3):
            print("Top 10 recently added songs! ")
            break
        if(menu2 == 4):
            break

# menu para suscribirse


def subMenu():
    while True:
        print("\nCurrent Subscription: free\n")
        pregunta = input("Do you want to sub?\n1. Yes\n2. No\n")
        if pregunta == '1':
            username = input("enter your username: \n")
            db.alterSub(username, 'premium', 6)
            print('Welcome to SounCity Premium. You can now listen to unlimited songs\n')
            break
        if pregunta == '2':
            print('Come back tomorrow for another 3 songs \n')
            break

# menu de admin


def adminMenu(user, userID):
    while True:
        print("What do you want to do? ")
        print("1. Listen to music \n2. Management Tools\n3. Automatic listenings\n4. Add New Random songs \n5. Save users' listenings\n6. Recommend Songs to less active users \n7. Exit\n")
        menu2 = int(input())
        if (menu2 == 1):
            # muestra el catalogo
            db.catalogo()
            # pregunta por la cancion
            cancion = input('Enter the song number: ')
            if(db.searchSong(cancion)):
                # asigna un id automatico para mejor orden en la base
                cuenta = db.countSearch() + 1
                # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                db.newSearch(cuenta, user, cancion)
            elif(db.searchSong(cancion) == False):
                print("Sorry, this song is not available in this moment. \n")
        elif(menu2 == 2):
            print("--------Manager Tools--------")
            preguntaadmin = input(
                '\n1.Inactivate a Song \n2.Modify a Song \n3.Modify an album \n4.Modify an artist \n5.Delete an album \n6.Delete an artist \n7.Modify User type \n8.Reportes \n9.Change Log \n10.Exit\n')
            if preguntaadmin == '1':
                # muestra el catalogo
                db.catalogo()
                # pregunta por la cancion
                cancionborrar = input(
                    'Enter the song number you want to Inactivate: \n')
                db.inactiveSong(cancionborrar, userID)
            if preguntaadmin == '2':
                # muestra el catalogo
                # pregunta por la cancion
                db.catalogo()
                cancionmodificar = input(
                    'Enter the song id you want to modify: \n')
                cancioncambio = input('Enter the new value of the song : \n')
                db.alternameSong(cancionmodificar, cancioncambio, userID)
            if preguntaadmin == '3':
                # muestra el catalogo de albums
                db.catalogoalbumes()
                # pregunta por el album a modificar
                albummodificar = input(
                    'Enter the album name you want to modify: \n')
                albumcambio = input('Enter the new value of the album : \n')
                db.alteralbum(albummodificar, albumcambio, userID)
            if preguntaadmin == '4':
                # muestra el catalogo de artistas
                db.catalogoartistas()
                # pregunta por el artista a modificar
                artistamodificar = input(
                    'Enter the artist name you want to modify: \n')
                artistacambio = input('Enter the new value of the artist: \n')
                db.alterartist(artistamodificar, artistacambio, userID)
            if preguntaadmin == '5':
                # muestra el catalogo de albumes
                db.catalogoalbumes()
                # pregunta por el album a borrar
                albumborrar = input(
                    'Enter the album name you want to delete: \n')
                db.delalbum(albumborrar, userID)
            if preguntaadmin == '6':
                # muestra el catalogo de artistas
                db.catalogoartistas()
                # pregunta por el artista a borrar
                artistaborrar = input(
                    'Enter the artist name you want to delete: \n')
                db.delartist(artistaborrar, userID)
            if preguntaadmin == '7':
                print("Current users in the platform are: ")
                db.usuarios()
                userCambio = input(
                    'Enter the username you want to set user type to: ')
                print("\nUser Types:\n1. Free: limited songs per day \n2. Premium Playlists and unlimited songs\n3. Admin: Controls everything\n4. A: Monitor \n5. B: Monitor")
                typeCambio = input(
                    'Enter the number of the user type you want to set the user to: ')
                db.modUserType(userCambio, typeCambio, userID)
            if preguntaadmin == '8':
                eleccionreporte = input('\n1.Albumes mas recientes \n2.Artistas con mayor producci??n musical \n3.G??neros m??s populares \n4.Usuarios m??s activos en la plataforma \n5. Total de reproducciones por semana \n6. Los x Artistas con mas reproducciones entre fechas \n7. Total de reproducciones por genero en las fechas \n8. Top x canciones con mas reproducciones de artista \n')
                if eleccionreporte == '1':
                    db.albumesRecientes()
                if eleccionreporte == '2':
                    db.mostProd()
                if eleccionreporte == '3':
                    db.popularGen()
                if eleccionreporte == '4':
                    db.mostActive()
                if eleccionreporte == '5':
                    db.catalogo()
                    song = input("Enter the song: ")
                    inicio = input("Enter initial date in YY-MM-DD: ")
                    array = inicio.split('-')
                    fInicio = datetime.date(
                        int(array[0]), int(array[1]), int(array[2]))
                    final = fInicio + datetime.timedelta(days=7)
                    db.weekViews(fInicio, final, song)
                if eleccionreporte == '6':
                    cant = int(input("Enter the amount of artists: "))
                    inicio = input("Enter initial date in YY-MM-DD: ")
                    final = input("Enter final date in YY-MM-DD: ")
                    db.dateArtists(cant, inicio, final)
                if eleccionreporte == '7':
                    genre = input("Enter the genre: ")
                    inicio = input("Enter initial date in YY-MM-DD: ")
                    final = input("Enter final date in YY-MM-DD: ")
                    db.genreViewsIn(genre, inicio, final)
                if eleccionreporte == '8':
                    cant = input("Enter the amount of songs: ")
                    artist = input("Enter the artist: ")
                    db.topArtistSongs(cant, artist)
            if preguntaadmin == '9':
                db.bitacora()
        elif(menu2 == 3):
            print(
                "Welcome, in this section you will generate some automatic listenings\n")
            cantRepros = int(
                input("Enter the ammount of listenings to generate "))
            while True:
                datepreg = input(
                    "Do you want to generate listengings on today's date? Y/N ").lower()
                if(datepreg == 'y'):
                    rn = datetime.datetime.now().strftime('%Y-%m-%d')
                    print("Generating listenings, please wait...")
                    db.genListenings(cantRepros, rn)
                    print("Listenings generated! \n")
                    break
                elif(datepreg == 'n'):
                    listDate = input("Please enter the date as YYYY-MM-DD ")
                    print("Generating listenings, please wait...")
                    db.genListenings(cantRepros, listDate)
                    print("Listenings generated! \n")
                    break
                else:
                    print("Enter a valid option \n")
        elif(menu2 == 4):
            print("Add new random songs to the platform. ")
            qtySongs = int(input("Please enter the quantity of new songs you want to generate. "))
            print("Generating songs, please wait...")
            counter = 0
            notactives = db.notActive()
            while counter < qtySongs:
                db.genSongs(userID, notactives)
                counter += 1
                print(counter, '/',qtySongs, " song generated")
            print('\n', qtySongs, ' new songs are now active on the platform! \n')
        elif(menu2 == 5):
            print("Save user's listenings")
            while True:
                menu7 = input("Would you like to save all users' listenings? Y/N ").lower()
                if(menu7 == 'y'):
                    while True:
                        fechpreg = input("\nGenerate views up to this date? Y/N ").lower()
                        if(fechpreg == 'y'):
                            listDate = datetime.datetime.now().strftime('%Y-%m-%d')
                            print("Processing, please wait...\n")
                            allUsers = db.getUsers()
                            for u in allUsers:
                                userRolas = db.userListenings(u, listDate)
                                mdb.genUserListenings(u, userRolas, listDate)
                            print("All users' listenings saved! \n")
                            break
                        elif(fechpreg == 'n'):
                            listDate = input("Please enter the date as YYYY-MM-DD ")
                            for u in allUsers:
                                userRolas = db.userListenings(u, listDate)
                                mdb.genUserListenings(u, userRolas, listDate)
                            print("All users' listenings saved! \n")
                            break
                        else:
                            print("Enter a valid option \n")
                        break
                elif(menu7 == 'n'):
                    print(db.getUsers())
                    listUser = input("Enter the username. ")
                    while True:
                        fechpreg = input("\nGenerate views up to this date? Y/N ").lower()
                        if(fechpreg == 'y'):
                            listDate = datetime.datetime.now().strftime('%Y-%m-%d')
                            print("Fetching data, please wait...\n")
                            userRolas = db.userListenings(listUser, listDate)
                            mdb.genUserListenings(listUser, userRolas, listDate)
                            print(listUser,"`s listenings saved!\n")
                            break
                        elif(fechpreg == 'n'):
                            listDate = input("Please enter the date as YYYY-MM-DD ")
                            print("Fetching data, please wait...\n")
                            userRolas = db.userListenings(listUser, listDate)
                            print('Done! \n')
                            print("Sending data, please wait...\n")
                            mdb.genUserListenings(listUser, userRolas, listDate)
                            print(listUser,"`s listenings saved!\n")
                            break
                        else:
                            print("Enter a valid option \n")
                        break
                else:
                    print("Enter a valid option \n")
                break
        elif(menu2 == 6):
            print("\nRecommend Songs to less active users")
            print("\nThe 10 less active users are: ")
            db.usersRecommends()
            print("\nWe recommend These songs to them: ")
            db.recommends()
            print('\n')
        if(menu2==7):
            break

def monitorMenu(user, type, userID):
    # monitor A
    if type == 3:
        print('\nMonitor A Login Successful!\n')
        while True:
            print("What do you want to do? ")
            print("1. Listen to music \n2. Monitoring Tools\n3. Exit")
            menu2 = int(input())
            if (menu2 == 1):
                # muestra el catalogo
                db.catalogo()
                # pregunta por la cancion
                cancion = input('Enter the song number: \n')
                if(db.searchSong(cancion)):
                    # asigna un id automatico para mejor orden en la base
                    cuenta = db.countSearch() + 1
                    # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                    db.newSearch(cuenta, user, cancion)
                elif(db.searchSong(cancion) == False):
                    print("Sorry, this song is not available in this moment. \n")
            if(menu2 ==2):
                print('\n--------Monitoring Tools--------')
                monA = input('\n1. Inactivate a Song \n2. Modify a Song \n3. Modify an album \n4. Unsubscribe user \n5. Exit\n')
                if monA == '1':
                    # muestra el catalogo
                    db.catalogo()
                    # pregunta por la cancion
                    cancionborrar = input('Enter the song number you want to Inactivate: \n')
                    db.inactiveSong(cancionborrar, userID)
                elif monA == '2':
                    # muestra el catalogo
                    # pregunta por la cancion
                    cancionmodificar = input( 'Enter the song name you want to modify: \n')
                    cancioncambio = input('Enter the new value of the song : \n')
                    db.alternameSong(cancionmodificar, cancioncambio, userID)
                elif monA == '3':
                    # muestra el catalogo de albums
                    db.catalogoalbumes()
                    # pregunta por el album a modificar
                    albummodificar = input('Enter the album name you want to modify: \n')
                    albumcambio = input('Enter the new value of the album : \n')
                    db.alteralbum(albummodificar, albumcambio, userID)
                elif monA == '4':
                    userCambio = input('Enter the username you want to unsubscribe: ')
                    db.modUserType(userCambio, '1', userID)
                elif(monA == '5'):
                    break
            elif(menu2 ==3):
                break
    # monitor B
    elif type == 4:
        print('\nMonitor B Login Successful!\n')
        while True:
            print("What do you want to do? ")
            print("1. Listen to music \n2. Monitoring Tools\n3. Exit")
            menu2 = int(input())
            if (menu2 == 1):
                # muestra el catalogo
                db.catalogo()
                # pregunta por la cancion
                cancion = input('Enter the song number: \n')
                if(db.searchSong(cancion)):
                    # asigna un id automatico para mejor orden en la base
                    cuenta = db.countSearch() + 1
                    # crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
                    db.newSearch(cuenta, user, cancion)
                elif(db.searchSong(cancion) == False):
                    print("Sorry, this song is not available in this moment. \n")
            if(menu2 ==2):
                print('\n--------Monitoring Tools -------')
                monB = input('\n1. Add new Monitor \n2. Calculate Artist revenue \n3. Change Log \n4.Exit\n')
                if (monB == '1'):
                    print('Users available: \n')
                    db.usuarios()
                    userCambio = input('Enter the username you want to make Monitor: ')
                    monType = input('Enter the monitor type (A/B): ')
                    if (monType == 'A' or 'a'):
                        db.modUserType(userCambio, '4', userID)                    
                    if (monType == 'B' or 'b'):
                        db.modUserType(userCambio, '5', userID)                    
                elif (monB == '2'):
                    print('---Search an artist to calculate the revenue he makes in ONE month---')
                    print('Enter the date in the following format: YY-MM-DD\n')
                    art = input('Artist: ')
                    ini = input('Initial Date: ')
                    fin = input('Final Date: ')
                    db.comisiones(art, ini, fin)
                elif (monB == '3'):
                    db.bitacora()
                elif (monB == '4'):
                    break
            if(menu2 ==3):
                break
