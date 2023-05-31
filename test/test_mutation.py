import unittest

from src.mutation import bit_flip_mutation


class TestMutation(unittest.TestCase):
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
