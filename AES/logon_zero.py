from pwn import *
import json

r = remote('socket.cryptohack.org', 13399)
reset_pwd = {'option': 'reset_password', 'token': (b'\x00'*28).hex()}
authenticate = {'option': 'authenticate', 'password': ""}
reset_connection = {'option': 'reset_connection'}
ans = ""
r.recvline().decode()
cnt = 0
while True:
    cnt += 1
    print(f"Attempt {cnt}")
    r.sendline(json.dumps(reset_pwd).encode())
    r.recvline().decode()
    r.sendline(json.dumps(authenticate).encode())
    ans = r.recvline().decode()
    if "crypto" in ans:
        print(ans)
        r.close()
        break
    r.sendline(json.dumps(reset_connection).encode())
    r.recvline().decode()
