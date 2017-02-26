import unittest
from euler.solution_001 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 233168)

    def test_example(self):
        self.assertEqual(answer(10), 23)
