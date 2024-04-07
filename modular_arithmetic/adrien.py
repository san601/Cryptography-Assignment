a = 288260533169915
p = 1007621497415251
def decrypt_flag(hehe):
    plaintext = []
    for i in hehe:
        if pow(i, (p - 1) // 2, p) == 1:
            plaintext.append('1')
        else:
            plaintext.append('0')
    plaintext = ''.join(plaintext)
    reversed(plaintext)
    plaintext = ''.join([chr(int(plaintext[i:i + 8], 2)) for i in range(0, len(plaintext), 8)])
    return plaintext

hehe1 = open("output_adrien.txt").read().replace('[', '').replace(']', '').replace('\n', '').split(', ')
hehe = [int(i) for i in hehe1]
print(decrypt_flag(hehe))