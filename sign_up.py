import getpass
import re
import services.UserService as UserService

def addUser():
    test=False
    while not test:
        name = input("Please type your name\n")
        email = input('Please type your email\n')
        while(not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)):
            email = input('Please type a valid email\n')
        password='0'
        verifPassword='1'
        wrong=False
        while verifPassword != password:
            if wrong:
                print('Passwords are not identical! Please try again')
            password = getpass.getpass(prompt='Please type a password:', stream=None)
            while len(password) < 5:
                password = getpass.getpass(prompt='Please type a password with 5 characters at least\n', stream=None)
        
            verifPassword=getpass.getpass(prompt='Please verify your password')
            if verifPassword!=password:
                wrong = True
        test= UserService.UserService().addUser(name, email, password)
        if not test:
            print("This email is already used")
            print("Please type:")
            print("1- Retry")
            print("2- Return to the main menu")
            print("3- Quit") 
            choice = input()
            if choice== "2":
                return False
            elif choice=="3":
                exit()
    return True
