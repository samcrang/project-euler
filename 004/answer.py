#!/usr/bin/env python3

import math

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def answer(base_10_digits):
    best_candidate = 0
    for i in reversed(range(int(math.pow(10, base_10_digits)))):
        for j in reversed(range(int(math.pow(10, base_10_digits)))):
            candidate = i * j
            if is_palindrome(candidate) and candidate > best_candidate:
                best_candidate = candidate

    return best_candidate

if __name__ == "__main__":
    print(answer(3))
