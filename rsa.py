import textwrap

def readKeyFromFile(filepath):
    file = open(filepath, "r")
    key = file.read()
    file.close()
    return key[12:] if key[1] == "u" else key[13:]

def encryptRSA(input, keyFilepath, isEncrypt):
    output = ""
    n, key = tuple(readKeyFromFile(keyFilepath).split(", "))
    n = int(n[2:-1], 16)
    key = int(key[1:-2], 16)

    #CLEAN INPUT
    '''
    if(isEncrypt):
        input = input.encode("utf-8").hex()

    input = bin(int(input, 16))[2:]
    input = textwrap.wrap(input, 32)
    '''
    #output = [str((int(char, 2) ** key) % n).zfill(3) for char in input]

    #RESOLVING OUTPUT
    return "".join(output)
