import unittest

from src.simple_ga_max_bitstring import (
    bit_flip_mutation,
    one_point_crossover,
    ones_fitness,
    tournament_selection,
    value_fitness,
)


class TestSimpleGAMaxNumber(unittest.TestCase):
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

    def test_one_point_crossover_valid_case_returns_changed_chromosomes(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        crossover_points = [0, 2, 4]
        expected_chromosome_pairs = [
            ([1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
            ([0, 0, 1, 1, 1], [1, 1, 0, 0, 0]),
            ([0, 0, 0, 0, 1], [1, 1, 1, 1, 0]),
        ]
        for crossover_point, expected_chromosome_pair in zip(crossover_points, expected_chromosome_pairs):
            with self.subTest(crossover_point=crossover_point, expected_chromosome_pair=expected_chromosome_pair):
                self.assertEqual(
                    expected_chromosome_pair, one_point_crossover(chromosome_1, chromosome_2, crossover_point)
                )

    def test_one_point_crossover_unequal_chromosomes_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1]
        crossover_point = 0
        with self.assertRaises(ValueError):
            one_point_crossover(chromosome_1, chromosome_2, crossover_point)

    def test_one_point_crossover_crossover_point_out_of_bounds_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        bad_crossover_points = [-101, -1, 5, 101]
        for crossover_point in bad_crossover_points:
            with self.subTest(crossover_point=crossover_point):
                with self.assertRaises(ValueError):
                    one_point_crossover(chromosome_1, chromosome_2, crossover_point)

    def test_bit_flip_mutation_valid_case_returns_changed_chromosome(self):
        chromosome = [0, 0, 0, 0, 0]
        mutation_points = [0, 2, 4]
        expected_chromosomes = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1]]
        for mutation_point, expected_chromosome in zip(mutation_points, expected_chromosomes):
            with self.subTest(mutation_point=mutation_point, expected_chromosome=expected_chromosome):
                self.assertEqual(expected_chromosome, bit_flip_mutation(chromosome, mutation_point))

    def test_bit_flip_mutation_mutation_point_out_of_bounds_raises_value_error(self):
        chromosome = [0, 0, 0, 0, 0]
        bad_mutation_points = [-101, -1, 5, 101]
        for mutation_point in bad_mutation_points:
            with self.subTest(mutation_point=mutation_point):
                with self.assertRaises(ValueError):
                    bit_flip_mutation(chromosome, mutation_point)

    def test_value_fitness_various_cases_returns_correct_fitness(self):
        chromosomes = [[0], [1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        expecteds = [0, 1, 10, 5, 1023]
        for chromosome, expected in zip(chromosomes, expecteds):
            with self.subTest(chromosome=chromosome, expected=expected):
                self.assertEqual(expected, value_fitness(chromosome))

    def test_ones_fitness_various_cases_returns_correct_fitness(self):
        chromosomes = [[0], [1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        expecteds = [0, 1, 2, 2, 10]
        for chromosome, expected in zip(chromosomes, expecteds):
            with self.subTest(chromosome=chromosome, expected=expected):
                self.assertEqual(expected, ones_fitness(chromosome))
