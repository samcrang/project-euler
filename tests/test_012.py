import unittest
from euler.solution_012 import solution

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 76576500)
