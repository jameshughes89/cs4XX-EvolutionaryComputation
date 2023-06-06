import unittest

from src.crossover import one_point_crossover


class TestCrossover(unittest.TestCase):
    def test_one_point_crossover_valid_case_returns_changed_chromosomes(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        indices = [0, 2, 4]
        expected_chromosome_pairs = [
            ([1, 1, 1, 1, 1], [0, 0, 0, 0, 0]),
            ([0, 0, 1, 1, 1], [1, 1, 0, 0, 0]),
            ([0, 0, 0, 0, 1], [1, 1, 1, 1, 0]),
        ]
        for index, expected_chromosome_pair in zip(indices, expected_chromosome_pairs):
            with self.subTest(index=index, expected_chromosome_pair=expected_chromosome_pair):
                self.assertEqual(expected_chromosome_pair, one_point_crossover(chromosome_1, chromosome_2, index))

    def test_one_point_crossover_unequal_chromosomes_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1]
        index = 0
        with self.assertRaises(ValueError):
            one_point_crossover(chromosome_1, chromosome_2, index)

    def test_one_point_crossover_crossover_point_out_of_bounds_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        bad_indices = [-101, -1, 5, 101]
        for index in bad_indices:
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    one_point_crossover(chromosome_1, chromosome_2, index)
