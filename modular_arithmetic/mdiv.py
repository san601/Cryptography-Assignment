if __name__ == "__main__":
    """
    Using Little Fermat, realized that a ^ (p - 1) % p == 1 <=> a ^ (p - 1) congruent with 1 mod p
    <=> a ^ (p - 2) * a * a^(-1) congruent with a ^ (-1) % p
    <=> a ^ (p - 2) congruent with a ^ (-1) % p
    <=> a ^ p * a ^ (-2) congruent with a ^ (-1) % p 
    => inverse element: d = a ^ (-2)
    """
    # 3 * d congruent with 1 mod p=13 => 3 * d mod m = 1 => d is mod inverse of 3 (mod 13)
    # pow() function can solve this
    print(pow(3, 13 - 2, 13))