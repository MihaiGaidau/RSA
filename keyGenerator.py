import random
import math


def checkIfPrime(n):
    j = 2
    while j <= math.sqrt(n):
        if n % j == 0:
            return False
        j += 1
        return True

print(checkIfPrime(23))