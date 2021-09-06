import sys
import re
import textwrap
import math
import time

import des #custom Library
import aes #custom Library
import rsa #custom Library

def encryptCaesar(input, keyIn, isEncrypt):
    output = ""

    for i in input:
        oldVal = ord(i)
        newVal = ((keyIn if isEncrypt else -keyIn) + oldVal)
        while(newVal >= 127):
            newVal = newVal - 95
        while(newVal <= 31):
            newVal = newVal + 95
        output = output + chr( newVal )
    return output

options = {
    "Caesar":1,  #symmetric
    "DES":2,     #
    "3DES":3,    #
    "AES":4,     #symmetric
    "RSA":5,     #asymmetric
    "ECC":6,     #
}
encryption = 1
input = ""
output = ""
isEncrypt = True
key = 0

#print(str(sys.argv))

args = sys.argv
try:

    #Too few Arguments or too many arguments
    if(len(args) < 5 or len(args) > 5):
        raise ValueError

    #Set isEncrypt
    if(args[1] == "encrypt"):
        isEncrypt = True
    elif(args[1] == "decrypt"):
        isEncrypt = False
    else:
        raise ValueError

    #Find encryption method from dictionary
    try:
        encryption = int(args[2]) #integer entered
    except ValueError:
        if args[2] in options.keys():
            encryption = options[args[2]] #String equivalent from dictionary entered

    #check validity of encryption
    if encryption > len(options) or encryption < 1:
        raise ValueError()

    #Check key length and format based on encryption method
    if(encryption == 1):
        key = int(args[3]) #Caesar cipher requires integer key
    elif(encryption == 2):
        key = args[3]       #DES requires hex key
        if(not len(key) == 16):
            raise ValueError()
    elif(encryption == 3):
        key = args[3]       #3DES requires Hex key
        if(not len(key) == 48 and not len(key) == 32):
            raise ValueError()
    elif(encryption == 4):
        key = args[3]       #AES requires hex key
        if(not len(key) == 64 and not len(key) == 48 and not len(key) == 32):
            raise ValueError()
    else:
        key = args[3]       #temp catch

    input = args[4]
except ValueError:
    #Error Messages
    print("\nInput should be of the form:\n\tpython crypto.py [ENCRYPT/DECRYPT] [ENCRYPTION] [KEY] '[INPUTSTR]'")
    print("\nEncryption Algorithms Available: ")
    print("\n[", end="")
    for item in options.items():
        print(str(item[0])+ " : " + str(item[1]), end=" | " if item[1] != len(options) else "")
    print("]")
    print("\nENCRYPT/DECRYPT should be either 'encrypt' or 'decrypt'\n")
    print("ENCRYPTION should be integer value\n")
    print("KEY should be either integer value or hexadecimal for longer keys\n")
    print("\nEnsure you use single quotes ('') for INPUTSTR to avoid terminal misreading\n")
    sys.exit()

#start timer
startTime = time.time()

#select/call encryption algorithm
if(encryption == 1):
    output = encryptCaesar(input, key, isEncrypt)
elif(encryption == 2):
    output = des.encryptDES(input, key, isEncrypt)
elif(encryption == 3):
    output = des.encrypt3DES(input, key, isEncrypt)
elif(encryption == 4):
    output = aes.encryptAES(input, key, isEncrypt)
elif(encryption == 5):
    output = rsa.encryptRSA(input, key, isEncrypt)
elif(encryption == 6):
    output = encryptECC(input)

#end timer
endTime = time.time()

print("\nInput:\n" + input + "\n")
print("Output:\n" + output + "\n")

print("Time Taken: " + str(endTime-startTime) + "s\n")
