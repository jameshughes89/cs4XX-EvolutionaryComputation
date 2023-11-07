import unittest
import numpy as np
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
        result = value_fitness([3, 4])
        self.assertEqual(result, 3 ** 2 + 4 ** 2)
        result = value_fitness([0, 0])
        self.assertEqual(result, 0)

    def test_value_fitness_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            value_fitness([3])
        self.assertEqual(str(context.exception), "The length of individual is incorrect!")
        with self.assertRaises(ValueError) as context:
            value_fitness([3, 4, 5])
        self.assertEqual(str(context.exception), "The length of individual is incorrect!")

    def test_initialize_belief_space_returns_correct_value(self):
        belief_space = initialize_belief_space()
        assert belief_space["situational"] is None
        assert len(belief_space["normative"]) == 2
        for normative_values in belief_space["normative"]:
            assert len(normative_values) == 4
            assert -10 <= normative_values[0] <= 10
            assert -10 <= normative_values[1] <= 10
            assert normative_values[2] == 100
            assert normative_values[3] == 100

    def test_accept_returns_correct_value(self):
        population = [[1, 2], [3, 4], [5, 6], [7, 8]]
        population_fitness = [5, 25, 61, 113]
        result = accept(population, population_fitness)
        self.assertEqual(result, [[1, 2], [3, 4]])

    def test_update_returns_correct_value(self):
        belief_space = {
            "situational": None,
            "normative": [[-10, 10, 100, 100], [-10, 10, 100, 100]]
        }
        n_accepted = [[6, 5], [7, 8]]
        belief_space = update(belief_space, n_accepted)
        self.assertEqual(belief_space["situational"], [6, 5])
        self.assertEqual(belief_space["normative"][0], [6, 7, 61, 113])
        self.assertEqual(belief_space["normative"][1], [5, 8, 61, 113])

    @patch('numpy.random.normal')
    def test_influence_method_1_returns_correct_value(self, mock_random_normal):
        mock_random_normal.return_value = 0.5
        population = [[7, 8], [6, 5], [8, 8]]
        belief_space = {
            "situational": [6, 5],
            "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
        }
        influenced_population = influence_method_1(population, belief_space)
        expected_influenced_population = [[7.5, 9.5], [6.5, 6.5], [8.5, 9.5]]
        self.assertEqual(influenced_population, expected_influenced_population)

    @patch('numpy.random.normal')
    @patch('random.uniform')
    def test_influence_method_2_returns_correct_value(self, mock_random_normal, mock_random_uniform):
        mock_random_normal.return_value = 0.5
        mock_random_uniform.return_value = 0.5
        population = [[7, 8], [6, 5], [8, 8]]
        belief_space = {
            "situational": [6, 5],
            "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
        }
        influenced_population = influence_method_2(population, belief_space)
        expected_influenced_population = [[6.75, 7.75], [6.25, 5.25], [7.75, 7.75]]
        self.assertEqual(influenced_population, expected_influenced_population)

    @patch('numpy.random.normal')
    def test_influence_method_3_returns_correct_value(self, mock_random_normal):
        mock_random_normal.return_value = 0.5
        population = [[7, 8], [6, 5], [8, 8]]
        belief_space = {
            "situational": [6, 5],
            "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
        }
        influenced_population = influence_method_3(population, belief_space)
        expected_influenced_population = [[6.5, 6.5], [6.5, 6.5], [7.5, 6.5]]
        self.assertEqual(influenced_population, expected_influenced_population)

    @patch('numpy.random.normal')
    def test_influence_method_4_returns_correct_value(self, mock_random_normal):
        mock_random_normal.return_value = 0.5
        population = [[7, 8], [6, 5], [8, 8]]
        belief_space = {
            "situational": [6, 5],
            "normative": [[6, 7, 61, 113], [5, 8, 61, 113]]
        }
        influenced_population = influence_method_4(population, belief_space)
        expected_influenced_population = [[7.5, 9.5], [6.5, 6.5], [7.5, 9.5]]
        self.assertEqual(influenced_population, expected_influenced_population)


if __name__ == '__main__':
    unittest.main()
