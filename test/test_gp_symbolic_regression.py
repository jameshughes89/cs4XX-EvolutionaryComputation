import unittest

from src.gp_symbolic_regression import protected_divide


class TestGPSymbolicRegression(unittest.TestCase):
    def test_protected_divide_non_zero_divisor_returns_correct_quotient(self):
        valid_arguments = [
            (0, 1),
            (1, 1),
            (1, 2),
            (100, 50),
            (2, 4),
            (97, 1),
            (97, 10),
            (1, 0.0000001),
            (1.234, 5.678),
        ]
        expecteds = [0, 1, 0.5, 2, 0.5, 97, 9.7, 10000000, 0.21733004579]
        for valid_argument, expected in zip(valid_arguments, expecteds):
            with self.subTest(valid_argument=valid_argument, expected=expected):
                dividend, divisor = valid_argument
                self.assertAlmostEqual(expected, protected_divide(dividend, divisor))

    def test_protected_divide_zero_divisor_returns_999999999(self):
        dividends = [0, 1, 2, 3, 4, 10, 100]
        expected = 999_999_999
        for dividend in dividends:
            with self.subTest(dividend=dividend):
                self.assertEqual(expected, protected_divide(dividend, 0))