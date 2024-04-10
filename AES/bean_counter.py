import requests

ciphertext = requests.get('https://aes.cryptohack.org/bean_counter/encrypt/').json()['encrypted']

firstByte = [
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, 0x00, 0x00, 0x00, 0x0D,
    0x49, 0x48, 0x44, 0x52
]

block = [a ^ b for a, b in zip(firstByte, bytes.fromhex(ciphertext[:len(firstByte)*2]))]

block = block * (len(ciphertext) // len(block))
flag = [a ^ b for a, b in zip(block, bytes.fromhex(ciphertext))]

with open('image.png', 'wb') as file:
    file.write(bytes(flag))

