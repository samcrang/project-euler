import unittest
from euler.solution_007 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 104743)

    def test_example(self):
        self.assertEqual(answer(6), 13)
