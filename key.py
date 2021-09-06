import sys
import secrets


args = sys.argv

encryption = 0
keyLen = 0
key = 0

options = {
    "Caesar":1,  #symmetric
    "DES":2,     #
    "3DES":3,    #
    "AES":4,     #symmetric
    "RSA":5,     #asymmetric
    "ECC":6,     #
}

try:
    #check number of arguments
    if(len(args) < 2 or len(args) > 2):
        raise ValueError
    #get encryption and keyLength
    for item in options:
        if args[1].startswith(item):
            encryption = int(options[item])
            if("-" in args[1]):
                keyLen = int(args[1].split("-",1)[1])
            break
    if(encryption == 1):
        keyLen = 0
    elif(encryption == 2):
        if(keyLen == 0 or keyLen == 64):
            keyLen = 8
        else:
            raise ValueError
    elif(encryption == 3):
        if(keyLen == 0 or keyLen == 2 or keyLen == 128):
            keyLen = 16
        elif(keyLen == 3 or keyLen == 192):
            keyLen = 24
        else:
            raise ValueError
    elif(encryption == 4):
        if(keyLen == 0 or keyLen == 128):
            keyLen = 16
        elif(keyLen == 192):
            keyLen = 24
        elif(keyLen == 256):
            keyLen = 32
        else:
            raise ValueError
    elif(encryption == 5):
        keyLen = 0
    else:
        raise ValueError
except ValueError:
    print("\nInput should be of the form:\n\n\tpython key.py [ENCRYPTION]")
    print("\nENCRYPTION should be the algorithm to use")
    print("\nFor algorithms with multiple key lengths available, key length should follow the encryption with a hyphen separator")
    print("\ne.g.  ENCRYPTION-KEYLEN where KEYLEN is in bits/number of keys for 3DES\n")
    exit(0)


if(encryption == 1):
    key = secrets.randbelow(25)+1
elif(encryption in [2, 3, 4]):
    key = secrets.token_hex(keyLen)
else:
    print("Something went wrong")
    exit(0)

print(key)
