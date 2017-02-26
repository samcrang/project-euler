import unittest
from euler.solution_004 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 906609)

    def test_example(self):
        self.assertEqual(answer(2), 9009)
