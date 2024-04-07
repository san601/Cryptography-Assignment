from Crypto.PublicKey import RSA

a = RSA.importKey(open('privacy_enhanced_mail.pem').read())
print(a.d)