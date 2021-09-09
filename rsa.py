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
    output = [hex((char ** key) % n)[2:] for char in input]
    print([int(x, 16) for x in output])
    output = "".join(output)
    return output

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
