import sys
import re
import textwrap
import math
import binascii

def leftShiftBin(inp):
    out = ""
    for i in range(len(inp)-1):
        out = out + inp[i+1]
    out = out + inp[0]
    return out

def desKeyComb(R, Kn):
    E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
        20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    #SBOX
    S_BOX = [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],],
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],],
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],],
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],],
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],],
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],],
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],],
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],]]


    ER = ""

    for i in E:
        ER = ER + R[i-1]

    #print(R)
    #print(ER)
    #print(Kn)

    KER = bin(int(ER, 2) ^ int(Kn, 2))[2:].zfill(48)

    sBoxOut = ""

    for i in range(8):
        Bi = KER[i*6:(i+1)*6]
        row = int(Bi[0] + Bi[5], 2)
        col = int(Bi[1:5], 2)
        sBoxOut = sBoxOut + bin(S_BOX[i][row][col])[2:].zfill(4)

    #print(sBoxOut)

    P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

    output = ""

    for i in P:
        output = output + sBoxOut[i-1]


    return output

def desGenKeys(key):
    keyAsDecInt = int(key, 16)
    keyAsBinStr = bin(keyAsDecInt)
    K = keyAsBinStr[2:].zfill(64)
    K_Plus = ""
    subK_Plus = []

    PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,   10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
            63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,  14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

    PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,    15, 6, 21, 10, 23, 19, 12, 4,
            26, 8, 16, 7, 27, 20, 13, 2,    41, 52, 31, 37, 47, 55, 30, 40,
            51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

    for i in PC_1:
        K_Plus = K_Plus + K[i-1]

    C = [K_Plus[:28]]
    D = [K_Plus[28:]]

    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    for i in range(16):
        C.append(leftShiftBin(C[i]) if shifts[i] == 1 else leftShiftBin(leftShiftBin(C[i])))
        D.append(leftShiftBin(D[i]) if shifts[i] == 1 else leftShiftBin(leftShiftBin(D[i])))

    CD = [C[i] + D[i] for i in range(17)]

    for i in range(16):
        subK_Plus.append("")
        for j in PC_2:
            subK_Plus[i] = subK_Plus[i] + CD[i+1][j-1]

    #SubK_Plus is the resultant key list
    return subK_Plus

def desSingleSegDecrypt(M, subK_Plus, isDecrypt):
    IP_Mat = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,     62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

    PI_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,   38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,       34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]
    IP = ""

    for i in IP_Mat:
        IP = IP + str(M[i-1])

    #print(IP)

    L = [IP[:32]]
    R = [IP[32:]]

    for i in range(16):
        L.append(R[i])
        R.append(bin(int(L[i], 2)^int(desKeyComb(R[i], subK_Plus[15-i if isDecrypt else i]), 2))[2:].zfill(32))

    RL = R[16] + L[16]

    cipherAsBinStr = ""
    for i in PI_1:
        cipherAsBinStr = cipherAsBinStr + RL[i-1]
    cipherAsDecInt = int(cipherAsBinStr, 2)
    cipherAsHexStr = hex(cipherAsDecInt)[2:]
    return cipherAsHexStr


def decryptCaesar(cipher, key):
    plain = ""

    for i in cipher:
        oldVal = ord(i)
        newVal = (-key + oldVal)
        while(newVal >= 127):
            newVal = newVal - 95
        while(newVal <= 31):
            newVal = newVal + 95
        plain = plain + chr( newVal )
    return plain

def decryptDES(cipher, key, isDecrypt, isHexOutput):
    #Step 1: generate subkeys
    subK_Plus = desGenKeys(key)

    #Step 2: Decode Data 64 bits at a time
    cipherAsDecInt = int(cipher, 16)
    cipherAsBinStr = bin(cipherAsDecInt)[2:]
    length = 64 * math.ceil(len(cipherAsBinStr)/64)
    cipherAsBinStr = cipherAsBinStr.zfill(length)
    cipherAsBinStrSegments = textwrap.wrap(cipherAsBinStr, 64)

    resultHex = ""
    for seg in cipherAsBinStrSegments:
        resultHex = resultHex + desSingleSegDecrypt(seg, subK_Plus, isDecrypt)

    result = str(binascii.unhexlify(resultHex))[2:-1] if not isHexOutput else resultHex

    return result
