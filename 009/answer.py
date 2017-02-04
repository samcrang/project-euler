#!/usr/bin/env python3

"""
https://en.wikipedia.org/wiki/Coprime_integers#Generating_all_coprime_pairs
"""
def non_odd_odd_coprimes():
    return coprimes(2, 1)

def coprimes(m, n):
    queue = []
    queue.append((m,n))

    while True:
        node = queue.pop(0)
        m = node[0]
        n = node[1]
        branch_1 = (2 * m - n, m)
        branch_2 = (2 * m + n, m)
        branch_3 = (m + 2 * n, n)
        yield branch_1
        yield branch_2
        yield branch_3
        queue.append(branch_1)
        queue.append(branch_2)
        queue.append(branch_3)

"""
https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
"""
def primitive_triples():
    for m, n in non_odd_odd_coprimes():
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2
        yield (a, b, c)

def answer(n):
    for x in primitive_triples():
        summation = sum(x)
        if n % summation == 0:
            k = int(n / summation)
            a = (x[0] * k, x[1] * k, x[2] * k)
            return a[0] * a[1] * a[2]

if __name__ == "__main__":
    print(answer(1000))
