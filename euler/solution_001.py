def divides_evenly_by_3_or_5(number):
    return number % 3 == 0 or number % 5 == 0

def answer(upper_bound):
    acc = 0
    for x in range(1, upper_bound):
        if divides_evenly_by_3_or_5(x):
            acc = acc + x
    return acc

def solution():
    return answer(1000)
