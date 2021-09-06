import sys
import secrets
import random

def gcd(a, b):
   while a != 0:
      a, b = b % a, a
   return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        raise ValueError
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def rabinMiller(num):
    s = num - 1
    t = 0

    while s % 2 == 0:
        s = s // 2
        t += 1
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
        return True
def isPrime(num):
    if (num < 2):
        return False
    lowPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61,
    67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
    157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241,
    251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,317, 331, 337, 347, 349,
    353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
    457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
    571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
    673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
    797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907,
    911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if (num % prime == 0):
            return False
    return rabinMiller(num)
def generateLargePrime(keysize = 1024):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num
def rsaGenerateKey(keySize):
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    p = generateLargePrime(keySize)
    q = generateLargePrime(keySize)
    n = p * q
    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1).
    while True:
        e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        if gcd(e, (p - 1) * (q - 1)) == 1:
            break
    # Step 3: Calculate d, the mod inverse of e.
    d = findModInverse(e, (p - 1) * (q - 1))
    publicKey = (hex(n)[2:], hex(e)[2:])
    privateKey = (hex(n)[2:], hex(d)[2:])
    return (publicKey, privateKey)

def writeFile(filename, input):
    file = open(filename, "w")
    file.write(input)
    file.close()


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
        if(keyLen == 0):
            keyLen = 1024
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
elif(encryption == 5):
    key = rsaGenerateKey(keyLen)
else:
    print("Something went wrong")
    exit(0)

if(encryption != 5):
    print(key)
else:
    filepathPublic = "RSA_Keys/Public.txt"
    filepathPrivate = "RSA_Keys/Private.txt"
    print("Writing Public Key to " + filepathPublic)
    print("Writing Private Key to " + filepathPrivate)
    writeFile(filepathPublic, "Public Key: " + str(key[0]))
    writeFile(filepathPrivate, "Private Key: " + str(key[1]))
    print("Completed RSA Key Generation")
