from Crypto.Util.number import *
from sympy.ntheory import discrete_log
p = "de26ab651b92a129"
g = 2
A = "a5294eb393d3300d"
B = "7707727d4b999bb"
a = discrete_log(int(p,16), int(A,16),2 )
shared = pow(int(B,16),a,int(p,16))

from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
import hashlib


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


p = "de26ab651b92a129"
g = 2
A = "a5294eb393d3300d"
B = "7707727d4b999bb"
a = discrete_log(int(p,16), int(A,16),2 )
shared = pow(int(B,16),a,int(p,16))

shared_secret = shared
iv = "bd24b1f4c014eda1afde1a7c1085ce70"
ciphertext = "3150da3646b1edc8fbb02702187f80c0062fe328b31ede055f93b388d7559a9e"


print(decrypt_flag(shared_secret, iv, ciphertext))
