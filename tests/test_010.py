import unittest
from euler.solution_010 import solution, answer

class TestCase(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(solution(), 142913828922)

    def test_example(self):
        self.assertEqual(answer(10), 17)
