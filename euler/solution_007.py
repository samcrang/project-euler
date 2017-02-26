from .helpers.prime_sieve import prime_sieve

def solution():
    primes = prime_sieve(900000)
    return primes[10000]
