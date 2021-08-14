# Crypto
Practicing Encryption/Decryption Algorithms

## This repository will consist of a self project in which i will attempt to:
  *  - [X] Create a program that can encrypt sentences with basic algorithms
  *  - [X] Create a program that can decrypt sentences with basic algorithms
  *  - [ ] Improve the encryption program to more advanced algorithms
  *  - [ ] Improve the decryption program to more advanced algorithms
  *  - [ ] Develop a key-sharing algorithm implementation?

## Bot List

Algorithm | Symmetry | Completed
 :---:|:---:|:---: 
**Caesar** | Symmetric |  <ul><li>- [X] </li></ul>
**DES** | Symmetric |  <ul><li>- [X] </li></ul>
**3DES** | Symmetric |  <ul><li>- [ ] </li></ul>
**AES** | Symmetric |  <ul><li>- [ ] </li></ul>
**RSA** | Asymmetric |  <ul><li>- [ ] </li></ul>
**ECC** | Asymmetric |  <ul><li>- [ ] </li></ul>

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
