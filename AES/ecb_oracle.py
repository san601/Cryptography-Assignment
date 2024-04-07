from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

FLAG = 'crypto'
plaintext = '616161616161616161'
plaintext = bytes.fromhex(plaintext)
padded = pad(plaintext + FLAG.encode(), 16)
# padded = b'aaaaaaaaacrypto\x01'
