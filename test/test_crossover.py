import unittest

from src.crossover import one_point_crossover, order_crossover


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

    def test_one_point_crossover_index_out_of_bounds_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        bad_indices = [-101, -1, 5, 101]
        for index in bad_indices:
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    one_point_crossover(chromosome_1, chromosome_2, index)

    def test_order_crossover_valid_case_returns_changed_chromosomes(self):
        chromosome_1 = [0, 1, 2, 3, 4, 5, 6, 7]
        chromosome_2 = [4, 6, 3, 5, 2, 0, 1, 7]
        indices = [(0, 1), (0, 3), (2, 6), (0, 7), (5, 8)]
        expected_chromosome_pairs = [
            ([0, 6, 3, 5, 2, 1, 7, 4], [4, 1, 2, 3, 5, 6, 7, 0]),
            ([0, 1, 2, 5, 7, 4, 6, 3], [4, 6, 3, 5, 7, 0, 1, 2]),
            ([6, 0, 2, 3, 4, 5, 1, 7], [1, 4, 3, 5, 2, 0, 6, 7]),
            ([0, 1, 2, 3, 4, 5, 6, 7], [4, 6, 3, 5, 2, 0, 1, 7]),
            ([4, 3, 2, 0, 1, 5, 6, 7], [2, 3, 4, 5, 6, 0, 1, 7]),
        ]
        for index, expected_chromosome_pair in zip(indices, expected_chromosome_pairs):
            with self.subTest(start=index[0], end=index[1], expected_chromosome_pair=expected_chromosome_pair):
                self.assertEqual(
                    expected_chromosome_pair, order_crossover(chromosome_1, chromosome_2, index[0], index[1])
                )

    def test_order_crossover_same_indices_returns_unchanged_chromosomes(self):
        chromosome_1 = [0, 1, 2, 3, 4, 5, 6, 7]
        chromosome_2 = [4, 6, 3, 5, 2, 0, 1, 7]
        indices = [(0, 0), (1, 1), (5, 5), (7, 7)]
        expected_chromosome_pair = ([0, 1, 2, 3, 4, 5, 6, 7], [4, 6, 3, 5, 2, 0, 1, 7])
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(
                    expected_chromosome_pair, order_crossover(chromosome_1, chromosome_2, index[0], index[1])
                )

    def test_order_crossover_high_index_before_low_returns_unchanged_chromosome(self):
        chromosome_1 = [0, 1, 2, 3, 4, 5, 6, 7]
        chromosome_2 = [4, 6, 3, 5, 2, 0, 1, 7]
        indices = [(1, 0), (4, 1), (7, 5)]
        expected_chromosome_pair = ([0, 1, 2, 3, 4, 5, 6, 7], [4, 6, 3, 5, 2, 0, 1, 7])
        for index in indices:
            with self.subTest(start=index[0], end=index[1]):
                self.assertEqual(
                    expected_chromosome_pair, order_crossover(chromosome_1, chromosome_2, index[0], index[1])
                )

    def test_order_crossover_indices_cover_full_chromosome_returns_unchanged_chromosome(self):
        chromosome_1 = [0, 1, 2, 3, 4, 5, 6, 7]
        chromosome_2 = [4, 6, 3, 5, 2, 0, 1, 7]
        expected_chromosome_pair = ([0, 1, 2, 3, 4, 5, 6, 7], [4, 6, 3, 5, 2, 0, 1, 7])
        self.assertEqual(expected_chromosome_pair, order_crossover(chromosome_1, chromosome_2, 0, 8))

    def test_order_crossover_unequal_chromosomes_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1]
        with self.assertRaises(ValueError):
            order_crossover(chromosome_1, chromosome_2, 0, 1)

    def test_order_crossover_index_out_of_bounds_raises_value_error(self):
        chromosome_1 = [0, 0, 0, 0, 0]
        chromosome_2 = [1, 1, 1, 1, 1]
        bad_indices = [(-1, 3), (3, -101), (3, 6), (101, 3), (-1, -1), (6, 5), (6, 6)]
        for index in bad_indices:
            with self.subTest(index=index):
                with self.assertRaises(ValueError):
                    order_crossover(chromosome_1, chromosome_2, index[0], index[1])
