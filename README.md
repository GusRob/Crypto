# Crypto
Practicing Encryption/Decryption Algorithms

### crypto.py

`python crypto.py [ISENCRYPT] [ENCRYPTION] [KEY] '[INPUT]'`

  * Where '[ISENCRYPT]' sets the program to either encrypt or decrypt the given input, this argument can either be 'encrypt' or 'decrypt'
  * Where '[ENCRYPTION]' is an integer ID corresponding to the encryption algorithm to be used (shown in table below)
  * Where '[KEY]' is a key in the format shown in the table below
  * The output will be the hexadecimal ciphertext or ASCII plaintext, except for ceasar cipher which always outputs ASCII

### key.py

`python key.py [KEYLEN] [KEYBASE]`

  * Where both `[KEYLEN]` and `[KEYBASE]` are integer values
  * `[KEYLEN]` is in # of bits
  * `[KEYLEN]` is a multiple of 8
  * `[KEYBASE]` is one of `2`, `8`, `10` or `16`
  * The `[KEYBASE]` argument is optional, will default to 16

## This repository will consist of a self project in which i will attempt to:
  *  - [X] Create a program that can encrypt sentences with basic algorithms
  *  - [X] Create a program that can decrypt sentences with basic algorithms
  *  - [ ] Improve the encryption program to more advanced algorithms
  *  - [ ] Improve the decryption program to more advanced algorithms
  *  - [ ] Develop a key-sharing algorithm implementation?

## Encryption Algorithm List

Algorithm | Symmetry | Completed | ID | Key Format | Key Length (bits : hex chars)
 :---:|:---:|:---:|:---:|:---:|:---:
**Caesar** | Symmetric |  <ul><li>- [X] </li></ul> | 1 | Decimal | INT_MAX
**DES** | Symmetric |  <ul><li>- [X] </li></ul> | 2 | Hexadecimal | 64 : 16
**3DES** | Symmetric |  <ul><li>- [X] </li></ul> | 3 | Hexadecimal | 128 : 32 or 192 : 48
**AES** | Symmetric |  <ul><li>- [X] </li></ul> | 4 | Hexadecimal | 128 : 32 or 192 : 48 or 256 : 64
**RSA** | Asymmetric |  <ul><li>- [ ] </li></ul> | 5 | N/A | N/A
**ECC** | Asymmetric |  <ul><li>- [ ] </li></ul> | 6 | N/A | N/A

### Estimation of Time to Brute-Force

In the case of multiple key sizes, **[CIPHER]-[KEYVARIATION]** has been used. The final three columns show the estimated time taken to test the given percentage of all possible keys; e.g. For DES there are 288230376151711744 keys to test, so in the column labelled '50%', there will be the estimated time taken to test 144115188075855872 keys. In the column labelled 'Av Time To Decrypt' the average time to decrypt is calculated using the average of 1000 decryptions of a sample block of text, which is kept constant across the ciphers.

Algorithm | No. Of Keys | Av Time To Decrypt (seconds) | 50% (years) | 90% (years) | 100% (years)
 :---:|:---:|:---:|:---:|:---:|:---:
**Caesar** | 25 | 0.15515875816345215 | N/A | N/A | N/A
**DES** | 2^58 | 24.41735816001892 | N/A | N/A | N/A
**3DES-2KEY** | 2^112 | 74.09152507781982 | N/A | N/A | N/A
**3DES-3KEY** | 2^168 | 72.97424387931824 | N/A | N/A | N/A th
**AES-128** | 2^128 | 52.747599840164185 | N/A | N/A | N/A
**AES-192** | 2^192 | 62.59677004814148 | N/A | N/A | N/A
**AES-256** | 2^256 | 74.68215489387512 | N/A | N/A | N/A
**RSA** | N/A | N/A | N/A | N/A | N/Are
**ECC** | N/A | N/A | N/A | N/A | N/A

Obviously using a laptop CPU to solve an embarassingly parallelisable problem such as decryption is by no means the most efficient method to crack any of these ciphers, and the table shows how long a brute force attack might take on this device. However this does pose a starting point for how long a sophisticated attack might take on such a cipher. Following a normal distribution, the probabillity of the key being found by the time that 50% of keys have been tried is quite high, and multiple cores testing keys simultaneously would divide the problem massively and can make breaking these codes much quicker, but brute force attacks are still by no means feasible in most cases. For example, the 'record' for cracking DES currently sits at 23 hours, using far more sophisticated attacks than brute forcing every key possible, exploiting weaknesses in the encryption algorithm itself. However thease measurements of the time taken to decrypt give an indication to compare algorithms with each other. 

