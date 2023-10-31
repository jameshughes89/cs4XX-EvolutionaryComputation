import json
import math
import random 
import matplotlib.pyplot as plt


# [begin-hyperparameters]

POPULATION_SIZE = 100 # Must be Even  
TOURNAMENT_SIZE = 5
GENERATIONS = 10000
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.10
FILENAME = "u1060"
# [end-hyperparameters]

#Clean Data
def importdata(FILENAME):
    tsp_json = open(f"resources/tsp/{FILENAME}.json")
    tsp_dictionary = json.load(tsp_json)
    city_list = tsp_dictionary['NODE_COORD_SECTION']
    return city_list
#Distance between two cites
def distance(city1, city2):
    xd = city1[1] - city2[1]
    yd = city1[2] - city2[2]    
    return math.sqrt((xd*xd) + (yd*yd)) 

#Take a list of cites and travel to them in order. Then from the last city return home
def distance_fitness(city_list):
    length = len(city_list)
    counter = 0
    total_distance = 0
    while counter < length -1:
        city1 = city_list[counter]
        city2 = city_list[counter + 1]        
        total_distance += distance(city1, city2)
        counter += 1        
    ### Go Home
    home = city_list[0]
    laststop = city_list[length - 1]
    total_distance += distance(home, laststop)
    return total_distance

def tournament_selection(
    population: list, population_fitness: list, selected_indices: list[int], direction: int = -1
) -> list:
    """
    Select the chromosome with the maximum/minimum fitness value of the chromosomes in the tournament. The chromosomes
    in the tournament if its index is contained within the selected_indices list. By default, the function selects for
    maximum fitness.

    :param population: Population of chromosomes to select from
    :param population_fitness: Fitness values of the population
    :param selected_indices: List of indices in the tournament
    :param direction: +1 for maximizing fitness, -1 for minimizing fitness
    :return: A copy of the selected chromosome
    :raises ValueError: If the list of selected indices is empty or contains an out-of-bounds index
    """
    if len(selected_indices) == 0:
        raise ValueError(f"List of indices in the tournament must be non empty: {selected_indices}")
    for index in selected_indices:
        if index < 0 or index > len(population_fitness) - 1:
            raise ValueError(f"List of indices in the tournament contains out-of-bounds index: {index}")
    max_value = population_fitness[selected_indices[0]] * direction
    max_index = selected_indices[0]
    for index in selected_indices:
        if population_fitness[index] * direction > max_value:
            max_value = population_fitness[index] * direction
            max_index = index
    return population[max_index][:]

def one_point_crossover(parent_1: list, parent_2: list, index: int) -> tuple[list, list]:
    """
    One point crossover. All elements at and after the crossover index are swapped between the two chromosomes.
    For example, with a crossover index of 2, [0,0,0,0,0], [1,1,1,1,1] -> [0,0,1,1,1], [1,1,0,0,0]. A crossover index of
    0 is allowed, but results in all contents being swapped.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param index: The index of the starting point of where all elements will be swapped between chromosomes
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if the index is out-of-bounds
    """
    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if index < 0 or index > len(parent_1) - 1:
        raise ValueError(f"Index out-of-bounds: {index}")
    child_1 = parent_1[:]
    child_2 = parent_2[:]
    child_1[index:], child_2[index:] = child_2[index:], child_1[index:]
    return child_1, child_2

def swap_mutation(parent: list, index_1: int, index_2: int) -> list:
    """
    Swap mutation. Swap the values between the two specified indices. For example, with swap indices of 0 and 3,
    [0, 1, 2, 3, 4] -> [3, 1, 2, 0, 4]. Providing the same index for both index values results in no change.

    :param parent: Chromosome to be mutated
    :param index_1: Index to be swapped with index_2
    :param index_2: Index to be swapped with index_1
    :return: The chromosome after the mutation is applied
    :raises ValueError: If either index is out-of-bounds
    """
    if index_1 < 0 or index_2 < 0 or index_1 > len(parent) - 1 or index_2 > len(parent) - 1:
        raise ValueError(f"Index out-of-bounds: {index_1}, {index_2}")
    child = parent[:]
    child[index_1], child[index_2] = child[index_2], child[index_1]
    return child



if __name__ == "__main__":
    city_list = importdata(FILENAME)
    LENGTH = len(city_list)

    # Bookkeeping
    generation_max_fitness = []
    generation_average_fitness = []
    
    # [begin-initialization]
    population = []
    for i in range(POPULATION_SIZE):
        new_list = random.sample(city_list, k=len(city_list))
        population.append(new_list)
    # [end-initialization]   

    
    # [begin-generation-loop]    
    for generation in range(GENERATIONS): 
        # [begin-evaluation]       
        population_fitness = []
        for chromosome in population:
            fitness = distance_fitness(chromosome)            
            population_fitness.append(fitness)                      
        # [end-evaluation]
        
        # Bookkeeping
        generation_max_fitness.append(min(population_fitness))
        generation_average_fitness.append(sum(population_fitness) // len(population_fitness))

        # [begin-selection]
        mating_pool = []
        for _ in range(POPULATION_SIZE):
            tournament_indices = random.choices(range(POPULATION_SIZE), k=TOURNAMENT_SIZE)            
            chromosome = tournament_selection(population, population_fitness, tournament_indices)
            mating_pool.append(chromosome)
        # [end-selection]

        # [begin-crossover]
        for i in range(0, POPULATION_SIZE, 2):
            if random.random() < CROSSOVER_RATE:
                crossover_point = random.randrange(LENGTH)
                chromosome_1, chromosome_2 = one_point_crossover(mating_pool[i], mating_pool[i + 1], crossover_point)
                mating_pool[i] = chromosome_1
                mating_pool[i + 1] = chromosome_2
        # [end-crossover]

        # [begin-mutation]
        for i in range(POPULATION_SIZE):
            if random.random() < MUTATION_RATE:
                mutation_point = random.randrange(LENGTH)
                mutation_point_swap = random.randrange(LENGTH)
                chromosome = swap_mutation(mating_pool[i], mutation_point, mutation_point_swap)
                mating_pool[i] = chromosome
        # [end-mutation]

        population = mating_pool
        print(generation)
    # [end-generation-loop]


    # [begin-ending]
    population_fitness = []
    for chromosome in population:
        fitness = distance_fitness(chromosome)
        population_fitness.append(fitness)
    
    print(population_fitness)
    print(len(population[2]))    
    generation_max_fitness.append(min(population_fitness))
    generation_average_fitness.append(sum(population_fitness) // len(population_fitness))
    # [end-ending]



    plt.plot(generation_max_fitness, label="Best Fitness")
    plt.plot(generation_average_fitness, label="Average Fitness")
    plt.title("Fitness Over Time")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.legend()
    plt.show()


    
    
    













