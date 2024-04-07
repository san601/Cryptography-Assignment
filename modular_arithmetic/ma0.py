def solve(con_mod : int, mod : int) -> int:
    return con_mod % mod
if __name__ == "__main__":
    print(solve(11, 6), solve(8146798528947, 17))