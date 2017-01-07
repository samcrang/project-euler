#!/usr/bin/env python3

def fib():
    a, b = 1, 2

    while True:
        yield a
        a, b = b, a + b

def is_even(number):
    return number % 2 == 0

def answer(upper_bound):
    acc = 0
    for x in fib():
        if x < upper_bound:
            if is_even(x):
                acc = acc + x
        else:
            return acc

if __name__ == "__main__":
    print(answer(4000000))