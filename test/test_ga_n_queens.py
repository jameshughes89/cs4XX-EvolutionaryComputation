import unittest

from src.ga_n_queens import attacking_fitness


class TestGAMaxBitstring(unittest.TestCase):
    def test_attacking_fitness_various_cases_returns_correct_fitness(self):
        chromosomes = [
            [0],
            [0, 1],
            [1, 0],
            [0, 2, 1],
            [0, 1, 2],
            [1, 3, 0, 2],
            [0, 1, 2, 3, 4],
            [4, 2, 0, 3, 1],
            [3, 5, 7, 1, 6, 0, 2, 4],
            [3, 0, 4, 5, 1, 6, 2, 7],
            [1, 3, 5, 2, 6, 4, 7, 8],
            [7, 6, 5, 4, 3, 2, 1, 0],
        ]
        expecteds = [0, 1, 1, 1, 3, 0, 10, 0, 0, 2, 5, 28]
        for chromosome, expected in zip(chromosomes, expecteds):
            with self.subTest(chromosome=chromosome, expected=expected):
                self.assertEqual(expected, attacking_fitness(chromosome))
