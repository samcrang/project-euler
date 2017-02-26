import math
from .helpers.prime_sieve import prime_sieve

def answer(number):
    primes = prime_sieve(int(math.sqrt(number)))

    for x in reversed(primes):
        if number % x == 0:
            return x

def solution():
    return answer(600851475143)
