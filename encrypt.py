from Key import *


nrBits = 3


def encrypt(data, key):
    encryptData = ""
    for char in data:
        encryptData += oneTo8(modular_pow(ord(char), key.exponent, key.modul))
    return encryptData


def encryptChar(base, exponent, modulus):
    return (base**exponent) % modulus


def modular_pow(base, exponent, modulus):
    if modulus == 1:
        return 0
    c = 1
    for _ in range(0, exponent):
        c = (c * base) % modulus
    return c


def oneTo8(encryptedInt):
    myBinary = ('{0:0'+str(8*nrBits)+'b}').format(encryptedInt)
    # print(myBinary)
    encryptedChar = ""
    while myBinary != "":
        encryptedChar += chr(int(myBinary[:8], 2))
        myBinary = myBinary[8:]
    return encryptedChar
