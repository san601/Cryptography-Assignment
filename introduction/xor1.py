# KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
# KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
# KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
# FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf 

from Crypto.Util.number import *

def xor(string1 : str, string2 : str) -> None | str:
    if len(string1) != len(string2):
        print("Both string must have the same length!")
        return None
    try:
        res = hex(int(string1, 16) ^ int(string2, 16))
    except Exception as e:
        print(e)
        return None
    return res[2::]

if __name__ == "__main__":
    KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
    KEY2 = xor(KEY1, "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
    KEY3 = xor(KEY2, "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
    FLAG = xor(xor(xor(KEY1, KEY2), KEY3), "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
    print(bytes.fromhex(FLAG))