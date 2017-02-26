from .helpers.prime_sieve import prime_sieve

primes = prime_sieve(900000)

def answer(position):
    return primes[position - 1]

def solution():
    return answer(10001)
