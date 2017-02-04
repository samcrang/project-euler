import math

"""
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
def prime_sieve(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False

    i = 2
    while i < math.sqrt(size):
        if sieve[i]:
            j = int(math.pow(i, 2))
            k = 0
            while j < size:
                sieve[j] = False
                j = int(math.pow(i, 2)) + k * i
                k += 1
        i = i + 1

    primes = []
    for x in enumerate(sieve):
        if x[1] == True:
            primes.append(x[0])

    return primes
