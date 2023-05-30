"""
A simple genetic algorithm for maximizing an integer.

The integer is encoded as a bit string (list of 0s or 1s). Fitness is calculated with either the value of the bit string
or the number of 1s in the bit string (both are included for a comparison). Crossover is a single point crossover and
mutation is a bit flip mutation.
"""
from random import choices, random, randrange

BIT_STRING_LENGTH = 16
POPULATION_SIZE = 10
GENERATIONS = 100
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10


def bit_flip_mutation(parent, mutation_point):
    """
    Bit flip mutation. Flip the bit at the specified index. In other words, if the bit is a 0, change it to be a 1, and
    if the bit is a 1, change it to be a 0. For example, with mutation point of 2, [0,0,0,0,0] -> [0,0,1,0,0]. This
    function has no side effects; the chromosome provided as the argument is left unchanged.

    :param parent: Chromosome to be mutated
    :param mutation_point: Index of the bit to be flipped
    :return: The chromosome after the mutation is applied
    :raises ValueError: If the mutation point is out of bounds
    """
    if mutation_point < 0 or mutation_point > len(parent) - 1:
        raise ValueError(f"mutation_point out of bounds: {mutation_point}")
    child = parent[:]
    child[mutation_point] = (child[mutation_point] + 1) % 2
    return child


def value_fitness(chromosome):
    """
    Calculate the decimal value of the chromosome (bit string).

    :param chromosome: Chromosome (bit string) to evaluate
    :return: The decimal value of the chromosome (bit string)
    """
    return int("".join(str(bit) for bit in chromosome), 2)


def ones_fitness(chromosome):
    """
    Count the number of 1s (ones) in the chromosome (bit string).

    :param chromosome: Chromosome (bit string) to evaluate
    :return: The number of 1s (ones) in the chromosome (bit string).
    """
    number_of_ones = 0
    for bit in chromosome:
        number_of_ones += bit
    return number_of_ones


def tournament_selection(population, population_fitness, selected_indices):
    """
    Select the chromosome with the maximum fitness value of the chromosomes in the tournament. The chromosomes in the
    tournament if its index is contained within the selected_indices list.

    :param population: Population of chromosomes to select from
    :param population_fitness: Fitness values of the population
    :param selected_indices: List of indices in the tournament
    :return: A copy of the selected chromosome
    :raises ValueError: If the list of selected indices is empty or contains an out of bounds index
    """
    if len(selected_indices) == 0:
        raise ValueError(f"List of indices in the tournament must be non empty: {selected_indices}")
    for index in selected_indices:
        if index < 0 or index > len(population_fitness) - 1:
            raise ValueError(f"List of indices in the tournament contains out of bounds index: {index}")
    max_value = 0
    max_index = 0
    for index in selected_indices:
        if population_fitness[index] > max_value:
            max_value = population_fitness[index]
            max_index = index
    return population[max_index][:]


def one_point_crossover(parent_1, parent_2, crossover_point):
    """
    One point crossover. All elements at and after the crossover point are swapped between the two chromosomes.
    For example, with a crossover point of 2, [0,0,0,0,0], [1,1,1,1,1] -> [0,0,1,1,1], [1,1,0,0,0]. A crossover point of
    0 is allowed, but results in all contents being swapped. This function has no side effects; the chromosomes provided
    as arguments are left unchanged.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param crossover_point: The index of the starting point of where all elements will be swapped between chromosomes
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if the crossover point is out of bounds
    """
    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if crossover_point < 0 or crossover_point > len(parent_1) - 1:
        raise ValueError(f"crossover_point out of bounds: {crossover_point}")
    child_1 = parent_1[:]
    child_2 = parent_2[:]
    child_1[crossover_point:], child_2[crossover_point:] = child_2[crossover_point:], child_1[crossover_point:]
    return child_1, child_2


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
    new_population = []
    for _ in range(POPULATION_SIZE):
        tournament_indices = choices(range(POPULATION_SIZE))
        chromosome = tournament_selection(population, population_fitness, tournament_indices)
        new_population.append(chromosome)

    # Variation (Crossover)
    for i in range(0, POPULATION_SIZE, 2):
        if random() < CROSSOVER_RATE:
            crossover_point = randrange(BIT_STRING_LENGTH)
            chromosome_1, chromosome_2 = one_point_crossover(new_population[i], new_population[i + 1], crossover_point)
            new_population[i] = chromosome_1
            new_population[i + 1] = chromosome_2

    # Variation (Mutation)
    for i in range(POPULATION_SIZE):
        if random() < MUTATION_RATE:
            mutation_point = randrange(BIT_STRING_LENGTH)
            chromosome = bit_flip_mutation(new_population[i], mutation_point)
            new_population[i] = chromosome

    population = new_population

print(population_fitness)
