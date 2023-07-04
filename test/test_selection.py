import unittest

from src.selection import roulette_wheel_selection, tournament_selection


class TestSelection(unittest.TestCase):
    def test_roulette_wheel_selection_valid_case_returns_correct_chromosome(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 1, 2, 3, 4]
        valid_pill_landings = [0, 0.09, 0.1, 0.29, 0.3, 0.59, 0.6, 0.99]
        expecteds = [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [3, 3, 3, 3, 3],
            [3, 3, 3, 3, 3],
            [4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4],
        ]
        for pill_landing, expected in zip(valid_pill_landings, expecteds):
            with self.subTest(pill_landing=pill_landing, expected=expected):
                self.assertEqual(expected, roulette_wheel_selection(population, population_fitness, pill_landing))

    def test_roulette_wheel_selection_pill_landing_not_between_0_and_1_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [1, 1, 1, 1, 1]
        bad_pill_landings = [-101, -0.01, 1, 101]
        for pill_landing in bad_pill_landings:
            with self.subTest(selected_indices=pill_landing):
                with self.assertRaises(ValueError):
                    roulette_wheel_selection(population, population_fitness, pill_landing)

    def test_roulette_wheel_selection_population_fitness_total_is_zero_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        pill_landing = 0.5
        with self.assertRaises(ValueError):
            roulette_wheel_selection(population, population_fitness, pill_landing)

    def test_tournament_selection_valid_maximizing_case_returns_correct_chromosome(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 1, 2, 3, 4]
        valid_selected_indices = [[0], [2], [0, 2], [0, 2, 4], [0, 1, 2, 3, 4], [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]]
        expecteds = [
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2],
            [2, 2, 2, 2, 2],
            [4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4],
            [4, 4, 4, 4, 4],
        ]
        for selected_indices, expected in zip(valid_selected_indices, expecteds):
            with self.subTest(selected_indices=selected_indices, expected=expected):
                self.assertEqual(expected, tournament_selection(population, population_fitness, selected_indices))

    def test_tournament_selection_valid_minimizing_case_returns_correct_chromosome(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 1, 2, 3, 4]
        valid_selected_indices = [[0], [2], [0, 2], [2, 3, 4], [0, 1, 2, 3, 4], [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]]
        expecteds = [
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0],
            [2, 2, 2, 2, 2],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        for selected_indices, expected in zip(valid_selected_indices, expecteds):
            with self.subTest(selected_indices=selected_indices, expected=expected):
                self.assertEqual(expected, tournament_selection(population, population_fitness, selected_indices, -1))

    def test_tournament_selection_empty_selected_indices_when_maximizing_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        selected_indices = []
        with self.assertRaises(ValueError):
            tournament_selection(population, population_fitness, selected_indices)

    def test_tournament_selection_empty_selected_indices_when_minimising_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        selected_indices = []
        with self.assertRaises(ValueError):
            tournament_selection(population, population_fitness, selected_indices, -1)

    def test_tournament_selection_out_of_bounds_indices_when_maximising_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        bad_selected_indices = [[-1], [5], [0, 1, 2, -1], [4, 3, 2, 5]]
        for selected_indices in bad_selected_indices:
            with self.subTest(selected_indices=selected_indices):
                with self.assertRaises(ValueError):
                    tournament_selection(population, population_fitness, selected_indices)

    def test_tournament_selection_out_of_bounds_indices_when_minimizing_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        bad_selected_indices = [[-1], [5], [0, 1, 2, -1], [4, 3, 2, 5]]
        for selected_indices in bad_selected_indices:
            with self.subTest(selected_indices=selected_indices):
                with self.assertRaises(ValueError):
                    tournament_selection(population, population_fitness, selected_indices, -1)
