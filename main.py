import psql as db
import getpass

#bienvenida y menu
print('----------Welcome to SoundCity----------')
print('1.Create account\n2. Login')
#decision 1
while(True):
    d1 = input()
    try:
        int(d1)
        break
    except:
        print('Enter a number')

if (d1 == 1):
    print('------Sign Up------')
    newuser = input('Enter your username ')
    newpass = getpass.getpass('Enter your password ')

if(d1 == 2):
    print("------Login------")
    enteruser = input('Enter your username ')
    enterpass = getpass.getpass('Enter your password ')

