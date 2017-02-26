"""
https://en.wikipedia.org/wiki/Square_pyramidal_number

n(n + 1)(2n + 1) /6
"""
def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) / 6

"""
https://en.wikipedia.org/wiki/Triangular_number
"""
def sum(n):
    return n * (n + 1) / 2

def answer(n):
    return int(sum(n)**2 - sum_of_squares(n))

def solution():
    return answer(100)
