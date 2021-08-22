import sys
import secrets


args = sys.argv

keyBytes = 0

keyBase = 16

try:
    keyLen = int(args[1])
    if(not keyLen%8 == 0):
        raise ValueError
    keyBytes = int(keyLen/8)
    if(len(args) > 2):
        keyBase = int(args[2])
    if(not keyBase in [2, 8, 10, 16]):
        raise ValueError
except ValueError:
    print("\nInput should be of the form:\n\n\tpython key.py [KEYLEN] \nOR\n\tpython key.py [KEYLEN] [KEYBASE]")
    print("\nBoth arguments KEYLEN and KEYBASE should be integers")
    print("\nKEYLEN should be in bits, KEYLEN should be divisible by 8")
    print("\nKEYBASE should be either 2, 8, 10 or 16")


key = secrets.token_hex(keyBytes)

if(not keyBase == 16):
    intKey = int(key, 16)
    if(keyBase == 2):
        key = bin(intKey)[2:]
    elif(keyBase == 8):
        key = oct(intKey)[2:]
    elif(keyBase == 10):
        key = intKey

print(key)
