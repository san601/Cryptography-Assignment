from Crypto.Util.number import *
def is_generator(k,p):
    for n in range(2,p):
        if pow(k,n,p) == k:
            return False
    return True

#7
p = 28151
for i in range(p):
    if is_generator(i,p):
        print(i)
        break