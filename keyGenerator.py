import random
import math
import Key


def generateKeys(prime1, prime2 ):
    n = prime1 * prime2
    fi = (prime1-1)*(prime2-1)
    e,d = findED(fi, 1000)
    # print("n=",n)
    # print("fi=",fi)
    # print("e=",e)
    # print("d=",d)

    publica = Key.Key()
    publica.exponent = int(e)
    publica.modul = int(n)

    privata = Key.Key()
    privata.exponent = int(d)
    privata.modul = int(n)

    return privata, publica



def findNearPrime(number):
    if checkIfPrime(number):
        return number
    for i in range(number):
        if checkIfPrime(abs(number - i)):
            return abs(number - i)
        if checkIfPrime(number + i):
            return number + 1
        
def findED(fi, treshold):
    while True:
        eps = generateRandomNumber(fi)
        for _ in range(treshold):
            k = generateRandomNumber(10000)
            if ((k*fi)+1)%eps == 0:
                #print("k=",k)
                return eps, (k*fi + 1) / eps
    return 1,1

def generateRandomNumber(maxValue):
    return random.randint(0, maxValue)

def checkIfPrime(n):
    j = 2
    while j <= math.sqrt(n):
        if n % j == 0:
            return False
        j += 1
        return True
        

