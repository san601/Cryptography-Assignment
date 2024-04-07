def my_little_fermat(base : int, exponent: int, mod : int) -> int:
    diff = mod - exponent
    if diff == 0:
        return base
    elif diff > 0:
        return base // (base**diff)
    else:
        return base * base * (-diff)
    
if __name__ == "__main__":
    print(my_little_fermat(273246787654, 65536, 65537))