import services.UserService as UserService
import hashlib
import getpass
import authentification.OPT_sender as opt


def login():
    user = None
    email = input('Please type your email\n')
    password = getpass.getpass(
        prompt='Please type your password:', stream=None)
    user = UserService.UserService().verifyCredentials(email, password)
    if user:
        optCode = opt.sendVerificationCode(user[1], user[0])
        while True:
            enteredCode = input(
                f'Hello {user[0]} Please type the OTP code sent to your email: ')
            if optCode == enteredCode:
                print('Your opt code is correct!')
                return user
            print('Wrong code')
            choice = input("""Choose
1- Try again
2- Resend the code
3- Return to the main menu
4- Quit\n""")
            if choice == '1':
                continue
            elif choice == '2':
                optCode = opt.sendVerificationCode(user[1], user[0])
            elif choice == '3':
                return
            else:
                exit()

    else:
        print("Please type:")
        print("1- Retry")
        print("2- Return to the main menu")
        print("3- Quit")
        choice = input()
        if choice == "1":
            login()
        elif choice == "2":
            return False
        else:
            exit()


# print(login())
