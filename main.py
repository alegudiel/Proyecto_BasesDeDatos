import psql as db
import getpass

#menu reproduccion
def newMenu():
    print("What do you want to do? ")
    print("1. Listen to music \n 2. Suscribe")
    menu2 = int(input())
    if (menu2 == 1):    
        #muestra el catalogo    
        db.catalogo()   
        #pregunta por la cancion   
        cancion = input('Enter the song number: ')
        db.searchSong(cancion)

#bienvenida y menu
print('----------Welcome to SoundCity----------')
print('1.Create account\n2. Login')
opcion = True

#decision 1
while(opcion):
    menu = int(input())
    if menu == 1:
        try:
            int(menu)

        except:
            print('Enter a number')

    if (menu == 1):
        print('------Sign Up------')
        newuser = input('Enter your username ')
        newpass = getpass.getpass('Enter your password ')
        newmail = input('Enter your mail ')
        if (db.addUser(newuser, newpass, newmail) == True):
            while True:
                newMenu()

    else:
        print("------Login------")
        enteruser = input('Enter your username ')
        enterpass = getpass.getpass('Enter your password ')
        if db.checkUser(enteruser, enterpass) == True:
            print('Login Successful')
            newMenu()

        else:
            print('Login failed')


