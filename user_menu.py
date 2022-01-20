# this file contains the menu that will appear to the loggeed in user

import base64
import services.Code_Decode as code_decode
import services.hash as hash_module
import services.symmetric_encryption as symmetric_encryption
import services.assym_encryption as asym_enc
import chatroom.client as client

username=''
def user_menu():
    while(True):
        print("Please choose")
        print("1- Code or decode a message")
        print("2- Hash a message")
        print("3- Symmetric encryption and decryption")
        print("4- Asymmetric encryption and decryption")
        print("5- Chatroom ")
        print('6- Logout')
        choice = input()
        if choice == "1":
            c = input("choose:\n\
a- Code a message\n\
b- Decode a messaged\n")
            if c == 'a':
                print('Your coded message is:', code_decode.encode())
            elif c == 'b':
                print('Your decoded message is:', code_decode.decode())
        elif choice == '2':
            c = input('choose:\n\
a-hash a message\n\
b-crack a hashed email\n')
            if c == 'a':
                print('Your hash is: ', hash_module.hash_message())
            else:
                hash_module.crack_hashed_email()
        elif choice == '3':
            c = input("choose:\n\
a- Encrypt a message\n\
b- Decpryt a messaged\n")
            if c == 'a':
                print('Your encrypted message is: ',
                      symmetric_encryption.encrypt())
            else:
                print('Your message is: ', symmetric_encryption.decrpyt())
        elif choice == '4':
            c = input("choose:\n\
a- Encrypt a message\n\
b- Decpryt a messaged\n")
            if c == 'a':
                print('Your encrypted msg: ', asym_enc.encrypt())
            elif c == 'b':
                print('Your plain msg: ', asym_enc.decrypt())

        elif choice=='5':
             client.my_username=username
             client.joinChatroom()
        elif choice == '6':
            return

user_menu()
# e8af37e8c2ce8727656669d6927c51f1