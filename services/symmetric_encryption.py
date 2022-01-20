import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import pyDes


class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]


class DESCipher:

    k = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0",
                  pad=None, padmode=pyDes.PAD_PKCS5)

    def encrypt(self, msg):
        return self.k.encrypt(msg)

    def decrypt(self, msg):
        return self.k.decrypt(msg).decode()


def encrypt():
    msg = input('Type the message you want to encrypt: ')
    choix = input('Choose:\n\
1-AES256\n\
2-DES\n')
    if choix == '1':
        return AESCipher('key').encrypt(msg)
    else:
        return DESCipher().encrypt(msg)


def decrpyt():
    msg = input('Type the message you want to decrypt: ')
    choix = input('Choose:\n\
1-AES256\n\
2-DES\n')
    if choix == '1':
        return AESCipher('key').decrypt(msg)
    else:
        encrypted_input = msg.encode().decode(
            'unicode_escape').encode("raw_unicode_escape")

        return DESCipher().decrypt(encrypted_input)


# input('Msg à chiffrer\n')
# encrypted_text = DESCipher().encrypt()
# print(encrypted_text)
# toDecrypt = input('type the msg to decrpyt: ')

# print(DESCipher().decrypt(encrypted_input))
