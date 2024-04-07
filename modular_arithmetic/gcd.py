def gcd(a : int, b: int) -> int:
    while (a != b):
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

if __name__ == "__main__":
    print(gcd(66528, 52920))