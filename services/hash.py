import hashlib


def hash_message():
    msg = input('Please type the message to hash: ')
    algo = input('Please choose the hash function:\n\
1-Md5\n\
2-SHA1\n\
3-SHA256\n')
    if algo == '1':
        return hashlib.md5(msg.encode()).hexdigest()
    elif algo == '2':
        return hashlib.sha1(msg.encode()).hexdigest()
    else:
        return hashlib.sha256(msg.encode()).hexdigest()


def crack_hashed_email():
    hashed_email = input('Type the hash of the email:\n')
    file1 = open('randomEmails.txt', 'r')
    while True:
        line = file1.readline()
        line = line.strip()
        # print(line)

        hashed = hashlib.md5(line.encode()).hexdigest()
        if hashed == hashed_email:
            print('Sucess! the email is', line)
            return
        hashed = hashlib.sha1(line.encode()).hexdigest()
        if hashed == hashed_email:
            print('Sucess! the email is', line)
            return
        hashed = hashlib.sha256(line.encode()).hexdigest()
        if hashed == hashed_email:
            print('Sucess! the email is', line)
            return
        if not line:
            break
    print('Email not found in the current dictionary')
