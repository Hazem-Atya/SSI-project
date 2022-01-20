from Crypto.PublicKey import RSA
import ast
from Crypto.Cipher import PKCS1_OAEP
import services.elgamal as elgamal


class RSACipher:

    def exportKey(self):
        k = key.exportKey('PEM')
        p = key.publickey().exportKey('PEM')
        return (k, p)

    def saveKeysInFiles(self):
        (k, p) = self.exportKey()
        with open('services/rsa_keys/private.pem', 'w') as kf:
            kf.write(k.decode())
            kf.close()

        with open('services/rsa_keys/public.pem', 'w') as pf:
            pf.write(p.decode())
            pf.close()

    def getKeysFromFiles(self):
        privateKeyPath = 'services/rsa_keys/private.pem'
        publicKeyPath = 'services/rsa_keys/private.pem'

        with open(privateKeyPath, 'r') as fk:
            priv = fk.read()
            fk.close()
        with open(publicKeyPath, 'r') as fp:
            pub = fp.read()
            fp.close()
        privat = RSA.importKey(priv)
        public = RSA.importKey(pub)
        key = privat
        return (privat, public)

    def encrypt(self, msg):
        public_key = key.publickey()
        encryptor = PKCS1_OAEP.new(public_key)
        encrypted = encryptor.encrypt(msg.encode())
        return encrypted

    def decrypt(self, data):
        decryptor = PKCS1_OAEP.new(key)
        # print(data)
        decrypted = decryptor.decrypt(ast.literal_eval(str(data)))
        # print(decrypted)
        return decrypted.decode()


rsa = RSACipher()


def encrypt():
    msg = input('Type the message to encrypt: ')
    choix = input('choose:\n1-RSA  \n2-ELGamal\n')

    if choix == '1':
        return rsa.encrypt(msg)
    else:
        return elgamal.encrypt_msg(msg)


def decrypt():
    data = input('Type the message to encrypt: ')
    choix = '1'
    if choix == '1':
        encrypted_input = data.encode().decode(
            'unicode_escape').encode("raw_unicode_escape")
        return rsa.decrypt(encrypted_input)
    else:
        return elgamal.decrypt_msg(msg)


# print(encrypt())
# print(decrypt())
(priv,pub)=RSACipher().getKeysFromFiles()
key=priv
