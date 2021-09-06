import sys
import time
import aes
import des

example = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris sapien turpis, tristique non ante a, venenatis dictum risus. In sed placerat quam. Vestibulum rutrum semper nibh. Cras pellentesque feugiat pellentesque. Morbi pharetra elit turpis, id aliquam nunc consequat eget. Fusce interdum eros ante, sed facilisis velit consequat vitae. Praesent mattis, ex eget malesuada accumsan, ipsum enim ornare ex, sit amet venenatis elit dolor malesuada justo. Donec sit amet tincidunt ex. In vitae elit volutpat odio."
key = "1234567890ABCDEF"

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

def errorMsg():
    print("\nUsage:")
    print("\tpython benchmark.py [ENCRYPTION] [NTRIES] [KEYLEN]")
    print("\nEncryption Algorithms Available: ")
    print("\n[", end="")
    for item in options.items():
        print(str(item[0])+ " : " + str(item[1]), end=" | " if item[1] != len(options) else "")
    print("]")
    print("\nWhere [ENCRYPTION] is an integer referring to the encryption algorithm")
    print("\nWhere [NTRIES] is an optional integer referring to the number of times to execute the algorithm, default 1000")
    print("\nWhere [KEYLEN] is number of bits in key to use (128, 192, 156) or number of keys to use (3DES)\n")
    exit(0)

options = {
    "Caesar":1,  #symmetric
    "DES":2,     #
    "3DES":3,    #
    "AES":4,     #symmetric
    "RSA":5,     #asymmetric
    "ECC":6,     #
}

args = sys.argv
encryption = 1
keyLen = 0
nTests = 1000


if(len(args) >= 3):
    try:
        nTests = int(args[2])
    except ValueError:
        errorMsg()
if(len(args) >= 2):
    #Find encryption method from dictionary
    try:
        encryption = int(args[1]) #integer entered
    except ValueError:
        if args[1] in options.keys():
            encryption = options[args[1]] #String equivalent from dictionary entered
        else:
            errorMsg()

    #check validity of encryption
    if encryption > len(options) or encryption < 1:
        errorMsg()
if(len(args) == 4):
    try:
        keyLen = int(args[3])
    except ValueError:
        errorMsg()
elif(len(args) < 2 or len(args) > 4):
    errorMsg()

if(encryption == 1):
    key = 10
elif(encryption == 2):
    key = "1234567890ABCDEF"
elif(encryption == 3):
    if(keyLen == 0 or keyLen == 2 or keyLen == 128 or keyLen == 112):
        keyLen = " with 2 keys"
        key = "1234567890ABCDEFFEDCBA0987654321"
    elif(keyLen == 3 or keyLen == 192 or keyLen == 168):
        keyLen = " with 3 keys"
        key = "1234567890ABCDEFFEDCBA098765432124680BDFECA97531"
    else:
        errorMsg()
elif(encryption == 4):
    if(keyLen == 0 or keyLen == 2 or keyLen == 128):
        keyLen = "-128"
        key = "1234567890ABCDEFFEDCBA0987654321"
    elif(keyLen == 3 or keyLen == 192):
        keyLen = "-192"
        key = "1234567890ABCDEFFEDCBA098765432124680BDFECA97531"
    elif(keyLen == 4 or keyLen == 256):
        keyLen = "-256"
        key = "1234567890ABCDEFFEDCBA098765432124680BDFECA9753113579ACEFDB08642"
    else:
        errorMsg()
elif(encryption == 5):
    input = encryptRSA(example)
elif(encryption == 6):
    input = encryptECC(example)


start = time.time()
print("Started encryption")

#exection loop
if(encryption == 1):
    input = encryptCaesar(example, key, True)
elif(encryption == 2):
    input = des.encryptDES(example, key, True)
elif(encryption == 3):
    input = des.encrypt3DES(example, key, True)
elif(encryption == 4):
    input = aes.encryptAES(example, key, True)
elif(encryption == 5):
    input = encryptRSA(example)
elif(encryption == 6):
    input = encryptECC(example)

print("Finished encryption")
print("Started decryption")


for i in range(nTests):
    if(encryption == 1):
        output = encryptCaesar(input, key, False)
    elif(encryption == 2):
        output = des.encryptDES(input, key, False)
    elif(encryption == 3):
        output = des.encrypt3DES(input, key, False)
    elif(encryption == 4):
        output = aes.encryptAES(input, key, False)
    elif(encryption == 5):
        output = encryptRSA(input)
    elif(encryption == 6):
        output = encryptECC(input)

end = time.time()

encryptionStr = "Error"
for item in options.items():
    if item[1] == encryption:
        encryptionStr = item[0]
print("Finished " + str(nTests) + " encryptions using " + encryptionStr + (keyLen if type(keyLen) == str else ""))

print("Time Taken: " + str(end-start) + "s")
