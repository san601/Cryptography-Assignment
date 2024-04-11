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


shared_secret = 0x5f14002bab6279da79b36f8be2224660a1b670c0be968cffc46b6a0150f93a5995c4fd57870c72ddff8c9e6269aee7289d196aa5a4526810b7fc54268e681882331005a081ea2bd3aa5c0de57ab7f15d03f2c7c5fde32124b483491cec288cb20e8b55eacbb68b8e9f603a33cd0033e17eccd9b43b45cdc868eaf2da1914521d19384502ea2af3dd8632ce1ad378c9cd55aa2fcc97b94c8b6e666d55e94fb0f735b9aa92eee73f2d583567a58661c0a9a1f5682bd318105a2ec1c1d0a1020439
iv = "86d52306429a8d8b2e49dd699fdf8fa8"
ciphertext = "ff1d055171f7c0eb76fd6803f231787b5015e8da36d4cb28c6f3c08fc19bd1f1"


print(decrypt_flag(shared_secret, iv, ciphertext))
