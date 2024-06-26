from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests

def response(plaintext):
    url = "http://aes.cryptohack.org/ecb_oracle/encrypt/"
    req = requests.get(url + plaintext.hex() + '/')
    return req.json()['ciphertext']


char = ''
for i in range(33, 126):
    char += chr(i)
flag = ''
flag_len = 25

for i in range(25):
    byte_string = (b'a' * (31 - i))
    res1 = response(byte_string)
    for j in char:
        res2 = response(byte_string + flag.encode() + j.encode())
        if bytes.fromhex(res1[:64]) == bytes.fromhex(res2[:64]):
            print(j, end='')
            flag += j
            break
