import math
import textwrap
import binascii

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

def aesSubBytes(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            row = int(stateIn[x][y][:4], 2)
            col = int(stateIn[x][y][4:], 2)
            stateOut[x][y] = bin(int(aes_S_BOX[row][col], 16))[2:].zfill(8)
    return stateOut


def aesInvSubBytes(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            row = int(stateIn[x][y][:4], 2)
            col = int(stateIn[x][y][4:], 2)
            stateOut[x][y] = bin(int(aes_INV_S_BOX[row][col], 16))[2:].zfill(8)
    return stateOut

def aesShiftRows(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            stateOut[y][x] = stateIn[(y+x)%4][x]
    return stateOut

def aesInvShiftRows(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    for x in range(4):
        for y in range(4):
            stateOut[y][x] = stateIn[(y-x)%4][x]
    return stateOut

def aesMixColumns(stateIn):
    stateOut = [[stateIn[x][y] for x in range(4)] for y in range(4)]
    xtime = lambda a: (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)

    for y in range(4):
        a = [int(stateIn[y][x], 2) for x in range(4)]
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        stateOut[y][0] = bin(a[0] ^ (t ^ xtime(a[0] ^ a[1])))[2:].zfill(8)
        stateOut[y][1] = bin(a[1] ^ (t ^ xtime(a[1] ^ a[2])))[2:].zfill(8)
        stateOut[y][2] = bin(a[2] ^ (t ^ xtime(a[2] ^ a[3])))[2:].zfill(8)
        stateOut[y][3] = bin(a[3] ^ (t ^ xtime(a[3] ^ u)))[2:].zfill(8)
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

def aesSingleSegEncrypt(state, w, NbNkNr):
    Nb = NbNkNr[0]
    Nk = NbNkNr[1]
    Nr = NbNkNr[2]

    state = aesAddRoundKey(state, w[0:Nb])

    for round in map(lambda n: n+1, range(Nr-1)):
        state = aesSubBytes(state)
        state = aesShiftRows(state)
        state = aesMixColumns(state)
        state = aesAddRoundKey(state, w[round*Nb:((round+1)*(Nb))])

    state = aesSubBytes(state)
    state = aesShiftRows(state)
    state = aesAddRoundKey(state, w[Nr*Nb:((Nr+1)*(Nb))])

    return state

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


def encryptAES(input, keyIn, isEncrypt):
    Nb = 4                      #No. of 32 bit words comprising the state
    Nk = int(len(keyIn)/8)          #No. of 32 bit words comprising the key
    Nr = 10 if Nk == 4 else (12 if Nk == 6 else 14) #No. of rounds

    #Step 1: generate subkeys
    subKeys = aesGenKeys(keyIn, (Nb, Nk, Nr))

    #Step 2: enode data 128 bits at a time     testStrings:     "00112233445566778899aabbccddeeff"  "3243F6A8885A308D313198a2e0370734"
    inputAsHexStr = input.encode("utf-8").hex() if isEncrypt else input
    inputAsDecInt = int(inputAsHexStr , 16)
    inputAsBinStr = bin(inputAsDecInt)[2:]
    length = 128 * math.ceil(len(inputAsBinStr)/128)
    inputAsBinStr = inputAsBinStr.zfill(length)
    inputAsBinStrSegments = textwrap.wrap(inputAsBinStr, 128)

    result = ""
    for seg in inputAsBinStrSegments:
        inputState = aesGenState(seg)
        outputState = aesSingleSegEncrypt(inputState, subKeys, (Nb, Nk, Nr)) if isEncrypt else aesSingleSegDecrypt(inputState, subKeys, (Nb, Nk, Nr))
        result = result + aesGenStateReverse(outputState)

    outputAsDecInt = int(result, 2)
    outputAsHexStr = hex(outputAsDecInt)[2:]
    result = str(binascii.unhexlify(outputAsHexStr))[2:-1] if not isEncrypt else outputAsHexStr

    return result
