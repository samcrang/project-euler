#!/usr/bin/env python3

from collections import Counter
from functools import reduce
from ..helpers.prime_sieve import prime_sieve

primes = prime_sieve(9000)

"""
https://en.wikipedia.org/wiki/Trial_division
"""
def trial_division(n):
    if n < 2:
        return []
    prime_factors = []
    for p in primes:
        if p*p > n: break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors

"""
http://mathschallenge.net/library/number/number_of_divisors
"""
def count_divisors(n):
    c = Counter(trial_division(n))
    return reduce(lambda x, y: x*(y[1]+1), c.items(), 1)

def triangle_numbers():
    pos = 1
    i = 2
    while True:
        yield pos
        pos += i
        i += 1

def solution():
    for candidate in triangle_numbers():
        divisors = count_divisors(candidate)
        if divisors > 500:
            return candidate
        candidate += 1

if __name__ == "__main__":
    print(solution())
