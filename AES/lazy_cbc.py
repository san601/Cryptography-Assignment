import requests
from pwn import xor
ciphertext = b'\x00' * 32
plaintext = requests.get('https://aes.cryptohack.org/lazy_cbc/receive/' + ciphertext.hex() + '/').json()['error'][-64:]
key = xor(bytes.fromhex(plaintext[:32]), bytes.fromhex(plaintext[32:]))

flag = requests.get('https://aes.cryptohack.org//lazy_cbc/get_flag/' + key.hex() + '/').json()['plaintext']
print(bytes.fromhex(flag))
