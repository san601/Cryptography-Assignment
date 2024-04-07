from Crypto.Util.number import *
from pwn import *
import json
import telnetlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from PIL import Image
import numpy as np


img1 = Image.open('flag_.png')
img2 = Image.open('lemur.png')

img1 = np.array(img1)
img2 = np.array(img2)

img3 = img1 ^ img2

img3 = Image.fromarray(img3)
img3.save('hehe.png')