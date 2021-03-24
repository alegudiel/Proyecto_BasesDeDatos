import psql as db

db.checkSub('admin')

#menu reproduccion para usuarios gratis
def freeMenu(user, contador):
    while contador < 4:
        print("What do you want to do? ")
        print("1. Listen to music \n2. Subscribe\n3. Exit")
        menu2 = int(input())
        if (menu2 == 1 and contador != 3):    
            #muestra el catalogo    
            db.catalogo()   
            #pregunta por la cancion   
            cancion = input('Enter the song number: ')
            db.searchSong(cancion)
            contador +=1
            cuenta = db.countSearch() + 1
            db.newSearch(cuenta, user, cancion)
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

#menu reproduccion usuarios suscritos
def subsMenu(user):
    while True:
        print("Current Subscription: Premium")
        print("What do you want to do? ")
        print("1. Listen to music \n2. Playlists \n3.Exit")
        menu2 = int(input())
        if (menu2 == 1):    
            #muestra el catalogo    
            db.catalogo()   
            #pregunta por la cancion   
            cancion = input('Enter the song number: ')
            db.searchSong(cancion)
            #asigna un id automatico para mejor orden en la base
            cuenta = db.countSearch() + 1
            #crea un nuevo registro de busqueda para encontrar a los usuarios mas activos
            db.newSearch(cuenta, user, cancion)
            break
        if(menu2 == 2):
            while True:
                de = int(input('\n1. Create Playlist \n2. Add Song to Playlist \n3. Show Playlists\n4. Exit\n'))
                if de == 1:
                    id = db.countpl() + 1
                    name = input('Playlist name ')
                    db.newPL(id, name, user)
                elif de == 2:
                    db.catalogo()
                    id = db.countpls() + 1
                    play_id = input('\nPlaylist id ')
                    song_id = int(input('\nSong to your playlist '))
                    db.addToPL(id, play_id, song_id)
                elif de == 3:
                    print('\nThese are your playlists: ', user)
                    if db.getPlaylists(user):
                        cancion = input('Enter the song number: ')
                        db.searchSong(cancion)
                        cuenta = db.countSearch() + 1
                        db.newSearch(cuenta, user, cancion)
                    else:
                        new = input('You do not have playlists, do you want to create a new one? Y/n')
                        if new == 'y' or 'Y':
                            id = db.countpl() + 1
                        name = input('Playlist name ')
                        db.newPL(id, name, user)
                else:
                    break
        else:
            break

#menu para suscribirse
def subMenu():
    while True:
        print("Current Subscription: free")
        pregunta = input("Do you want to sub?\n1. Yes\n2. No\n")
        if pregunta == '1':
            username = input("enter your username: ")
            db.alterSub(username, 'premium')
            print('Welcome to SounCity Premium. You can now listen to unlimited songs')
            break
        if pregunta == '2':
            print('Come back tomorrow for another 3 songs ')
            break

#menu de admin
def adminMenu(user):
    while True:
        print("What do you want to do? ")
        print("1. Listen to music \n2. Management Tools\n3. Exit")
        menu2 = int(input())
        if (menu2 == 1):    
            #muestra el catalogo    
            db.catalogo()   
            #pregunta por la cancion   
            cancion = input('Enter the song number: ')
            db.searchSong(cancion)
            cuenta = db.countSearch() + 1
            db.newSearch(cuenta, user, cancion)
        if(menu2 == 2):
            preguntaadmin = input('1.Inactivate a Song \n2.Modify a Song \n3.Modify an album \n4.Modify an artist \n5.Delete an album \n6.Delete an artist \n7.Reportes ')
            if preguntaadmin=='1':
                #muestra el catalogo    
                db.catalogo()
                #pregunta por la cancion   
                cancionborrar = input('Enter the song number you want to delete: ')
                db.delsong(cancionborrar)
            if preguntaadmin=='2':
                #muestra el catalogo    
                db.catalogo()
                #pregunta por la cancion   
                cancionmodificar = input('Enter the song name you want to modify: ')
                cancioncambio = input('Enter the new value of the song : ')
                db.alternameSong(cancionmodificar,cancioncambio)
            if preguntaadmin=='3':
                #muestra el catalogo de albums
                db.catalogoalbumes()
                #pregunta por el album a modificar
                albummodificar = input('Enter the album name you want to modify: ')
                albumcambio = input('Enter the new value of the album : ')
                db.alteralbum(albummodificar,albumcambio)
            if preguntaadmin == '4':
                #muestra el catalogo de artistas
                db.catalogoartistas()
                #pregunta por el artista a modificar
                artistamodificar= input('Enter the artist name you want to modify: ')
                artistacambio = input('Enter the new value of the artist: ')
                db.alterartist(artistamodificar,artistacambio)
            if preguntaadmin == '5':
                #muestra el catalogo de albumes
                db.catalogoalbumes()
                #pregunta por el album a borrar
                albumborrar = input('Enter the album name you want to delete: ')
                db.delalbum(albumborrar)
            if preguntaadmin == '6':
                #muestra el catalogo de artistas
                db.catalogoartistas90
                #pregunta por el artista a borrar
                artistaborrar = input ('Enter the artist name you want to delete: ')
                db.delartist(artistaborrar)
            if preguntaadmin == '7':
                eleccionreporte = input('\n1.Albumes mas recientes \n2.Artistas con popularidad creciente en los últimostres meses \n3.Cantidad de nuevas suscripciones mensuales durantelos últimos seis meses \n4.Artistas con mayor producción musical \n5.Géneros más populares \n6.Usuarios más activos en la plataforma ')
                if eleccionreporte == '1':
                    db.albumesRecientes()           
                if eleccionreporte == '4':
                    db.mostProd()
                if eleccionreporte == '5':
                    db.popularGen()
                if eleccionreporte == '6':               
                    db.mostActive()
