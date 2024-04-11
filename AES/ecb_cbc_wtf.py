import os
import requests
from pwn import xor

a = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/').json()['ciphertext']
iv = bytes.fromhex(a[:32])
ct1 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + a[32:32+32]).json()['plaintext']
ct2 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + a[32+32:]).json()['plaintext']

print(xor(iv, bytes.fromhex(ct1)).decode(), end='')
print(xor(bytes.fromhex(a[32:32+32]), bytes.fromhex(ct2)).decode())


