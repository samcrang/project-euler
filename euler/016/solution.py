from functools import reduce

def answer(exponent):
    return reduce(lambda x, y: x + int(y), str(2**exponent), 0)

def solution():
    return answer(1000)
