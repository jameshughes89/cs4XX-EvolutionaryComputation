import unittest

from src.mutation import bit_flip_mutation


class TestMutation(unittest.TestCase):
    def test_bit_flip_mutation_valid_case_returns_changed_chromosome(self):
        chromosome = [0, 0, 0, 0, 0]
        indices = [0, 2, 4]
        expected_chromosomes = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1]]
        for index, expected_chromosome in zip(indices, expected_chromosomes):
            with self.subTest(index=index, expected_chromosome=expected_chromosome):
                self.assertEqual(expected_chromosome, bit_flip_mutation(chromosome, index))

    def test_bit_flip_mutation_mutation_point_out_of_bounds_raises_value_error(self):
        chromosome = [0, 0, 0, 0, 0]
        bad_indices = [-101, -1, 5, 101]
        for index in bad_indices:
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    bit_flip_mutation(chromosome, index)
