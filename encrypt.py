import sys
import re

#print(str(sys.argv))

def encryptCaesar():
    return ""
def encryptDES():
    return ""
def encrypt3DES():
    return ""
def encryptAES():
    return ""
def encryptRSA():
    return ""
def encryptECC():
    return ""

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
    response = input("\n>> ")
    if re.match("^[A-z,.?!(); ]*$", response) and len(response) < 100:
        valid = True
    else:
        print("\nPlease enter a string using only the letters A-Z and ,.?!(); less than 100 charactrs in length")

#clean user input
for i in response:
    val = ord(i)
    if val >= 97 and val <= 122:
        plaintext +=  chr(val-32)
    elif val >= 65 and val <= 90:
        plaintext += i
print("\nPlaintext: " + plaintext)

#select/call encryption algorithm
output = ""
if(encryption == 1):
    output = encryptCaesar()
elif(encryption == 2):
    output = encryptDES()
elif(encryption == 3):
    output = encrypt3DES()
elif(encryption == 4):
    output = encryptAES()
elif(encryption == 5):
    output = encryptRSA()
elif(encryption == 6):
    output = encryptECC()
ciphertext = output

print("Ciphertext:\n" + ciphertext)
