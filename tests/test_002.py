import unittest
from euler.solution_002 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 4613732)
