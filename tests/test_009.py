import unittest
from euler.solution_009 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 31875000)
