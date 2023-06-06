import unittest

from src.mutation import bit_flip_mutation, inversion_mutation, swap_mutation


class TestMutation(unittest.TestCase):
    def test_bit_flip_mutation_valid_case_returns_changed_chromosome(self):
        chromosome = [0, 0, 0, 0, 0]
        indices = [0, 2, 4]
        expected_chromosomes = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1]]
        for index, expected_chromosome in zip(indices, expected_chromosomes):
            with self.subTest(index=index, expected_chromosome=expected_chromosome):
                self.assertEqual(expected_chromosome, bit_flip_mutation(chromosome, index))

    def test_bit_flip_mutation_index_out_of_bounds_raises_value_error(self):
        chromosome = [0, 0, 0, 0, 0]
        bad_indices = [-101, -1, 5, 101]
        for index in bad_indices:
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    bit_flip_mutation(chromosome, index)

    def test_inversion_mutation_valid_case_returns_changed_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(0, 2), (0, 3), (1, 4), (0, 5)]
        expected_chromosomes = [
            [1, 0, 2, 3, 4],
            [2, 1, 0, 3, 4],
            [0, 3, 2, 1, 4],
            [4, 3, 2, 1, 0],
        ]
        for index, expected_chromosome in zip(indices, expected_chromosomes):
            with self.subTest(start=index[0], end=index[1], expected_chromosome=expected_chromosome):
                self.assertEqual(expected_chromosome, inversion_mutation(chromosome, index[0], index[1]))

    def test_inversion_mutation_same_indices_returns_unchanged_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(0, 0), (1, 1), (5, 5)]
        expected_chromosome = [0, 1, 2, 3, 4]
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(expected_chromosome, inversion_mutation(chromosome, index[0], index[1]))

    def test_inversion_mutation_adjacent_indices_returns_unchanged_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(0, 1), (1, 2), (4, 5)]
        expected_chromosome = [0, 1, 2, 3, 4]
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(expected_chromosome, inversion_mutation(chromosome, index[0], index[1]))

    def test_inversion_mutation_high_index_before_low_returns_unchanged_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(1, 0), (4, 2), (5, 0)]
        expected_chromosome = [0, 1, 2, 3, 4]
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(expected_chromosome, inversion_mutation(chromosome, index[0], index[1]))

    def test_inversion_mutation_indices_out_of_bounds_raises_value_error(self):
        chromosome = [0, 0, 0, 0, 0]
        bad_indices = [(-1, 3), (3, -101), (3, 6), (101, 3), (-1, -1), (6, 6)]
        for index in bad_indices:
            with self.subTest(start=index[0], end=index[1]):
                with self.assertRaises(ValueError):
                    inversion_mutation(chromosome, index[0], index[1])

    def test_swap_mutation_valid_case_returns_changed_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(0, 2), (0, 3), (1, 4), (2, 4)]
        expected_chromosomes = [[2, 1, 0, 3, 4], [3, 1, 2, 0, 4], [0, 4, 2, 3, 1], [0, 1, 4, 3, 2]]
        for index, expected_chromosome in zip(indices, expected_chromosomes):
            with self.subTest(start=index[0], end=index[1], expected_chromosome=expected_chromosome):
                self.assertEqual(expected_chromosome, swap_mutation(chromosome, index[0], index[1]))

    def test_swap_mutation_same_indices_returns_unchanged_chromosome(self):
        chromosome = [0, 1, 2, 3, 4]
        indices = [(0, 0), (1, 1), (4, 4)]
        expected_chromosome = [0, 1, 2, 3, 4]
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(expected_chromosome, swap_mutation(chromosome, index[0], index[1]))

    def test_swap_mutation_indices_out_of_bounds_raises_value_error(self):
        chromosome = [0, 0, 0, 0, 0]
        bad_indices = [(-1, 3), (3, -101), (3, 5), (101, 3), (-1, -1), (5, 5)]
        for index in bad_indices:
            with self.subTest(start=index[0], end=index[1]):
                with self.assertRaises(ValueError):
                    swap_mutation(chromosome, index[0], index[1])
