from .helpers.prime_sieve import prime_sieve

def answer(number):
    return sum(prime_sieve(number))

def solution():
    return answer(2000000)
