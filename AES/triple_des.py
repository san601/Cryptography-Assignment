import requests

url = "https://aes.cryptohack.org/triple_des/"
key = '00' * 8 + 'ff' * 8
cipher = requests.get(url + "encrypt_flag/" + key + "/").json()["ciphertext"]
cipher = requests.get(url + "encrypt/" + key + "/" + cipher + "/").json()["ciphertext"]
print(bytes.fromhex(cipher).decode())
