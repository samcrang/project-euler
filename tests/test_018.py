import unittest
from euler.solution_018 import solution, answer

class TestCase(unittest.TestCase):
    def test_example(self):
        example = [\
            [3], \
            [7, 4], \
            [2, 4, 6], \
            [8, 5, 9, 3], \
        ]

        self.assertEqual(answer(example), 23)

    def test_solution(self):
        self.assertEqual(solution(), 1074)
