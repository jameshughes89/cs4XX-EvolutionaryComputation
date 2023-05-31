import unittest

from src.selection import tournament_selection


class TestSelection(unittest.TestCase):
    def test_tournament_selection_valid_case_returns_correct_chromosome(self):
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
        for selected_indices, expecteds in zip(valid_selected_indices, expecteds):
            with self.subTest(selected_indices=selected_indices, expecteds=expecteds):
                self.assertEqual(expecteds, tournament_selection(population, population_fitness, selected_indices))

    def test_tournament_selection_empty_selected_indices_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        selected_indices = []
        with self.assertRaises(ValueError):
            tournament_selection(population, population_fitness, selected_indices)

    def test_tournament_selection_out_of_bounds_indices_raises_value_error(self):
        population = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
        population_fitness = [0, 0, 0, 0, 0]
        bad_selected_indices = [[-1], [5], [0, 1, 2, -1], [4, 3, 2, 5]]
        for selected_indices in bad_selected_indices:
            with self.subTest(selected_indices=selected_indices):
                with self.assertRaises(ValueError):
                    tournament_selection(population, population_fitness, selected_indices)
