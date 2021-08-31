import sys
import re
import textwrap
import math
import binascii
import time

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
    des_S_BOX = [
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
        sBoxOut = sBoxOut + bin(des_S_BOX[i][row][col])[2:].zfill(4)

    #print(sBoxOut)

    P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
        2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

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
    length = round(len(cipherAsHexStr)/2)*2

    return cipherAsHexStr.zfill(length)

def aesGenState(segIn):
    stateOut = [["00" for i in range(4)] for i in range(4)]


    byteInSeg = 0
    for x in range(4):
        for y in range(4):
            stateOut[x][y] = segIn[byteInSeg*8 : (byteInSeg+1)*8]
            byteInSeg = byteInSeg+1

    return stateOut

def aesGenStateReverse(stateIn):
    segOut = ""

    for x in range(4):
        for y in range(4):
            segOut = segOut + stateIn[x][y]
        segOut = segOut

    return segOut

def aesSubWord(word):
    aes_S_BOX = [
        ["63", "7c", "77", "7b", "f2", "6b", "6f", "c5", "30", "01", "67", "2b", "fe", "d7", "ab", "76"],["ca", "82", "c9", "7d", "fa", "59", "47", "f0", "ad", "d4", "a2", "af", "9c", "a4", "72", "c0"],
        ["b7", "fd", "93", "26", "36", "3f", "f7", "cc", "34", "a5", "e5", "f1", "71", "d8", "31", "15"],["04", "c7", "23", "c3", "18", "96", "05", "9a", "07", "12", "80", "e2", "eb", "27", "b2", "75"],
        ["09", "83", "2c", "1a", "1b", "6e", "5a", "a0", "52", "3b", "d6", "b3", "29", "e3", "2f", "84"],["53", "d1", "00", "ed", "20", "fc", "b1", "5b", "6a", "cb", "be", "39", "4a", "4c", "58", "cf"],
        ["d0", "ef", "aa", "fb", "43", "4d", "33", "85", "45", "f9", "02", "7f", "50", "3c", "9f", "a8"],["51", "a3", "40", "8f", "92", "9d", "38", "f5", "bc", "b6", "da", "21", "10", "ff", "f3", "d2"],
        ["cd", "0c", "13", "ec", "5f", "97", "44", "17", "c4", "a7", "7e", "3d", "64", "5d", "19", "73"],["60", "81", "4f", "dc", "22", "2a", "90", "88", "46", "ee", "b8", "14", "de", "5e", "0b", "db"],
        ["e0", "32", "3a", "0a", "49", "06", "24", "5c", "c2", "d3", "ac", "62", "91", "95", "e4", "79"],["e7", "c8", "37", "6d", "8d", "d5", "4e", "a9", "6c", "56", "f4", "ea", "65", "7a", "ae", "08"],
        ["ba", "78", "25", "2e", "1c", "a6", "b4", "c6", "e8", "dd", "74", "1f", "4b", "bd", "8b", "8a"],["70", "3e", "b5", "66", "48", "03", "f6", "0e", "61", "35", "57", "b9", "86", "c1", "1d", "9e"],
        ["e1", "f8", "98", "11", "69", "d9", "8e", "94", "9b", "1e", "87", "e9", "ce", "55", "28", "df"],["8c", "a1", "89", "0d", "bf", "e6", "42", "68", "41", "99", "2d", "0f", "b0", "54", "bb", "16"]
    ]
    output = ""
    for i in range(4):
        iByte = word[8*i:8*(i+1)]
        row = int(iByte[:4], 2)
        col = int(iByte[4:], 2)
        output = output + bin(int(aes_S_BOX[row][col], 16))[2:].zfill(8)
    return output

def aesRotWord(word):
    return word[8:] + word[:8]

def aesGenKeys(keyIn, NbNkNr):
    Nb = NbNkNr[0]
    Nk = NbNkNr[1]
    Nr = NbNkNr[2]

    keyAsDecInt = int(keyIn, 16)
    keyAsBinStr = bin(keyAsDecInt)[2:].zfill(Nk*32)
    keyAsBinStrOfBytes = textwrap.wrap(keyAsBinStr, 8)

    w = ["" for i in range(Nb*(Nr+1))]

    r_con = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
    )

    for i in range(Nk):
        w[i] = (keyAsBinStrOfBytes[4*i] + keyAsBinStrOfBytes[(4*i)+1] + keyAsBinStrOfBytes[(4*i)+2] + keyAsBinStrOfBytes[(4*i)+3])

    for i in range(Nb*(Nr+1)):
        if i < Nk:
            i = Nk
        temp = w[i-1]
        if i % Nk == 0:
            temp = aesSubWord(aesRotWord(temp))
            tempFirstByte = bin(int(temp[:8], 2)^r_con[int(i/Nk)])[2:].zfill(8)
            temp = tempFirstByte + temp[8:]
        elif (Nk > 6 and i % Nk == 4):
            temp = aesSubWord(temp)
        w[i] = bin(int(w[i-Nk], 2) ^ int(temp, 2))[2:].zfill(8*Nb)
    return w

