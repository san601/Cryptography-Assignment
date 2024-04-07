def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    return x % m

def solve_congruences(a1, m1, a2, m2, a3, m3):
    M = m1 * m2 * m3
    M1 = M // m1
    M2 = M // m2
    M3 = M // m3
    y1 = modinv(M1, m1)
    y2 = modinv(M2, m2)
    y3 = modinv(M3, m3)
    x = (a1 * M1 * y1 + a2 * M2 * y2 + a3 * M3 * y3) % M
    return x

# Test the function with the given congruences
a1 = 2
m1 = 5
a2 = 3
m2 = 11
a3 = 5
m3 = 17
print(solve_congruences(a1, m1, a2, m2, a3, m3))  # Output: a
