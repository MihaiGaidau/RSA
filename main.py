from decrypt import *
from encrypt import *
from keyGenerator import *
import Key



random1 = generateRandomNumber(1000)
random2 = generateRandomNumber(1000)

prime1 = findNearPrime(random1)
prime2 = findNearPrime(random2)

# print("random:")
# print(random1,random2)
# print("primes: ")
# print(prime1, prime2)
privata, publica = generateKeys(prime1,prime2)
print(privata,publica)
print(ord('2'))
print(decrypt(encrypt("misa",privata),publica))
