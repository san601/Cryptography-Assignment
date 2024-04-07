from Crypto.PublicKey import RSA

a = RSA.importKey(open('bruce_rsa.pub').read())
print(a.n)