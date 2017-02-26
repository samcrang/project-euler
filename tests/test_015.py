import unittest
from euler.solution_015 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 137846528820)

    def test_example(self):
        self.assertEqual(answer(2, 2), 6)
