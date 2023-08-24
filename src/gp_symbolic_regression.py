"""
A genetic programming for symbolic regression.

Data from some unknown function is read in from a file. Rows represent observations of the function and columns
represent the variables. The last column in the file must be the dependant variable. The file can contain arbitrarily
many variables but should contain at least two --- one independent and one dependent variable.
"""
import math
import operator
import os.path
from functools import partial
from random import randint

import numpy
from deap import algorithms, base, creator, gp, tools

# [begin-hyperparameters]
POPULATION_SIZE = 10
GENERATIONS = 100
TOURNAMENT_SIZE = 2
CROSSOVER_RATE = 0.80
MUTATION_RATE = 0.05
# [end-hyperparameters]

# [begin-data-parameters]
RELATIVE_RESOURCES = "../resources/regression-data/"
DATA_FILE = "d0.csv"
# [end-data-parameters]


def protected_divide(dividend: float, divisor: float) -> float:
    """
    The basic arithmetic operator of division. If the division basic results in a ZeroDivisionError, this function
    returns an arbitrarily large number (999,999,999).

    :param dividend: Value to divide
    :param divisor: Value to divide by
    :return: The quotient; the result of the division (dividend/divisor)
    """
    if divisor == 0:
        return math.inf
    else:
        return dividend / divisor


def mean_squared_error(
    compiled_individual, independent_variables: list[list[float]], dependent_variable: list[float]
) -> float:
    """
    Calculate the mean squared error for a given function on the observed data. The independent variables are a list of
    lists where the list of the outer list is the number of observations and the length of the inside list is the number
    of independent variables. The length of the dependent variables is the number of observations.

    :param compiled_individual: A callable function that the dependent variables are give to as arguments
    :param independent_variables: Values given to the function to predict
    :param dependent_variable: Expected result of the function
    :return: Mean squared error of the function on the observed data
    """
    running_error_squared_sum = 0
    for xs, y in zip(independent_variables, dependent_variable):
        y_hat = compiled_individual(*xs)
        running_error_squared_sum += (y - y_hat) ** 2
    return running_error_squared_sum / len(dependent_variable)


def mean_squared_error_fitness(
    individual, toolbox, independent_variables: list[list[float]], dependent_variable: list[float]
) -> tuple[float]:
    """
    Calculate the mean squared error for a given function on the observed data. The independent variables are a list of
    lists where the list of the outer list is the number of observations and the length of the inside list is the number
    of independent variables. The length of the dependent variables is the number of observations.

    :param individual: A deap representation of a function that the dependent variables are give to as arguments
    :param toolbox: A deap toolbox
    :param independent_variables: Values given to the function to predict
    :param dependent_variable: Expected result of the function
    :return: A tuple containing the mean squared error of the function on the observed data
    :raises ValueError: If the number of observations s 0 or if there are a different number of observations
    """
    if len(independent_variables) == 0 or len(dependent_variable) == 0:
        raise ValueError("Number of dependent and independent variables must be greater than 0")
    if len(independent_variables) != len(dependent_variable):
        raise ValueError(
            f"Uneven number of observations of independent and dependent variables: "
            f"{len(independent_variables)}, {len(dependent_variable)}"
        )
    callable_function = toolbox.compile(expr=individual)
    individual_mean_squared_error = mean_squared_error(callable_function, independent_variables, dependent_variable)
    return (individual_mean_squared_error,)


if __name__ == "__main__":
    # [begin-data]
    data_file = open(os.path.join(RELATIVE_RESOURCES, DATA_FILE))
    all_data = [list(map(float, x.split(","))) for x in data_file]
    independent_variables = [observation[:-1] for observation in all_data]
    dependent_variable = [observation[-1] for observation in all_data]
    # [end-data]

    # [begin-language]
    primitive_set = gp.PrimitiveSet("MAIN", len(independent_variables[0]))
    primitive_set.addPrimitive(operator.add, 2)
    primitive_set.addPrimitive(operator.sub, 2)
    primitive_set.addPrimitive(operator.mul, 2)
    primitive_set.addPrimitive(protected_divide, 2)
    primitive_set.addPrimitive(operator.neg, 1)
    primitive_set.addEphemeralConstant("rand_int", partial(randint, -10, 10))
    # [end-language]

    # [begin-setting-hyperparameters]
    creator.create("FitnessMinimum", base.Fitness, weights=(-1.0,))
    creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMinimum)

    toolbox = base.Toolbox()
    toolbox.register("generate_tree", gp.genHalfAndHalf, pset=primitive_set, min_=1, max_=4)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.generate_tree)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("compile", gp.compile, pset=primitive_set)
    toolbox.register(
        "evaluate",
        mean_squared_error_fitness,
        toolbox=toolbox,
        independent_variables=independent_variables,
        dependent_variable=dependent_variable,
    )
    toolbox.register("select", tools.selTournament, tournsize=2)
    toolbox.register("mate", gp.cxOnePoint)
    toolbox.register("generate_mutation_subtree", gp.genFull, min_=0, max_=4)
    toolbox.register("mutate", gp.mutUniform, expr=toolbox.generate_mutation_subtree, pset=primitive_set)
    # [end-setting-hyperparameters]

    # [begin-bloat-control]
    toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=6))
    toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=6))
    toolbox.decorate("mate", gp.staticLimit(key=len, max_value=32))
    toolbox.decorate("mutate", gp.staticLimit(key=len, max_value=32))
    # [end-bloat-control]

    # [begin-bookkeeping]
    hall_of_fame = tools.HallOfFame(1)
    stats_fit = tools.Statistics(lambda individual: individual.fitness.values)
    stats_size = tools.Statistics(len)
    stats_height = tools.Statistics(operator.attrgetter("height"))
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size, height=stats_height)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)
    # [end-bookkeeping]

    # [begin-run]
    population = toolbox.population(n=POPULATION_SIZE)
    population, log = algorithms.eaSimple(
        population, toolbox, 0.5, 0.1, GENERATIONS, stats=mstats, halloffame=hall_of_fame, verbose=True
    )
    # [end-run]

    # [begin-ending]
    print(str(hall_of_fame[0]))
    print(hall_of_fame[0].fitness.values)
    # [end-ending]
