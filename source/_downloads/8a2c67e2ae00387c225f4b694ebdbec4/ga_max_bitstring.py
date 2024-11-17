"""
A genetic algorithm for maximizing a bitstring.

The integer is encoded as a bitstring (list of 0s or 1s). Fitness is calculated with either the value of the bitstring
or the number of 1s in the bitstring (both are included for a comparison). Crossover is a single point crossover and
mutation is a bit flip mutation.
"""
from random import choices, random, randrange

import matplotlib.pyplot as plt

from src.crossover import one_point_crossover
from src.mutation import bit_flip_mutation
from src.selection import tournament_selection

# [begin-hyperparameters]
BIT_STRING_LENGTH = 10
POPULATION_SIZE = 10  # Must be multiple of two
TOURNAMENT_SIZE = 2
GENERATIONS = 25
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10
# [end-hyperparameters]


def value_fitness(chromosome: list) -> int:
    """
    Calculate the decimal value of the chromosome (bitstring).

    :param chromosome: Chromosome (bitstring) to evaluate
    :return: The decimal value of the chromosome (bitstring)
    :raises ValueError: If the chromosome is empty
    """
    if len(chromosome) == 0:
        raise ValueError(f"Empty chromosome cannot be evaluated: {chromosome}")
    return int("".join(str(bit) for bit in chromosome), 2)


def ones_fitness(chromosome: list) -> int:
    """
    Count the number of 1s (ones) in the chromosome (bitstring).

    :param chromosome: Chromosome (bitstring) to evaluate
    :return: The number of 1s (ones) in the chromosome (bitstring).
    :raises ValueError: If the chromosome is empty
    """
    if len(chromosome) == 0:
        raise ValueError(f"Empty chromosome cannot be evaluated: {chromosome}")
    number_of_ones = 0
    for bit in chromosome:
        number_of_ones += bit
    return number_of_ones


if __name__ == "__main__":
    # Bookkeeping
    generation_max_fitness = []
    generation_average_fitness = []

    # [begin-initialization]
    population = []
    for _ in range(POPULATION_SIZE):
        chromosome = choices([0, 1], k=BIT_STRING_LENGTH)
        population.append(chromosome)
    # [end-initialization]

    # [begin-generation-loop]
    for generation in range(GENERATIONS):
        # [begin-evaluation]
        population_fitness = []
        for chromosome in population:
            fitness = value_fitness(chromosome)
            population_fitness.append(fitness)
        # [end-evaluation]

        # Bookkeeping
        generation_max_fitness.append(max(population_fitness))
        generation_average_fitness.append(sum(population_fitness) // len(population_fitness))

        # [begin-selection]
        mating_pool = []
        for _ in range(POPULATION_SIZE):
            tournament_indices = choices(range(POPULATION_SIZE), k=TOURNAMENT_SIZE)
            chromosome = tournament_selection(population, population_fitness, tournament_indices)
            mating_pool.append(chromosome)
        # [end-selection]

        # [begin-crossover]
        for i in range(0, POPULATION_SIZE, 2):
            if random() < CROSSOVER_RATE:
                crossover_point = randrange(BIT_STRING_LENGTH)
                chromosome_1, chromosome_2 = one_point_crossover(mating_pool[i], mating_pool[i + 1], crossover_point)
                mating_pool[i] = chromosome_1
                mating_pool[i + 1] = chromosome_2
        # [end-crossover]

        # [begin-mutation]
        for i in range(POPULATION_SIZE):
            if random() < MUTATION_RATE:
                mutation_point = randrange(BIT_STRING_LENGTH)
                chromosome = bit_flip_mutation(mating_pool[i], mutation_point)
                mating_pool[i] = chromosome
        # [end-mutation]

        population = mating_pool
    # [end-generation-loop]

    # [begin-ending]
    population_fitness = []
    for chromosome in population:
        fitness = value_fitness(chromosome)
        population_fitness.append(fitness)
    print(population_fitness)
    print(population)
    generation_max_fitness.append(max(population_fitness))
    generation_average_fitness.append(sum(population_fitness) // len(population_fitness))
    # [end-ending]

    # plt.plot(generation_max_fitness, label="Best Fitness")
    # plt.plot(generation_average_fitness, label="Average Fitness")
    # plt.title("Fitness Over Time")
    # plt.xlabel("Generation")
    # plt.ylabel("Fitness")
    # plt.legend()
    # plt.show()