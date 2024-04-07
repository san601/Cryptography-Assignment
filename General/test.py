import math
from Crypto.Util.number import inverse
from sympy import *
import numpy as np

# u1 = v1
# Loop i = 2,3...,n
#    Compute μij = vi ∙ uj / ||uj||2, 1 ≤ j < i.
#    Set ui = vi - μij * uj (Sum over j for 1 ≤ j < i)
# End Loop

