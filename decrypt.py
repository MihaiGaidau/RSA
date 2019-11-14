import Key
from encrypt import modular_pow, nrBits
import keyGenerator


def decrypt(data, key):
    decryptedData = ""
    while data:
        eight = data[:nrBits]
        myBinary = ""
        for char in eight:
            #print("char: '", char, "'")
            myBinary += '{0:08b}'.format(ord(char))
        #print(myBinary)
        myInt = int(myBinary, 2)
        #print("fromBinary: ", myInt)
        decryptedInt = modular_pow(myInt, key.exponent, key.modul)
        #print("myIntBack:", decryptedInt)
        decryptedChar = chr(decryptedInt)

        decryptedData += decryptedChar
        data = data[nrBits:]
    return decryptedData
