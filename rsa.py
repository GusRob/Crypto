import textwrap
import binascii
import math

def readKeyFromFile(filepath):
    file = open(filepath, "r")
    key = file.read()
    file.close()
    return key[12:] if key[1] == "u" else key[13:]

def encryptRSAHex2Hex(input, key, n, blockSize):
    input = [int(x, 16) for x in textwrap.wrap(input, blockSize)]
    print(input)
    output = [hex(pow(char, key, n))[2:] for char in input]
    print([int(x, 16) for x in output])
    output = "".join(output)
    return output

def singleBlockRSA(a, b, n): #(X * Y) mod N = (X mod N) * (Y mod N) mod N



    ''' RECURSIVE FUNCTION IMPL - DOESNT WORK NUMBERS TOO BIG MAX RECURSION DEPTH LIMIT
    if b == 0:
        return 1
    elif not b % 2 == 0:
        return (singleBlockRSA(a, b-1, n) * a) % n
    else:
        return (singleBlockRSA(a, b/2, n)**2) % n
    '''
    return (a**b) % n

def encryptRSA(input, keyFilepath, isEncrypt):
    output = ""
    n, key = tuple(readKeyFromFile(keyFilepath).split(", "))
    blockSizeHex = len(n)-3
    n = int(n[2:-1], 16)
    key = int(key[1:-2], 16)

    inputAsHexStr = input.encode("utf-8").hex() if isEncrypt else input
    length = math.ceil(len(inputAsHexStr)/blockSizeHex)*blockSizeHex
    inputAsHexStr = inputAsHexStr.zfill(length)

    output = encryptRSAHex2Hex(inputAsHexStr, key, n, blockSizeHex)

    output = str(binascii.unhexlify(output))[2:-1] if not isEncrypt else output


    return output