def decrypt3DES(cipher, key):
    keys = textwrap.wrap(key, 16)

    result = ""
    if(len(keys) == 2):
        result = decryptDES(cipher, keys[0], True, True)
        result = decryptDES(result, keys[1], False, True)
        result = decryptDES(result, keys[1], True, False)
    else:
        result = decryptDES(cipher, keys[0], True, True)
        result = decryptDES(result, keys[1], True, True)
        result = decryptDES(result, keys[2], True, False)
    return result
def decryptAES(cipher):
    return cipher
def decryptRSA(cipher):
    return cipher
def decryptECC(cipher):
    return cipher


def isValidText(s):
    result = True
    for i in s:
        if not isValidChar(i):
            result = False
    return result

def isValidChar(c):
    return (32 <= ord(c)) and (126 >= ord(c))


def reqDecryption():
    decryption = ""
    plaintext = ""
    #prompt user for decryption method
    print("\nPlease select a decryption algorithm")
    print("\n[", end="")
    for n in options.keys():
        print(str(n)+ " : " + options[n], end=" | " if n != len(options) else "")
    print("]")

    #get user input for decryption method
    valid = False
    while not valid:
        response = input("\n>> ")
        print()
        try:
            userChoice = int(response)
            if userChoice <= len(options) and userChoice >= 1:
                decryption = userChoice
                valid = True
            else:
                raise ValueError()
        except ValueError:
            print("Please enter a number (1-" + str(len(options)) + "):")
    print("You have chosen " + str(decryption) + ": " + options[decryption])


    #prompt user input, ask for string to encrpyt
    print("\nPlease enter a string to decrypt")

    #get user input for string to decrypt
    valid = False
    while not valid:
        ciphertext = input("\n>> ")
        if len(ciphertext) < 100 and isValidText(ciphertext):
            valid = True
        else:
            print("\nPlease enter a string using only the letters A-Z and ,.?!(); less than 100 charactrs in length\n")

    print("\nPlaintext:\n" + ciphertext + "\n")

    #prompt user for key value
    print("\nPlease input your key")

    #get user input for key value
    valid = False
    while not valid:
        response = input("\n>> ")
        print()
        try:
            key = int(response)
            valid = True
        except ValueError:
            print("Please enter a number")
    print("You have chosen " + str(key) + " as your key")

    return decryption, ciphertext, key



options = {
    1:"Caesar",  #symmetric
    2:"DES",     #
    3:"3DES",    #
    4:"AES",     #symmetric
    5:"RSA",     #asymmetric
    6:"ECC",     #
}
decryption = 1
plaintext = ""
ciphertext = ""
key = 0

#print(str(sys.argv))

args = sys.argv

if len(args) < 2:

    decryption, ciphertext, key = reqDecryption() #Make specific requests for each option

else:

    try:
        decryption = int(args[1])
        if(decryption == 1):
            key = int(args[2])
        elif(decryption == 2):
            key = args[2]
            if(not len(key) == 16):
                raise ValueError()
        elif(decryption == 3):
            key = args[2]
            if(not len(key) == 48 and not len(key) == 32):
                raise ValueError()
        else:
            key = args[2]
        if not (decryption <= len(options) and decryption >= 1):
            raise ValueError()
    except ValueError:
        print("\nInput should be of the form:\n\tpython decrypt.py [DECRYPTION] [KEY] '[PLAINTEXT]'")
        print("\nDecryption Algorithms Available: ")
        print("\n[", end="")
        for n in options.keys():
            print(str(n)+ " : " + options[n], end=" | " if n != len(options) else "")
        print("]")
        print("\nDECRYPTION should be integer value\n")
        print("\KEY should be either integer value or hexadecimal for longer keys\n")
        print("\nEnsure you use single quotes ('') for PLAINTEXT to avoid terminal misreading\n")
        sys.exit()
    args.pop(0)
    args.pop(0)
    args.pop(0)

    ciphertext = " ".join(args)

#select/call decryption algorithm
output = ""
if(decryption == 1):
    output = decryptCaesar(ciphertext, key)
elif(decryption == 2):
    output = decryptDES(ciphertext, key, True, False)
elif(decryption == 3):
    output = decrypt3DES(ciphertext, key)
elif(decryption == 4):
    output = decryptAES(ciphertext)
elif(decryption == 5):
    output = decryptRSA(ciphertext)
elif(decryption == 6):
    output = decryptECC(ciphertext)
plaintext = output

print("\nCiphertext:\n" + ciphertext + "\n")
print("Plaintext:\n" + plaintext + "\n")
