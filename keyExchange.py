import math
import random

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
def generateLargePrime(keysize = 512):
    while True:
        num = random.randrange(2**(keysize-1), 2**(keysize))
        if isPrime(num):
            return num

# Variables Used
print("Please enter all values in hex format\n")
print("Please Enter Publicly Shared Prime:")
sharedPrime = 0
while(not isPrime(sharedPrime)):
    inputPrime = input(">>> ")
    if(not inputPrime == ''):
        sharedPrime = int(inputPrime, 16)    # p
    else:
        sharedPrime = generateLargePrime()
print("Please Enter Publicly Shared Base:")
sharedBase = int(input(">>> "), 16)      # g

print("Please Enter User1 Secret Key")
user1Key = int(input(">>> "), 16)     # a
print("Please Enter User2 Secret Key")
user2Key = int(input(">>> "), 16)      # b

# Begin
print( "Publicly Shared Variables:")
print( "    Publicly Shared Prime: " , hex(sharedPrime)[2:] )
print( "    Publicly Shared Base:  " , hex(sharedBase)[2:] )
print( "Privately Held Variables:")
print( "    User1 Private Key: " , hex(user1Key)[2:] )
print( "    User2 Private Key:  " , hex(user2Key)[2:] )

# Alice Sends Bob A = g^a mod p
A = pow(sharedBase, user1Key, sharedPrime)
print( "\nAlice Sends Over Public Chanel: " , hex(A)[2:] )

# Bob Sends Alice B = g^b mod p
B = pow(sharedBase, user2Key, sharedPrime)
print( "\nBob Sends Over Public Chanel: ", hex(B)[2:] )

print( "\n------------\n" )
print( "Privately Calculated Shared Secret:" )
# Alice Computes Shared Secret: s = B^a mod p
user1SharedSecret = pow(B, user1Key, sharedPrime)
print( "\nUser1 Shared Secret: ", hex(user1SharedSecret)[2:] )

# Bob Computes Shared Secret: s = A^b mod p
user2SharedSecret = pow(A, user2Key, sharedPrime)
print( "\nUser2 Shared Secret: ", hex(user2SharedSecret)[2:] )
