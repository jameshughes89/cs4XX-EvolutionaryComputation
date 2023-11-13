import copy
import random
import numpy as np

POPULATION_SIZE = 30
GENERATIONS = 100
ACCEPT_NUMBER = 2


def value_fitness(individual):
    if len(individual) != 2:
        raise ValueError(f"The length of individual is incorrect: {len(individual)}")
    return individual[0] ** 2 + individual[1] ** 2


def initialize_belief_space():
    # initialize situational
    belief_space = {"situational": None, "normative": []}
    # initialize normative
    for _ in range(2):
        # [min, max, Lower, Upper]
        belief_space["normative"].append([-10, 10, 100, 100])
    return belief_space


def accept(population, population_fitness):
    combined_data = list(zip(population, population_fitness))
    sorted_combined_data = sorted(combined_data, key=lambda x: x[1])
    sorted_population, sorted_population_fitness = zip(*sorted_combined_data)
    return list(sorted_population[:ACCEPT_NUMBER])


def update(belief_space, n_accepted):
    update_belief_space = copy.deepcopy(belief_space)
    for x_l in n_accepted:
        # update situational
        if update_belief_space["situational"] is None:
            update_belief_space["situational"] = x_l
        elif value_fitness(x_l) < value_fitness(update_belief_space["situational"]):
            update_belief_space["situational"] = x_l

        # update_normative
        for j in range(2):
            bound = update_belief_space["normative"][j]
            # update min and L
            if x_l[j] <= bound[0] or value_fitness(x_l) < bound[2]:
                bound[0] = x_l[j]
                bound[2] = value_fitness(x_l)
            # update max and U
            if x_l[j] >= bound[1] or value_fitness(x_l) < bound[3]:
                bound[1] = x_l[j]
                bound[3] = value_fitness(x_l)
    return update_belief_space


def influence_method_1(population, belief_space):
    influence_population = copy.deepcopy(population)
    for i in range(len(influence_population)):
        for j in range(2):
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            influence_population[i][j] = influence_population[i][j] + size * np.random.normal(0, 1)
    return influence_population


def influence_method_2(population, belief_space):
    influence_population = copy.deepcopy(population)
    for i in range(len(influence_population)):
        for j in range(2):
            s = belief_space["situational"]
            strategy = random.uniform(-1, 1)
            if influence_population[i][j] < s[j]:
                influence_population[i][j] = influence_population[i][j] + abs(strategy * np.random.normal(0, 1))
            elif influence_population[i][j] > s[j]:
                influence_population[i][j] = influence_population[i][j] - abs(strategy * np.random.normal(0, 1))
            else:
                influence_population[i][j] = influence_population[i][j] + strategy * np.random.normal(0, 1)
    return influence_population


def influence_method_3(population, belief_space):
    influence_population = copy.deepcopy(population)
    for i in range(len(population)):
        for j in range(2):
            s = belief_space["situational"]
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            if influence_population[i][j] < s[j]:
                influence_population[i][j] = influence_population[i][j] + abs(size * np.random.normal(0, 1))
            elif influence_population[i][j] > s[j]:
                influence_population[i][j] = influence_population[i][j] - abs(size * np.random.normal(0, 1))
            else:
                influence_population[i][j] = influence_population[i][j] + size * np.random.normal(0, 1)
    return influence_population


def influence_method_4(population, belief_space):
    influence_population = copy.deepcopy(population)
    for i in range(len(influence_population)):
        for j in range(2):
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            beta = 1
            if influence_population[i][j] < bound[0]:
                influence_population[i][j] = influence_population[i][j] + abs(size * np.random.normal(0, 1))
            elif influence_population[i][j] > bound[1]:
                influence_population[i][j] = influence_population[i][j] - abs(size * np.random.normal(0, 1))
            else:
                influence_population[i][j] = influence_population[i][j] + beta * size * np.random.normal(0, 1)
    return influence_population


if __name__ == '__main__':
    # [begin-initialize-population]
    population = []
    for _ in range(POPULATION_SIZE):
        individual = [random.uniform(-10, 10) for _ in range(2)]
        population.append(individual)
    # [end-initialize-population]

    belief_space = initialize_belief_space()

    # [begin-evolve]
    for generation in range(GENERATIONS):
        # evaluation
        population_fitness = []
        for individual in population:
            fitness = value_fitness(individual)
            population_fitness.append(fitness)

        n_accepted = accept(population, population_fitness)
        belief_space = update(belief_space, n_accepted)
        influence_population = influence_method_4(population, belief_space)

        population = influence_population
    # [end-evolve]

    print(belief_space["situational"])
    print(value_fitness(belief_space["situational"]))
