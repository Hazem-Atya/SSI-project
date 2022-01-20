import re
import sign_up as register
import authentification.auth as auth
import user_menu
def emailVerification(email):
    match=re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match==None:
        return False
    return True

#email=input('Please type your email to log in \n')

while(True):
    print("Please choose")
    print("1- Sign-up")
    print("2- Log in")
    print("3- Quit")
    choice= input()
    if choice== "1":
        loggedIn=register.addUser()
        if (loggedIn):
            print("Account created successfully!")
    elif choice=="2":
        user=auth.login()
        if(user):
            print('Welcome ',user[0])
            user_menu.username=user[0]
            user_menu.user_menu()
    elif choice=="3":
        exit()

# e8af37e8c2ce8727656669d6927c51f1