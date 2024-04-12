import requests
from pwn import *

a = 'admin=False;expi'.encode()
b = 'admin=True; expi'.encode()
print(xor(a, b))
r = requests.get('https://aes.cryptohack.org/flipping_cookie/get_cookie/').json()['cookie']
iv = r[:32]
ct = r[32:]
iv = xor(bytes.fromhex(iv), xor(a, b)).hex()
r = requests.get('https://aes.cryptohack.org/flipping_cookie/check_admin/' + ct + '/' + iv + '/').json()
print(r)
