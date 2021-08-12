import sys
import re

#print(str(sys.argv))

def encryptCaesar(plain):
    key = 0
    cipher = ""
    #prompt user for key value
    print("\nPlease input your key")

    #get user input for encryption method
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

    for i in plain:
        oldVal = ord(i)
        newVal = (key + oldVal)
        if(newVal >= 126):
            newVal = newVal - 95
        cipher = cipher + chr( newVal )
    return cipher
def encryptDES(plain):
    return plain
def encrypt3DES(plain):
    return plain
def encryptAES(plain):
    return plain
def encryptRSA(plain):
    return plain
def encryptECC(plain):
    return plain


def isValidText(s):
    result = True
    for i in s:
        if not isValidChar(i):
            result = False
    return result

def isValidChar(c):
    return (32 <= ord(c)) and (126 >= ord(c))



options = {
    1:"Caesar",  #symmetric
    2:"DES",     #
    3:"3DES",    #
    4:"AES",     #symmetric
    5:"RSA",     #asymmetric
    6:"ECC",     #
}
encryption = 1
plaintext = ""
ciphertext = ""

#prompt user for encryption method
print("\nPlease select an encryption algorithm")
print("\n[", end="")
for n in options.keys():
    print(str(n)+ " : " + options[n], end=" | " if n != len(options) else "")
print("]")

#get user input for encryption method
valid = False
while not valid:
    response = input("\n>> ")
    print()
    try:
        userChoice = int(response)
        if userChoice <= len(options) and userChoice >= 1:
            encryption = userChoice
            valid = True
        else:
            raise ValueError()
    except ValueError:
        print("Please enter a number (1-" + str(len(options)) + "):")
print("You have chosen " + str(encryption) + ": " + options[encryption])


#prompt user input, ask for string to encrpyt
print("\nPlease enter a string to encrypt")

#get user input for string to encrypt
valid = False
while not valid:
    plaintext = input("\n>> ")
    if len(plaintext) < 100 and isValidText(plaintext):
        valid = True
    else:
        print("\nPlease enter a string using only the letters A-Z and ,.?!(); less than 100 charactrs in length\n")

print("\nPlaintext:\n" + plaintext + "\n")

#select/call encryption algorithm
output = ""
if(encryption == 1):
    output = encryptCaesar(plaintext)
elif(encryption == 2):
    output = encryptDES(plaintext)
elif(encryption == 3):
    output = encrypt3DES(plaintext)
elif(encryption == 4):
    output = encryptAES(plaintext)
elif(encryption == 5):
    output = encryptRSA(plaintext)
elif(encryption == 6):
    output = encryptECC(plaintext)
ciphertext = output

print("\nPlaintext:\n" + plaintext + "\n")
print("Ciphertext:\n" + ciphertext + "\n")
