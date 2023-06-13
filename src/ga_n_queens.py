"""
A genetic algorithm for n queens.

The queen placements is encoded as a permutation of length n containing integers 0 -- 7 inclusively. This encoding
ensures that no two queens are in the same row or column, thus the only potential for attacking is diagonal. Fitness
is calculated as the number of attacking queens (each pair of attacking queens is counted only once). Crossover is a
permutation safe order crossover and mutation is a permutation safe swap mutation.
"""
from random import choices, random, randrange

from src.crossover import order_crossover
from src.mutation import swap_mutation
from src.selection import tournament_selection

N_QUEENS = 8
POPULATION_SIZE = 10
GENERATIONS = 100
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10