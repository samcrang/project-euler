import unittest
from euler.solution_003 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 6857)

    def test_example(self):
        self.assertEqual(answer(13195), 29)
