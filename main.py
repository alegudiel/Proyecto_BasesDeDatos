import psql as db
import getpass
import menus as m

opcion = True

#decision 1
while(opcion):
#bienvenida y menu
    print('----------Welcome to SoundCity----------')
    print('1.Create account\n2. Login')
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
            db.newSub(newuser)
            contador = 0
            m.freeMenu(newuser, contador)

    else:
        print("------Login------")
        enteruser = input('Enter your username ')
        enterpass = getpass.getpass('Enter your password ')
        if(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 1):
            print('\nPremium Login Successful')
            m.subsMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 2):
            print('\nAdmin Login Successful')
            m.adminMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 3):
            print('\nFree Login Successful')
            contador = 0
            m.freeMenu(enteruser, contador)
        else:   
            print('Login failed')