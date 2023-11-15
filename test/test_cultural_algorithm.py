import unittest
from unittest.mock import patch

from src.cultural_algorithm import (
    value_fitness,
    initialize_belief_space,
    accept,
    update,
    influence_method_1,
    influence_method_2,
    influence_method_3,
    influence_method_4,
)


class TestCulturalAlgorithm(unittest.TestCase):

    def test_value_fitness_returns_correct_value(self):
        test_cases = [
            ([3, 4], 3 ** 2 + 4 ** 2),
            ([0, 0], 0),
        ]
        for input_values, expected_result in test_cases:
            with self.subTest(input_values=input_values):
                result = value_fitness(input_values)
                self.assertEqual(result, expected_result)

    def test_value_fitness_raises_value_error(self):
        test_cases = [[3], [3, 4, 5]]
        for input_values in test_cases:
            with self.subTest(input_values=input_values):
                with self.assertRaises(ValueError):
                    value_fitness(input_values)

    def test_initialize_belief_space_situational_returns_correct_value(self):
        belief_space = initialize_belief_space()
        self.assertIsNone(belief_space["situational"])

    def test_initialize_belief_space_normative_returns_correct_value(self):
        belief_space = initialize_belief_space()
        for normative_values in belief_space["normative"]:
            self.assertEqual(normative_values, [-10, 10, 100, 100])

    def test_accept_returns_correct_value(self):
        population = [[1, 2], [3, 4], [5, 6], [7, 8]]
        population_fitness = [5, 25, 61, 113]
        result = accept(population, population_fitness)
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_update_situational_returns_correct_value(self):
        belief_space = {
            "situational": None,
            "normative": [[-10, 10, 100, 100], [-10, 10, 100, 100]]
        }
        n_accepted = [[6, 5], [7, 8]]
        belief_space = update(belief_space, n_accepted)
        self.assertEqual(belief_space["situational"], [6, 5])

    def test_update_normative_returns_correct_value(self):
        belief_space = {
            "situational": None,
            "normative": [[-10, 10, 100, 100], [-10, 10, 100, 100]]
        }
        n_accepted = [[6, 5], [7, 8]]
        belief_space = update(belief_space, n_accepted)
        self.assertEqual(belief_space["normative"][0], [6, 7, 61, 113])
        self.assertEqual(belief_space["normative"][1], [5, 8, 61, 113])

    @patch('numpy.random.normal')
    def test_influence_method_1_returns_correct_value(self, mock_random_normal):
        test_cases = [
            {
                "population": [[7, 8], [6, 5], [8, 8]],
                "belief_space": {
                    "situational": [6, 5],
                    "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
                },
                "expected_result": [[7.5, 9.5], [6.5, 6.5], [8.5, 9.5]]
            },
            {
                "population": [[-9, -6], [1, -2], [6, 1]],
                "belief_space": {
                    "situational": [1, -2],
                    "normative": [[1, 6, 5, 37], [-2, 1, 5, 37]]
                },
                "expected_result": [[-6.5, -4.5], [3.5, -0.5], [8.5, 2.5]]
            }
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                mock_random_normal.return_value = 0.5
                influenced_population = influence_method_1(test_case["population"], test_case["belief_space"])
                self.assertListEqual(influenced_population, test_case["expected_result"])

    @patch('numpy.random.normal')
    @patch('random.uniform')
    def test_influence_method_2_returns_correct_value(self, mock_random_normal, mock_random_uniform):
        test_cases = [
            {
                "population": [[7, 8], [6, 5], [8, 8]],
                "belief_space": {
                    "situational": [6, 5],
                    "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
                },
                "expected_result": [[6.75, 7.75], [6.25, 5.25], [7.75, 7.75]]
            },
            {
                "population": [[4, 6], [7, 0], [8, -1]],
                "belief_space": {
                    "situational": [7, 0],
                    "normative": [[4, 7, 52, 49], [0, 6, 49, 52]]
                },
                "expected_result": [[4.25, 5.75], [7.25, 0.25], [7.75, -0.75]]
            }
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                mock_random_normal.return_value = 0.5
                mock_random_uniform.return_value = 0.5
                influenced_population = influence_method_2(test_case["population"], test_case["belief_space"])
                self.assertListEqual(influenced_population, test_case["expected_result"])

    @patch('numpy.random.normal')
    def test_influence_method_3_returns_correct_value(self, mock_random_normal):
        test_cases = [
            {
                "population": [[7, 8], [6, 5], [8, 8]],
                "belief_space": {
                    "situational": [6, 5],
                    "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
                },
                "expected_result": [[6.5, 6.5], [6.5, 6.5], [7.5, 6.5]]
            },
            {
                "population": [[4, 6], [7, 0], [8, -1]],
                "belief_space": {
                    "situational": [7, 0],
                    "normative": [[4, 7, 52, 49], [0, 6, 49, 52]]
                },
                "expected_result": [[5.5, 3], [8.5, 3], [6.5, 2]]
            }
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                mock_random_normal.return_value = 0.5
                influenced_population = influence_method_3(test_case["population"], test_case["belief_space"])
                self.assertListEqual(influenced_population, test_case["expected_result"])

    @patch('numpy.random.normal')
    def test_influence_method_4_returns_correct_value(self, mock_random_normal):
        test_cases = [
            {
                "population": [[7, 8], [6, 5], [8, 8]],
                "belief_space": {
                    "situational": [6, 5],
                    "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
                },
                "expected_result": [[7.5, 9.5], [6.5, 6.5], [7.5, 9.5]]
            },
            {
                "population": [[4, 6], [7, 0], [8, -1]],
                "belief_space": {
                    "situational": [7, 0],
                    "normative": [[4, 7, 52, 49], [0, 6, 49, 52]]
                },
                "expected_result": [[5.5, 9], [8.5, 3], [6.5, 2]]
            }
        ]
        for test_case in test_cases:
            with self.subTest(test_case=test_case):
                mock_random_normal.return_value = 0.5
                influenced_population = influence_method_4(test_case["population"], test_case["belief_space"])
                self.assertListEqual(influenced_population, test_case["expected_result"])