def aesInvSubBytes(stateIn):
    aes_INV_S_BOX = [
        ["52", "09", "6a", "d5", "30", "36", "a5", "38", "bf", "40", "a3", "9e", "81", "f3", "d7", "fb"],["7c", "e3", "39", "82", "9b", "2f", "ff", "87", "34", "8e", "43", "44", "c4", "de", "e9", "cb"],
        ["54", "7b", "94", "32", "a6", "c2", "23", "3d", "ee", "4c", "95", "0b", "42", "fa", "c3", "4e"],["08", "2e", "a1", "66", "28", "d9", "24", "b2", "76", "5b", "a2", "49", "6d", "8b", "d1", "25"],
        ["72", "f8", "f6", "64", "86", "68", "98", "16", "d4", "a4", "5c", "cc", "5d", "65", "b6", "92"],["6c", "70", "48", "50", "fd", "ed", "b9", "da", "5e", "15", "46", "57", "a7", "8d", "9d", "84"],
        ["90", "d8", "ab", "00", "8c", "bc", "d3", "0a", "f7", "e4", "58", "05", "b8", "b3", "45", "06"],["d0", "2c", "1e", "8f", "ca", "3f", "0f", "02", "c1", "af", "bd", "03", "01", "13", "8a", "6b"],
        ["3a", "91", "11", "41", "4f", "67", "dc", "ea", "97", "f2", "cf", "ce", "f0", "b4", "e6", "73"],["96", "ac", "74", "22", "e7", "ad", "35", "85", "e2", "f9", "37", "e8", "1c", "75", "df", "6e"],
        ["47", "f1", "1a", "71", "1d", "29", "c5", "89", "6f", "b7", "62", "0e", "aa", "18", "be", "1b"],["fc", "56", "3e", "4b", "c6", "d2", "79", "20", "9a", "db", "c0", "fe", "78", "cd", "5a", "f4"],
        ["1f", "dd", "a8", "33", "88", "07", "c7", "31", "b1", "12", "10", "59", "27", "80", "ec", "5f"],["60", "51", "7f", "a9", "19", "b5", "4a", "0d", "2d", "e5", "7a", "9f", "93", "c9", "9c", "ef"],
        ["a0", "e0", "3b", "4d", "ae", "2a", "f5", "b0", "c8", "eb", "bb", "3c", "83", "53", "99", "61"],["17", "2b", "04", "7e", "ba", "77", "d6", "26", "e1", "69", "14", "63", "55", "21", "0c", "7d"]
    ]
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            row = int(stateIn[x][y][:4], 2)
            col = int(stateIn[x][y][4:], 2)
            stateOut[x][y] = bin(int(aes_INV_S_BOX[row][col], 16))[2:].zfill(8)
    return stateOut

