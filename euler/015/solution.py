import math

"""
We can write a path through our lattice using "N" or "E". The number of Ns is the height of the lattice, the number of Es is the width of the lattice. Every path through the same lattice has exactly the same number of Es and Ns. We can just find the number of anagrams in order to find the number of paths.

https://en.wikipedia.org/wiki/Lattice_path#North-East_lattice_paths
https://en.wikipedia.org/wiki/Permutation#Permutations_of_multisets
"""

def answer(width, height):
    return int(math.factorial(width + height)/(math.factorial(width) * math.factorial(height)))

def solution():
    return answer(20, 20)
