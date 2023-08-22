"""
A genetic programming for symbolic regression.

Data from some unknown function is read in from a file. Rows represent observations of the function and columns
represent the variables. The last column in the file must be the dependant variable. The file can contain arbitrarily
many variables but should contain at least two --- one independent and one dependent variable.
"""

import operator
from random import randint

from deap import algorithms, base, creator, gp, tools

# [begin-hyperparameters]
POPULATION_SIZE = 10
GENERATIONS = 100
TOURNAMENT_SIZE = 2
CROSSOVER_RATE = 0.70
MUTATION_RATE = 0.05
# [end-hyperparameters]


def mean_squared_error(
    compiled_individual, independent_variables: list[list[float]], dependent_variable: list[float]
):
    """
    Calculate the mean squared error for a given function on the observed data. The independent variables are a list of
    lists where the list of the outer list is the number of observations and the length of the inside list is the number
    of independent variables. The length of the dependent variables is the number of observations.

    :param compiled_individual: A callable function that the dependent variables
    :param independent_variables: Values given to the function to predict
    :param dependent_variable: Expected result of the function
    :return: Mean squared error of the function on the observed data
    :raises ValueError: If the number of observations s 0 or if there are a different number of observations
    """
    if len(independent_variables) == 0 or len(dependent_variable) == 0:
        raise ValueError("Number of dependent and independent variables must be greater than 0")
    if len(independent_variables) != len(dependent_variable):
        raise ValueError(
            f"Uneven number of observations of independent and dependent variables: "
            f"{len(independent_variables)}, {len(dependent_variable)}"
        )
    squared_errors = []
    for xs, y in zip(independent_variables, dependent_variable):
        y_hat = compiled_individual(*xs)
        squared_errors.append((y - y_hat) ** 2)
    return sum(squared_errors) / len(dependent_variable)


def protected_divide(dividend: float, divisor: float) -> float:
    """
    The basic arithmetic operator of division. If the division basic results in a ZeroDivisionError, this function
    returns an arbitrarily large number (999,999,999).

    :param dividend: Value to divide
    :param divisor: Value to divide by
    :return: The quotient; the result of the division (dividend/divisor)
    """
    if divisor == 0:
        return 999_999_999
    else:
        return dividend / divisor


if __name__ == "__main__":
    # [begin-language]
    primitive_set = gp.PrimitiveSet("MAIN", 1)
    primitive_set.addPrimitive(operator.add, 2)
    primitive_set.addPrimitive(operator.sub, 2)
    primitive_set.addPrimitive(operator.mul, 2)
    primitive_set.addPrimitive(protected_divide, 2)
    primitive_set.addPrimitive(operator.neg, 1)
    primitive_set.addEphemeralConstant("rand_int", lambda: randint(-10, 10))
    # [end-language]
