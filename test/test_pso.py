import unittest

from src.pso import matyas_function


class TestGAMaxBitstring(unittest.TestCase):
    def test_matyas_function_returns_correct_value(self):
        vectors = [(0, 0), (1, 1), (1, 2), (-5, 5), (10, 10), (-100, 100)]
        expecteds = [0, 0.04, 0.34, 25, 4, 10000]
        for vector, expected in zip(vectors, expecteds):
            with self.subTest(vector=vector, expected=expected):
                self.assertAlmostEqual(expected, matyas_function(vector[0], vector[1]))
