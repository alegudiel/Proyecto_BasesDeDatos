import psql as db
import getpass
import menus as m

opcion = True

#decision 1
while(opcion):
#bienvenida y menu
    print('----------Welcome to SoundCity----------')
    print('1.Create account\n2. Login\n')
    menu = input()

    if (menu == '1'):
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
            print('Premium Login Successful\n')
            m.subsMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 2):
            print('Admin Login Successful\n')
            m.adminMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 3):
            print('A Monitor Login Successful\n')
            m.adminMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 4):
            print('B Monitor Login Successful\n')
            m.adminMenu(enteruser)
        elif(db.checkUser(enteruser, enterpass) == True and db.checkSub(enteruser) == 5):
            print('Free Login Successful\n')
            contador = 0
            m.freeMenu(enteruser, contador)
        else:   
            print('Login failed\n')