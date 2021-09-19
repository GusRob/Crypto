import math
import textwrap
import binascii

E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
#SBOX
des_S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],]
    ]

P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

PC_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,   10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,  14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

PC_2 = [14, 17, 11, 24, 1, 5, 3, 28,    15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,    41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

IP_Mat = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,     62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,        61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,   38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,       34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def leftShiftBin(inp):
    out = ""
    for i in range(len(inp)-1):
        out = out + inp[i+1]
    out = out + inp[0]
    return out

def desKeyComb(R, Kn):
    ER = ""
    for i in E:
        ER = ER + R[i-1]
    KER = bin(int(ER, 2) ^ int(Kn, 2))[2:].zfill(48)
    sBoxOut = ""
    for i in range(8):
        Bi = KER[i*6:(i+1)*6]
        row = int(Bi[0] + Bi[5], 2)
        col = int(Bi[1:5], 2)
        sBoxOut = sBoxOut + bin(des_S_BOX[i][row][col])[2:].zfill(4)

    #print(sBoxOut)
    output = ""
    for i in P:
        output = output + sBoxOut[i-1]
    return output

def desGenKeys(keyIn):
    keyAsDecInt = int(keyIn, 16)
    keyAsBinStr = bin(keyAsDecInt)
    K = keyAsBinStr[2:].zfill(64)
    K_Plus = ""
    subK_Plus = []

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

def desSingleSegEncrypt(M, subK_Plus, isEncrypt):
    IP = ""

    for i in IP_Mat:
        IP = IP + str(M[i-1])

    #print(IP)

    L = [IP[:32]]
    R = [IP[32:]]

    for i in range(16):
        L.append(R[i])
        R.append(bin(int(L[i], 2)^int(desKeyComb(R[i], subK_Plus[i if isEncrypt else (15-i)]), 2))[2:].zfill(32))

    RL = R[16] + L[16]

    cipherAsBinStr = ""
    for i in PI_1:
        cipherAsBinStr = cipherAsBinStr + RL[i-1]
    cipherAsDecInt = int(cipherAsBinStr, 2)
    cipherAsHexStr = hex(cipherAsDecInt)[2:]
    length = round(len(cipherAsHexStr)/2)*2

    return cipherAsHexStr.zfill(length)

def encryptDESHex2Hex(inputAsHexStr, keyAsHexStr, isEncrypt):
    #STEP 1: Generate subkeys
    subK_Plus = desGenKeys(keyAsHexStr)

    #STEP 2: Encode data 64 bits at a time
    inputAsDecInt = int(inputAsHexStr , 16)
    inputAsBinStr = bin(inputAsDecInt)[2:]
    length = 64 * math.ceil(len(inputAsBinStr)/64)
    inputAsBinStr = inputAsBinStr.zfill(length)
    inputAsBinStrSegments = textwrap.wrap(inputAsBinStr, 64)

    result = ""
    for seg in inputAsBinStrSegments:
        result = result + desSingleSegEncrypt(seg, subK_Plus, isEncrypt)

    return result


def encryptDES(input, keyAsHexStr, isEncrypt):
    inputAsHexStr = input.encode("utf-8").hex() if isEncrypt else input

    result = encryptDESHex2Hex(inputAsHexStr, keyAsHexStr, isEncrypt)

    result = str(binascii.unhexlify(result))[2:-1] if not isEncrypt else result

    return result

def encrypt3DES(input, keyIn, isEncrypt):
    keys = textwrap.wrap(keyIn, 16)

    inputAsHexStr = input.encode("utf-8").hex() if isEncrypt else input

    result = ""

    if(len(keys) == 2):
        result = encryptDESHex2Hex(inputAsHexStr, keys[0], isEncrypt)
        result = encryptDESHex2Hex(result, keys[1], not isEncrypt)
        result = encryptDESHex2Hex(result, keys[0], isEncrypt)
    else:
        result = encryptDESHex2Hex(inputAsHexStr, keys[0] if isEncrypt else keys[2], isEncrypt)
        result = encryptDESHex2Hex(result, keys[1], not isEncrypt)
        result = encryptDESHex2Hex(result, keys[2] if isEncrypt else keys[0], isEncrypt)

    result = str(binascii.unhexlify(result))[2:-1] if not isEncrypt else result

    return result