def aesInvShiftRows(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            stateOut[y][x] = stateIn[(y-x)%4][x]
    return stateOut

def aesInvMixColumns(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


    for y in range(4):
        a = [int(stateIn[y][x], 2) for x in range(4)]
        u = xtime(xtime(a[0] ^ a[2]))
        v = xtime(xtime(a[1] ^ a[3]))
        stateOut[y][0] = bin(a[0]^u)[2:].zfill(8)
        stateOut[y][1] = bin(a[1]^v)[2:].zfill(8)
        stateOut[y][2] = bin(a[2]^u)[2:].zfill(8)
        stateOut[y][3] = bin(a[3]^v)[2:].zfill(8)

    for y in range(4):
        a = [int(stateOut[y][x], 2) for x in range(4)]
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        stateOut[y][0] = bin(a[0] ^ (t ^ xtime(a[0] ^ a[1])))[2:].zfill(8)
        stateOut[y][1] = bin(a[1] ^ (t ^ xtime(a[1] ^ a[2])))[2:].zfill(8)
        stateOut[y][2] = bin(a[2] ^ (t ^ xtime(a[2] ^ a[3])))[2:].zfill(8)
        stateOut[y][3] = bin(a[3] ^ (t ^ xtime(a[3] ^ u)))[2:].zfill(8)
    return stateOut

def aesAddRoundKey(stateIn, K):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    subKeySet = [textwrap.wrap(i, 8) for i in K]
    stateOut = aesGenState(bin(int(aesGenStateReverse(stateIn), 2) ^ int(aesGenStateReverse(subKeySet), 2))[2:].zfill(128))
    return stateOut

def aesSingleSegDecrypt(state, w, NbNkNr):
    Nb = NbNkNr[0]
    Nk = NbNkNr[1]
    Nr = NbNkNr[2]

    state = aesAddRoundKey(state, w[Nr*Nb:(Nr+1)*Nb])

    for round in map(lambda n: n+1, reversed(range(Nr-1))):
        state = aesInvShiftRows(state)
        state = aesInvSubBytes(state)
        state = aesAddRoundKey(state, w[round*Nb:((round+1)*(Nb))])
        state = aesInvMixColumns(state)

    state = aesInvShiftRows(state)
    state = aesInvSubBytes(state)
    state = aesAddRoundKey(state, w[0:Nb])

    return state

def decryptCaesar(cipher, keyIn):
    plain = ""

    for i in cipher:
        oldVal = ord(i)
        newVal = (-keyIn + oldVal)
        while(newVal >= 127):
            newVal = newVal - 95
        while(newVal <= 31):
            newVal = newVal + 95
        plain = plain + chr( newVal )
    return plain

def decryptDES(cipher, keyAsHexStr, isDecrypt, isHexOutput):
    #Step 1: generate subkeys
    subK_Plus = desGenKeys(keyAsHexStr)

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

def decrypt3DES(cipher, keyIn):
    keys = textwrap.wrap(keyIn, 16)

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

def decryptAES(cipher, keyIn):

    Nb = 4                      #No. of 32 bit words comprising the state
    Nk = int(len(keyIn)/8)          #No. of 32 bit words comprising the key
    Nr = 10 if Nk == 4 else (12 if Nk == 6 else 14) #No. of rounds

    #Step 1: generate subkeys
    subKeys = aesGenKeys(keyIn, (Nb, Nk, Nr))

    #Step 2: enode data 128 bits at a time
    cipherAsDecInt = int(cipher , 16)
    cipherAsBinStr = bin(cipherAsDecInt)[2:]
    length = 128 * math.ceil(len(cipherAsBinStr)/128)
    cipherAsBinStr =cipherAsBinStr.zfill(length)
    cipherAsBinStrSegments = textwrap.wrap(cipherAsBinStr, 128)

    result = ""
    for seg in cipherAsBinStrSegments:
        cipherState = aesGenState(seg)
        plainState = aesSingleSegDecrypt(cipherState, subKeys, (Nb, Nk, Nr))
        result = result + aesGenStateReverse(plainState)

    plainAsDecInt = int(result, 2)
    plainAsHexStr = hex(plainAsDecInt)[2:]
    print(plainAsHexStr)

    result = str(binascii.unhexlify(plainAsHexStr))[2:-1]

    return result

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
        elif(decryption == 4):
            key = args[2]
            if(not len(key) == 64 and not len(key) == 48 and not len(key) == 32):
                raise ValueError()
        else:
            key = args[2]
        if decryption > len(options) or decryption < 1 or len(args) < 4:
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

#start timer
startTime = time.time()

#select/call decryption algorithm
output = ""
if(decryption == 1):
    output = decryptCaesar(ciphertext, key)
elif(decryption == 2):
    output = decryptDES(ciphertext, key, True, False)
elif(decryption == 3):
    output = decrypt3DES(ciphertext, key)
elif(decryption == 4):
    output = decryptAES(ciphertext, key)
elif(decryption == 5):
    output = decryptRSA(ciphertext)
elif(decryption == 6):
    output = decryptECC(ciphertext)
plaintext = output

#end timer
endTime = time.time()

print("\nCiphertext:\n" + ciphertext + "\n")
print("Plaintext:\n" + plaintext + "\n")

print("Time Taken: " + str(endTime-startTime) + "s\n")
