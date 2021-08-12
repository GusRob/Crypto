import sys
import re

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
def decryptDES(cipher):
    return cipher
def decrypt3DES(cipher):
    return cipher
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
        key = int(args[2])
        if not (decryption <= len(options) and decryption >= 1):
            raise ValueError()
    except ValueError:
        print("\nInput should be of the form:\n\tpython decrypt.py [ENCRYPTION] [KEY] [PLAINTEXT]")
        print("\nDecryption Algorithms Available: ")
        print("\n[", end="")
        for n in options.keys():
            print(str(n)+ " : " + options[n], end=" | " if n != len(options) else "")
        print("]")
        print("\nENCRYPTION and KEY should be integer values\n")
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
    output = decryptDES(ciphertext)
elif(decryption == 3):
    output = decrypt3DES(ciphertext)
elif(decryption == 4):
    output = decryptAES(ciphertext)
elif(decryption == 5):
    output = decryptRSA(ciphertext)
elif(decryption == 6):
    output = decryptECC(ciphertext)
plaintext = output

print("\nCiphertext:\n" + ciphertext + "\n")
print("Plaintext:\n" + plaintext + "\n")
