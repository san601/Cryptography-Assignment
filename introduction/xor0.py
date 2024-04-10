def xor(string : str, interger : int) -> str:
    '''Xor a string with a number, then convert it back to a new string'''
    xored = ''.join([chr(ord(char) ^ interger) for char in string])
    return xored

if __name__ == "__main__":
    string = 'label'
    flag = "crypto{" + xor(string, 13) + "}"
    print(flag)