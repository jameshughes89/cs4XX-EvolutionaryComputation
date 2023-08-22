"""
A genetic programming for symbolic regression.

Data from some unknown function is read in from a file. Rows represent observations of the function and columns
represent the variables. The last column in the file must be the dependant variable. The file can contain arbitrarily
many variables but should contain at least two --- one independent and one dependent variable.
"""

# [begin-hyperparameters]

# [end-hyperparameters]


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
        return dividend/divisor

