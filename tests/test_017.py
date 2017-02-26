import unittest
from euler.solution_017 import solution

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 21124)
