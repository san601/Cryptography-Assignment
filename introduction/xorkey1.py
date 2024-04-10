secret = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
flag = ''

if __name__ == "__main__":
    key = "myXORkey" * 6
    part = bytes.fromhex(secret)
    flag = ""
    for i in range(42):
        flag += chr(ord(key[i]) ^ part[i])
    print(flag)
