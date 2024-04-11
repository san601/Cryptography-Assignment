import os
import requests
from pwn import xor

response = requests.get('https://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/').json()['ciphertext']
iv = response[:32]
ct1 = response[32:32+32]
ct2 = response[32+32:]
pt1 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + ct1).json()['plaintext']
pt2 = requests.get('https://aes.cryptohack.org/ecbcbcwtf/decrypt/' + ct2).json()['plaintext']

print(xor(bytes.fromhex(iv), bytes.fromhex(pt1)).decode(), end='')
print(xor(bytes.fromhex(ct1), bytes.fromhex(pt2)).decode())
