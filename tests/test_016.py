import unittest
from euler.solution_016 import solution

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 1366)
