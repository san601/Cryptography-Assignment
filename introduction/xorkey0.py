secret = '73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'

if __name__ == "__main__":
    flag = ''
    bytes_arr = bytes.fromhex(secret)
    for key in range(256):
        flag = ''
        for byte in bytes_arr:
            flag += chr(key ^ byte)
        if "crypto{" in flag:
            print(f"The flag is: {flag}")
            print(f"Secret key is: {hex(key)}")
