import Database.DBConnection as db
import re
import hashlib
import uuid


class UserService(metaclass=db.MetaSingleton):
    i = 0

    def findUserByEmail(self, email):
        cur = db.Database().connect()
        conn = db.Database().connection
        user = cur.execute(
            "select * from users where email=(?)", (email,)).fetchone()
        conn.commit()
        return user

    def addUser(self, name, email, password):
        cur = db.Database().connect()
        conn = db.Database().connection
        # verifying if the mail is already used
        user = cur.execute(
            'select * from users where email==?', (email,)).fetchone()
        if(user):
            return False
        salt = uuid.uuid4().hex
        pwd = str.encode(password+salt)
        hashed_password = hashlib.sha512(pwd).hexdigest()
        cur.execute("insert into users (name,email,password,salt) values(?,?,?,?)",
                    (name, email, hashed_password, salt))
        conn.commit()
        return True

    def verifyCredentials(self, email, password):
        user = UserService().findUserByEmail(email)
        if user == None:
            print('Wrong email and/or password')
            return None
        else:
            salt = user[4]
            pwd = str.encode(password+salt)
            hashed_password = hashlib.sha512(pwd).hexdigest()
            user_pwd = user[3]
            if hashed_password != user_pwd:
                print('Wrong email and/or password')
                return None
            else:
                name = user[1]
                return (name, email)


#print(UserService().verifyCredentials('hazem10@gmail.com', 'hazem'))
