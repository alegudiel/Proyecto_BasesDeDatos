import psql as db
import getpass
import menus as m

opcion = True

#decision 1
while(opcion):
#bienvenida y menu
    print('----------Welcome to SoundCity----------')
    print('1. Create account\n2. Login\n3. Exit')
    menu = input()

    if (menu == '1'):
        print('------Sign Up------')
        newuser = input('Enter your username ')
        newpass = getpass.getpass('Enter your password ')
        newmail = input('Enter your mail ')
        if (db.addUser(newuser, newpass, newmail) == True):
            db.newSub(newuser)
            contador = 0
            userId = db.getUserId(newuser)
            m.freeMenu(newuser, contador)

    if (menu == '2'):
        print("\n------Login------")
        enteruser = input('Enter your username ')
        enterpass = getpass.getpass('Enter your password ')
        #primero chquea que el usuario este en la base de datos
        if(db.checkUser(enteruser, enterpass)):
            #si esta en la base de datos, vemos el tipo de usuario que es
            #la funcion checkSub devuelve un int para saber el tipo de usuario
            userType = db.checkSub(enteruser)
            userId = db.getUserId(enteruser)
            if(userType == 1):
                print('\nPremium Login Successful!')
                m.subsMenu(enteruser)
            elif(db.checkSub(enteruser) == 2):
                print('\nAdmin Login Successful!')
                m.adminMenu(enteruser, userId)
            # ----menus para monitores---
            elif(db.checkSub(enteruser) == 3 or 4):
                m.monitorMenu(enteruser, userType, userId)
            elif(userType == 5):
                print('\nFree Login Successful')
                contador = 0
                m.freeMenu(enteruser, contador, userId)
            else:   
                print('\nLogin failed\n')
    else:
        break