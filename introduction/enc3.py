import base64

if __name__ == "__main__":
    hex_ = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
    string = bytes.fromhex(hex_)
    print(base64.b64encode(string).decode())