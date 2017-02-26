def collatz(n):
    sequence = [] 

    while True:
        sequence.append(int(n))

        if n == 1:
            return sequence

        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1

def answer(limit):
    best_candidate = (0, 0)
    for n in range(limit):
        length = len(collatz(n + 1))
        if length > best_candidate[1]:
            best_candidate = (n + 1, length)
    return best_candidate[0]

def solution():
    return answer(1000000)
