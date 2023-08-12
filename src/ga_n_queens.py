"""
A genetic algorithm for n queens.

The queen placements is encoded as a permutation of length n containing integers 0 -- 7 inclusively. This encoding
ensures that no two queens are in the same row or column, thus the only potential for attacking is diagonal. Fitness
is calculated as the number of attacking queens (each pair of attacking queens is counted only once). Crossover is a
permutation safe order crossover and mutation is a permutation safe swap mutation.
"""
from random import choices, random, randrange, sample

from src.crossover import order_crossover
from src.mutation import swap_mutation
from src.selection import tournament_selection

N_QUEENS = 8
POPULATION_SIZE = 10
GENERATIONS = 100
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10


def attacking_fitness(chromosome: list) -> int:
    """
    Count the number of attacking queens in the provided queen placements. To count each attacking pair only once, the
    check for attacking only happens in the forward direction (from index 0 towards n). With the permutation
    representation, attacking can only happen in a diagonal, thus the check for attacking is to check only +/- offset,
    where offset is the number of indices away the queens are from each other. For example, consider the chromosome
    [?, ?, 4, 3, 6, 1, ?, ?]. The queen at index 2 is attacking 3 queens: it attacks the queen at index 3 as it is
    offset 1 and 4-1=3, it is attacking the queen at index 4 as it is offset 2 and 4+2=6, and it is attacking the queen
    at index 5 as it is offset 3 and 4-3=1.

    :param chromosome: Chromosome (queen placements) to evaluate
    :return: The number of attacking queens.
    """
    total_attackers = 0
    for attacker_column, attacker_row in enumerate(chromosome):
        for victim_index in range(attacker_column + 1, len(chromosome)):
            offset = victim_index - attacker_column
            victim_row = chromosome[victim_index]
            if (attacker_row - offset) == victim_row or (attacker_row + offset) == victim_row:
                total_attackers += 1
    return total_attackers


if __name__ == "__main__":
    # [begin-initialization]
    population = []
    population_fitness = []
    for _ in range(POPULATION_SIZE):
        chromosome = sample(range(N_QUEENS), k=N_QUEENS)
        population.append(chromosome)
    # [end-initialization]

    # [begin-generation-loop]
    for generation in range(GENERATIONS):
        # [begin-evaluation]
        population_fitness = []
        for chromosome in population:
            fitness = attacking_fitness(chromosome)
            population_fitness.append(fitness)
        # [end-evaluation]

        # [begin-selection]
        mating_pool = []
        for _ in range(POPULATION_SIZE):
            tournament_indices = choices(range(POPULATION_SIZE), k=2)
            chromosome = tournament_selection(population, population_fitness, tournament_indices, direction=-1)
            mating_pool.append(chromosome)
        # [end-selection]

        # [begin-crossover]
        for i in range(0, POPULATION_SIZE, 2):
            if random() < CROSSOVER_RATE:
                index_one = randrange(N_QUEENS)
                index_two = randrange(N_QUEENS)
                start_index = min(index_one, index_two)
                end_index = max(index_one, index_two)
                chromosome_1, chromosome_2 = order_crossover(mating_pool[i], mating_pool[i + 1], start_index, end_index)
                mating_pool[i] = chromosome_1
                mating_pool[i + 1] = chromosome_2
        # [end-crossover]

        # [begin-mutation]
        for i in range(POPULATION_SIZE):
            if random() < MUTATION_RATE:
                index_one = randrange(N_QUEENS)
                index_two = randrange(N_QUEENS)
                chromosome = swap_mutation(mating_pool[i], index_one, index_two)
                mating_pool[i] = chromosome
        # [end-mutation]

        population = mating_pool
    # [end-generation-loop]

    # [begin-ending]
    population_fitness = []
    for chromosome in population:
        fitness = attacking_fitness(chromosome)
        population_fitness.append(fitness)
    print(population_fitness)
    print(population)
    # [end-ending]
