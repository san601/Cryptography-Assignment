from Crypto.PublicKey import RSA

a = RSA.importKey(open('transparency.pem').read())

import hashlib
from Crypto.PublicKey import RSA

a = 112105991116784701231126410351951161171141105111495495610050102975048125
print(long_to_bytes(a))