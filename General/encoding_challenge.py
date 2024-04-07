from pwn import *  # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13377, level='debug')


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def rot13(cipher) -> str:
    cipher = list(cipher)
    for i in range(len(cipher)):
        if cipher[i] == '_':
            continue
        cipher[i] = chr((((ord(cipher[i]) - 97) - 13) % 26) + 97)
    return ''.join(cipher)


for i in range(100):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    encoded = ''
    if received["type"] == "base64":
        encoded = base64.b64decode(received["encoded"]).decode()
    elif received["type"] == "hex":
        encoded = bytes.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        encoded = rot13(received["encoded"])
    elif received["type"] == "bigint":
        encoded = bytes.fromhex(received["encoded"][2:]).decode()
    elif received["type"] == "utf-8":
        encoded = ''.join(chr(i) for i in received["encoded"])

    to_send = {
        "decoded": encoded
    }
    json_send(to_send)

flag = json_recv()
print(flag['flag'])
