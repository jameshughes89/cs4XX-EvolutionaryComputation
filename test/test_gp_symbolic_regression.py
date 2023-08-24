import math
import operator
import unittest
from unittest.mock import patch

from src.gp_symbolic_regression import (
    mean_squared_error,
    mean_squared_error_fitness,
    protected_divide,
)


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
                self.assertAlmostEqual(expected, protected_divide(*valid_argument))

    def test_protected_divide_zero_divisor_returns_infinity(self):
        dividends = [0, 1, 2, 3, 4, 10, 100]
        expected = math.inf
        for dividend in dividends:
            with self.subTest(dividend=dividend):
                self.assertEqual(expected, protected_divide(dividend, 0))

    def test_mean_squared_error_returns_correct_value(self):
        independent_variables = [[0, 0], [1, 1], [2, 1], [2, 2], [3, 3], [10, 1], [10, 10], [-1, 1], [-2, -2]]
        dependent_variable = [0, 2, 3, 4, 6, 11, 20, 0, -4]
        functions = [operator.add, operator.sub, operator.mul]
        expecteds = [0, 484 / 9, 2159 / 3]
        for func, expected in zip(functions, expecteds):
            with self.subTest(func=func, expected=expected):
                self.assertAlmostEqual(expected, mean_squared_error(func, independent_variables, dependent_variable))

    @patch("deap.base.Toolbox")
    def test_mean_squared_error_fitness_returns_correct_value(self, mocked_toolbox):
        independent_variables = [[0, 0], [1, 1], [2, 1], [2, 2], [3, 3], [10, 1], [10, 10], [-1, 1], [-2, -2]]
        dependent_variable = [0, 2, 3, 4, 6, 11, 20, 0, -4]
        functions = [operator.add, operator.sub, operator.mul]
        expecteds = [(0,), (484 / 9,), (2159 / 3,)]
        for func, expected in zip(functions, expecteds):
            with self.subTest(func=func, expected=expected):
                mocked_toolbox.compile.return_value = func
                self.assertAlmostEqual(
                    expected,
                    mean_squared_error_fitness(None, mocked_toolbox, independent_variables, dependent_variable),
                )

    def test_mean_squared_error_fitness_zero_length_variables_raises_value_error(self):
        independent_variables_set = [[], [[]], []]
        dependent_variable_set = [[[]], [], []]
        for independent_variables, dependent_variable in zip(independent_variables_set, dependent_variable_set):
            with self.subTest(independent_variables=independent_variables, dependent_variable=dependent_variable):
                with self.assertRaises(ValueError):
                    mean_squared_error_fitness(None, None, independent_variables, dependent_variable)

    def test_mean_squared_error_fitness_uneven_length_variables_raises_value_error(self):
        independent_variables = [[], [], []]
        dependent_variable = [0, 0, 0, 0]
        with self.assertRaises(ValueError):
            mean_squared_error_fitness(None, None, independent_variables, dependent_variable)
