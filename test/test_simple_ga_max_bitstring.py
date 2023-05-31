import unittest

from src.simple_ga_max_bitstring import ones_fitness, value_fitness


class TestSimpleGAMaxNumber(unittest.TestCase):
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