AES encryption is yet to be repeatably broken. While there are exploits to reduce the time taken to test possible keys, or to minimie the key space, the length of time required to test a reasonable proportion of the key space is still far too large for this to be possible. This is reflected in the above table where AES-256 requires over 2.4\*10^68 years to solve which would still be a ridiculously large number, even with unlimited funds to complete. 

## Milestone Log

2021/08/11
  * Skeleton code written to take user input, clean it and call algorithm depending on user request
  * Currently, user input accepted for plaintext is limited to alphabet and basic punctuation incl. `\n ( ) , . ? ! ;`
  * User input is cleaned as follows:
    * All characters capitalised
    * All punctuation removed
    * All spaces removed
  * Need to update to allow punctuation and numbers to be included in plaintext before the encryption algorithms are written

2021/08/12
  * Identical/mirror version of skeleton code created for the decryption algorithms (necessary to test the encryption)
  * User input is now allowed for all characters with char values 32-126 incl.
  * User input now no longer needs to be thoroughly cleaned as the character codes are used
  * Both programs can be run with a single line using command line args as follows:
    * `python encrypt.py [ENCRYPTION] [KEY] '[PLAINTEXT]'`
    * Where:
      * `[ENCRYPTION]` and `[KEY]` are both integer values with encryption corresponding to the dictionary key-value pairs of the algorithms
      * `[PLAINTEXT]` is written surrounded in single quotes so that the terminal ignores special characters
  * Todo:
    * Find out how to make sure the plaintext input is surrounded by single quotes, and request the user re-enters their command if so
    * Write an encryption and decryption algorithm to implement DES encryption

2021/08/13
  * Caesar cipher has been implemented in both encrypting and decrypting
  * DES encryption and encryption works
  * DES de/encryption only accepts keys of 64 bits, as is the standard for storing DES keys
  * http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm used for structure

2021/08/14
  * 3DES implemented with 2 and 3 key variations
  * DES encryption correction made as key variable name caused mismatched usage
    * Was not a problem for DES encryption as the key variable was constant throughout program
    * 3DES implementation calls the DES Encryption algorithm multiple times with different keys so made the error apparent
  * Todo:
    * Create AES encryption and decryption
      * https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf could be used
    * Test program on larger strings of text (e.g. whole paragraphs)
    * Test user input to only allow plaintext with single quotes surrounding

2021/08/22
  * Simple pseudo-random key generation implemented
  * Should be useful for more in depth testing of the encryption algorithms
  * Usage is as follows:
    * `python key.py [KEYLEN] [KEYBASE]`
    * Where:
      * Both `[KEYLEN]` and `[KEYBASE]` are integer values
      * `[KEYLEN]` is in bits
      * `[KEYLEN]` is a multiple of 8
      * `[KEYBASE]` is one of `2`, `8`, `10` or `16`
      * The `[KEYBASE]` argument is optional, will default to 16
  * The secrets.py module is used as opposed to the random.py module
  * The secrets library function used is `secrets.token_hex([nbytes=None])` as this generates a random text string in hexadecimal format

2021/08/30
  * Skeleton code for functions of AES implementation added
  * Main AES loop calling encryption functions implemented
  * Included a timer library to time completion of encryption/decryption functions
    * Included to allow for potential cracking of encrypted ciphertext without key
    * (I have no intention for this currently, but it may prove useful to test encryption implementations too)
    * Should this be the case however, a link to a github page with a 'gibberish classifier' could prove useful, shown below
      * https://github.com/thomas-daniels/GibberishClassifier-Python/blob/master/gibberishclassifier.py

2021/08/31
  * AES encryption and decryption implemented
  * Key length can be of 128, 192 or 256 bits
  * Uses mix_columns and inv_mix_columns algorithms from https://github.com/boppreh/aes/blob/master/aes.py for more concise code
  * Using Time Taken addition, it is possible to calculate how long it might take to brute force the key using this machine, added to README.md
  * Todo:
    * Develop asymmetric key cipher algorithms, starting with either RSA or ECC
    * Implement asymmetric key generation into the `key.py` program
    * Develop a key-sharing algorithm??

2021/09/02
  * Redesigned the program to separate code corresponding to different algorithms
  * The AES and DES algorithms now exist in separate libraries `aes.py` and `des.py` to the main executable, `crypto.py` 
  * Caesar Cipher, as a single short function still exists within `crypto.py`
  * `crypto.py` is now able to encrypt and decrypt without having to call different files
  * Changes completed in a different branch, needs to be merged to main
  * Todo:
    * Further algorithms that are implemented will be done as separate libraries too
    * RSA will be next to implement
    * Need to devise how `key.py` can output asymmetric key-pairs
  
