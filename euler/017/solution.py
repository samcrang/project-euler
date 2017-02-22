#!/usr/bin/env python3

from functools import reduce

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def in_words(n):
    result = ""

    if n == 1000:
       return "one thousand"

    if n >= 100:
        result += digits[n // 100 - 1] + " hundred"
        n %= 100 
        
        if n > 0:
            result += " and "

    if n >= 20:
        result += tens[n // 10 - 2]
        n %= 10
        if n > 0:
            result += "-"

    if n > 0:
        result += digits[n - 1]

    return result

def solution():
    return len(reduce(lambda x, y: x + in_words(y), range(1, 1001), "").replace(" ", "").replace("-", ""))

if __name__ == "__main__":
    print(solution())
