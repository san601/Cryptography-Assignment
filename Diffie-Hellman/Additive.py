from Crypto.Util.number import *
p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 0x02
A = 0x387367618042a11df5caa640a340c66c9cdb100eeb1a64dca7e7c5dabfcea9eb5f08a62868ab6a822f1c7576b4419964128fe3676da5f4edb9f8f4aba7f4e6c7578596125875bfc14897ef3cd273c73f93d9beaf9c429989669a89976214ccb91aecff97548931f88e62d48d5f847da24b6e525e58b99f70adafc58e31fc46171e083dfe25c45f653f2ca28bb5a49eb3f3439b5a2003bf695001168a38e761e16e8da9c849aecedb48c69e947eec6eeb98557c8b908a90663a7c8afeede26068
B = 0x57334bfaf2695b08518032495fb39b1bc05f8e5a3821aefbbf97445af8c10cf29328e01c41b58b71eaa1b59124c455e565b6f491075ec95265a85902d4f76ac1c024161358aebc708b6a07ec5603d31119705de508e2282df79f45b393f2a7c7a33f3338b8889204f6b960c11c6a628b2404a760a61949d15620c884dd7807decd7cb12a074144da97eb9a5880d42d18bae71e98f8ef9b3ecf71fbb26105c29873eb69ad1443983a1a6f813dbef83f4f082477ff3686d1259c98865d8908aa20
iv= "c44c21e7df32a5b70c31457b092c274c"
encrypted = "1172654d6da540164f2ffa7b420935fcd781a7af2ca34bc4dcfd041679dddf0b2dd36ed7765e41ddb514ffbc266e4e2d"

a = A*inverse(g,p)
shared = B*a%p

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

p = 0xffffffffffffffffc90fdaa22168c234c4c6628b80dc1cd129024e088a67cc74020bbea63b139b22514a08798e3404ddef9519b3cd3a431b302b0a6df25f14374fe1356d6d51c245e485b576625e7ec6f44c42e9a637ed6b0bff5cb6f406b7edee386bfb5a899fa5ae9f24117c4b1fe649286651ece45b3dc2007cb8a163bf0598da48361c55d39a69163fa8fd24cf5f83655d23dca3ad961c62f356208552bb9ed529077096966d670c354e4abc9804f1746c08ca237327ffffffffffffffff
g = 0x02
A = 0x387367618042a11df5caa640a340c66c9cdb100eeb1a64dca7e7c5dabfcea9eb5f08a62868ab6a822f1c7576b4419964128fe3676da5f4edb9f8f4aba7f4e6c7578596125875bfc14897ef3cd273c73f93d9beaf9c429989669a89976214ccb91aecff97548931f88e62d48d5f847da24b6e525e58b99f70adafc58e31fc46171e083dfe25c45f653f2ca28bb5a49eb3f3439b5a2003bf695001168a38e761e16e8da9c849aecedb48c69e947eec6eeb98557c8b908a90663a7c8afeede26068
B = 0x57334bfaf2695b08518032495fb39b1bc05f8e5a3821aefbbf97445af8c10cf29328e01c41b58b71eaa1b59124c455e565b6f491075ec95265a85902d4f76ac1c024161358aebc708b6a07ec5603d31119705de508e2282df79f45b393f2a7c7a33f3338b8889204f6b960c11c6a628b2404a760a61949d15620c884dd7807decd7cb12a074144da97eb9a5880d42d18bae71e98f8ef9b3ecf71fbb26105c29873eb69ad1443983a1a6f813dbef83f4f082477ff3686d1259c98865d8908aa20
iv= "c44c21e7df32a5b70c31457b092c274c"
encrypted = "1172654d6da540164f2ffa7b420935fcd781a7af2ca34bc4dcfd041679dddf0b2dd36ed7765e41ddb514ffbc266e4e2d"
#A = g*a % p
#shared = A*b % p = g*a*b
a = A*inverse(g,p)
shared = B*a%p
shared_secret = 1547922466740669851136899009270554812141325611574971428561894811681012510829813498961168330963719034921137405736161582760628870855358912091728546731744381382987669929718448423076919613463237884695314172139247244360699127770351428964026451292014069829877638774839374984158095336977179683450837507011404610904412301992397725594661037513152497857482717626617522302677408930050472100106931529654955968569601928777990379536458959945351084885704041496571582522945310187
#iv = '737561146ff8194f45290f5766ed6aba'
ciphertext = '39c99bf2f0c14678d6a5416faef954b5893c316fc3c48622ba1fd6a9fe85f3dc72a29c394cf4bc8aff6a7b21cae8e12c'

print(decrypt_flag(shared, iv, encrypted))
