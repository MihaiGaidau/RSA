import Key

def encrypt(key, data):
    encryptData = ""
    for char in data:
        encryptData+=encryptChar(char, key.second, key.prime)
    return encryptData

def encryptChar(char, exponent, mod):
    return (char**exponent) % mod