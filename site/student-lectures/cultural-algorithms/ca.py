import math
import random
import numpy as np

POPULATION_SIZE = 30
GENERATIONS = 100
ACCEPT_NUMBER = 2

def fitness_function(individual):
    return individual[0] ** 2 + individual[1] ** 2

def initialize_population():
    population = []
    for _ in range(POPULATION_SIZE):
        individual = [random.uniform(-10, 10) for _ in range(2)]
        population.append(individual)
    return population


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
    # ACCEPT_NUMBER is a constant
    return sorted_population[:ACCEPT_NUMBER]


def update(belief_space, n_accepted):
    for x_l in n_accepted:
        # update situational
        if belief_space["situational"] is None:
            belief_space["situational"] = x_l
        elif fitness_function(x_l) < fitness_function(belief_space["situational"]):
            belief_space["situational"] = x_l

        # update_normative
        for j in range(2):
            bound = belief_space["normative"][j]
            # update min and L
            if x_l[j] <= bound[0] or fitness_function(x_l) < bound[2]:
                bound[0] = x_l[j]
                bound[2] = fitness_function(x_l)
            # update max and U
            if x_l[j] >= bound[1] or fitness_function(x_l) < bound[3]:
                bound[1] = x_l[j]
                bound[3] = fitness_function(x_l)

    print(belief_space)


def influence_method_1(population):
    for i in range(len(population)):
        for j in range(2):
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            population[i][j] = population[i][j] + size * np.random.normal(0, 1)


def influence_method_2(population):
    for i in range(len(population)):
        for j in range(2):
            s = belief_space["situational"]
            strategy = random.uniform(-1, 1)
            if population[i][j] < s[j]:
                population[i][j] = population[i][j] + abs(strategy * np.random.normal(0, 1))
            elif population[i][j] > s[j]:
                population[i][j] = population[i][j] - abs(strategy * np.random.normal(0, 1))
            else:
                population[i][j] = population[i][j] + strategy * np.random.normal(0, 1)


def influence_method_3(population):
    for i in range(len(population)):
        for j in range(2):
            s = belief_space["situational"]
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            if population[i][j] < s[j]:
                population[i][j] = population[i][j] + abs(size * np.random.normal(0, 1))
            elif population[i][j] > s[j]:
                population[i][j] = population[i][j] - abs(size * np.random.normal(0, 1))
            else:
                population[i][j] = population[i][j] + size * np.random.normal(0, 1)


def influence_method_4(population):
    for i in range(len(population)):
        for j in range(2):
            bound = belief_space["normative"][j]
            size = bound[1] - bound[0]
            beta = 1
            if population[i][j] < bound[0]:
                population[i][j] = population[i][j] + abs(size * np.random.normal(0, 1))
            elif population[i][j] > bound[1]:
                population[i][j] = population[i][j] - abs(size * np.random.normal(0, 1))
            else:
                population[i][j] = population[i][j] + beta * np.random.normal(0, 1)


# [begin-main]
if __name__ == '__main__':
    # initialize population
    population = initialize_population()
    # initialize belief space
    belief_space = initialize_belief_space()

    for generation in range(GENERATIONS):
        # evaluation
        population_fitness = []
        for individual in population:
            fitness = fitness_function(individual)
            population_fitness.append(fitness)

        # accept
        n_accepted = accept(population, population_fitness)

        # update
        update(belief_space, n_accepted)

        # influence
        # influence_method_1(population)
        # influence_method_2(population)
        # influence_method_3(population)
        influence_method_4(population)

        # do genetic operators

    print(belief_space["situational"])
    print(fitness_function(belief_space["situational"]))
# [end-main]
