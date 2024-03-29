from sys import argv
import io
from decrypt import *
from encrypt import *
from keyGenerator import *
import Key

maxRandomNumber = 500
fileToRead = 'in.txt'
outFile = 'crypted.txt'
outFile2 = 'decrypted.txt'



def readFromFile(file):
    myFile = io.open(fileToRead, "r+", encoding="utf-8")
    data = myFile.read()
    myFile.close()
    return data


# def manageInputs(argv):
#     if len(argv) == 3:
#         dataToEncrypt = readFromFile(argv[1])
#         fileToWrite = open(argv[2], "w")
#         return dataToEncrypt, fileToWrite


def main():
    out = io.open(outFile, "w", encoding="utf-8")
    out2 = io.open(outFile2, "w", encoding="utf-8")
    random1 = generateRandomNumber(maxRandomNumber)
    random2 = generateRandomNumber(maxRandomNumber)

    prime1 = findNearPrime(random1)
    prime2 = findNearPrime(random2)

    privata, publica = generateKeys(prime1, prime2)
    print(privata, publica)

    textToEncrypt = readFromFile(fileToRead)
    encryptedData = encrypt(textToEncrypt, privata)
    print("crypted", encryptedData)
    out.write(encryptedData)
    decryptedData = decrypt(encryptedData, publica)
    out2.write(decryptedData)
    # #print("decrypted", decryptedData)
    out.close()
    out2.close()


if __name__ == "__main__":
    main()
