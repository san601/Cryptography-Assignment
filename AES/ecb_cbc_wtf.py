import os

iv = os.urandom(16)
print(len(iv.hex()))
a = 'eed934a273821c508880ce3d431d4094cdb6f093dfab429cd56b151bae4368bea629d7bd6efcc50f3c41bc0538986d2f'
print(a[:32])
print(a[32:32+32])
print(a[32+32:])