import unittest
from euler.solution_006 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 25164150)

    def test_example(self):
        self.assertEqual(answer(10), 2640)
