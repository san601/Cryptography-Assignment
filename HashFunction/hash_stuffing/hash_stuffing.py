from pwn import *  # pip install pwntools
import json

r = remote('socket.cryptohack.org', 13405, level='debug')

block1 = b'\x01' * 32
block2 = b'\x01' * 31
block1 = block1.hex()
block2 = block2.hex()
payload = json.dumps({"m1": block1, "m2": block2}).encode()

r.sendlineafter(b'JSON: ', payload)
r.recvline()
r.close()

