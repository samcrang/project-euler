import unittest
from euler.solution_008 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 23514624000)

    def test_example(self):
        self.assertEqual(answer(4), 5832)
