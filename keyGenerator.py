import random
import math
import Key


def generateKeys(prime1, prime2):
    n = prime1 * prime2
    fi = (prime1-1)*(prime2-1)
    e, d = findED(fi)
    #print(prime1, " ", prime2)
    #print("n=", n)
    #print("fi=", fi)
    #print("e=", e)
    #print("d=", d)

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


def findED(fi):
    d = 1
    while d == 1:
        eps = generateRandomNumber(fi)
        while gcd(eps, fi) != 1:
            eps = generateRandomNumber(fi)
        d = modInverse(eps, fi)
    return eps, d


def generateRandomNumber(maxValue):
    return random.randint(0, maxValue)


def checkIfPrime(n):
    j = 2
    while j <= math.sqrt(n):
        if n % j == 0:
            return False
        j += 1
    return True


def gcd(number1, number2):
    while number1 != number2:
        if number1 > number2:
            number1 = number1-number2
        else:
            number2 = number2 - number1
    return number1


def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1
