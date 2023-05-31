"""
A simple genetic algorithm for maximizing a bit string.

The integer is encoded as a bit string (list of 0s or 1s). Fitness is calculated with either the value of the bit string
or the number of 1s in the bit string (both are included for a comparison). Crossover is a single point crossover and
mutation is a bit flip mutation.
"""
from random import choices, random, randrange

from src.crossover import one_point_crossover
from src.mutation import bit_flip_mutation
from src.selection import tournament_selection

BIT_STRING_LENGTH = 16
POPULATION_SIZE = 10
GENERATIONS = 100
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10


def value_fitness(chromosome: list) -> int:
    """
    Calculate the decimal value of the chromosome (bit string).

    :param chromosome: Chromosome (bit string) to evaluate
    :return: The decimal value of the chromosome (bit string)
    """
    return int("".join(str(bit) for bit in chromosome), 2)


def ones_fitness(chromosome: list) -> int:
    """
    Count the number of 1s (ones) in the chromosome (bit string).

    :param chromosome: Chromosome (bit string) to evaluate
    :return: The number of 1s (ones) in the chromosome (bit string).
    """
    number_of_ones = 0
    for bit in chromosome:
        number_of_ones += bit
    return number_of_ones


def run_max_bitstring_ga():
    # Initialize
    population = []
    population_fitness = []
    for _ in range(POPULATION_SIZE):
        chromosome = choices([0, 1], k=BIT_STRING_LENGTH)
        population.append(chromosome)

    # Run for a Specified Number of Generations (Termination)
    for generation in range(GENERATIONS):
        # Evaluate
        population_fitness = []
        for chromosome in population:
            fitness = value_fitness(chromosome)
            population_fitness.append(fitness)

        # Selection
        mating_pool = []
        for _ in range(POPULATION_SIZE):
            tournament_indices = choices(range(POPULATION_SIZE))
            chromosome = tournament_selection(population, population_fitness, tournament_indices)
            mating_pool.append(chromosome)

        # Variation (Crossover)
        for i in range(0, POPULATION_SIZE, 2):
            if random() < CROSSOVER_RATE:
                crossover_point = randrange(BIT_STRING_LENGTH)
                chromosome_1, chromosome_2 = one_point_crossover(mating_pool[i], mating_pool[i + 1], crossover_point)
                mating_pool[i] = chromosome_1
                mating_pool[i + 1] = chromosome_2

        # Variation (Mutation)
        for i in range(POPULATION_SIZE):
            if random() < MUTATION_RATE:
                mutation_point = randrange(BIT_STRING_LENGTH)
                chromosome = bit_flip_mutation(mating_pool[i], mutation_point)
                mating_pool[i] = chromosome

        population = mating_pool

    print(population_fitness)
    print(population)


if __name__ == "__main__":
    run_max_bitstring_ga()
