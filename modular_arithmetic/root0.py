ints = [14, 6, 11]
res = [a for a in range(29) if (a*a % 29) in ints]
print(min(res))