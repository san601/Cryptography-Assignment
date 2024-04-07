from Crypto.Cipher import AES
import hashlib
import requests

ciphertext = 'c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66'
ciphertext = bytes.fromhex(str(ciphertext))
words = requests.get("https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words").text.splitlines()
for word in words:
    KEY = hashlib.md5(word.encode()).digest()
    cipher = AES.new(KEY, AES.MODE_ECB)
    try:
        plaintext = cipher.decrypt(ciphertext)
        if "crypto" in plaintext.decode():
            print(plaintext)
            break
    except:
        pass