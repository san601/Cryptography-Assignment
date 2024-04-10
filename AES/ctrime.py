import requests
import string


def encrypt(plaintext):
    plaintext = plaintext.encode().hex()
    s = 'http://aes.cryptohack.org/ctrime/encrypt/' + plaintext + '/'
    ciphertext = requests.get(s).json()['ciphertext']
    return ciphertext


alphabet = '!' + '}' + '_' + '@' + '?' + string.ascii_uppercase + string.digits + string.ascii_lowercase

# plaintext = 'crypto{'
plaintext = 'crypto{CRIME'
current_length = len(encrypt(plaintext))

while True:
    flag = False
    for char in alphabet:
        ciphertext = encrypt(plaintext + char)
        print(f"Trying {plaintext + char} with length {len(ciphertext)}")
        if len(ciphertext) < current_length:
            current_length = len(ciphertext)
            print(f"Found character: {char}")
            plaintext += char
            flag = True
            break
        current_length = len(ciphertext)
    if not flag or '}' in plaintext:
        print(plaintext)
        break
