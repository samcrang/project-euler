def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):
    return int(a * b / gcd(a, b))

def answer(upper_bound):
    result = 1
    for i in range(1, upper_bound + 1):
        result = lcm(result, i)

    return result

def solution():
    return answer(20)
