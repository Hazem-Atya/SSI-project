import base64


def encode():
    msg = input('Type the msg to encode: ')
    base = input('Choose the base:\n\
1-Base 16\n\
2-Base 32\n\
3-Base 64\n')
    if base == '1':
        return base64.b16encode(msg.encode()).decode()
    elif base == '2':
        return base64.b32encode(msg.encode()).decode()
    else:
        return base64.b64encode(msg.encode()).decode()

def decode():
    msg = input('Type the msg to decode: ')
    base = input('Choose the base:\n\
1-Base 16\n\
2-Base 32\n\
3-Base 64\n')
    if base == '1':
        return base64.b16decode(msg.encode()).decode()
    elif base == '2':
        return base64.b32decode(msg.encode()).decode()
    else:
        return base64.b64decode(msg.encode()).decode()
# print(encode())
# print(decode())