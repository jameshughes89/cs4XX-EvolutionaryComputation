import unittest

from src.ga_max_bitstring import ones_fitness, value_fitness


class TestGAMaxBitstring(unittest.TestCase):
    def test_value_fitness_various_cases_returns_correct_fitness(self):
        chromosomes = [[0], [1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        expecteds = [0, 1, 10, 5, 1023]
        for chromosome, expected in zip(chromosomes, expecteds):
            with self.subTest(chromosome=chromosome, expected=expected):
                self.assertEqual(expected, value_fitness(chromosome))

    def test_value_fitness_empty_chromosome_raises_value_error(self):
        chromosome = []
        with self.assertRaises(ValueError):
            value_fitness(chromosome)

    def test_ones_fitness_various_cases_returns_correct_fitness(self):
        chromosomes = [[0], [1], [1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        expecteds = [0, 1, 2, 2, 10]
        for chromosome, expected in zip(chromosomes, expecteds):
            with self.subTest(chromosome=chromosome, expected=expected):
                self.assertEqual(expected, ones_fitness(chromosome))

    def test_ones_fitness_empty_chromosome_raises_value_error(self):
        chromosome = []
        with self.assertRaises(ValueError):
            ones_fitness(chromosome)
