"""
A particle swarm optimization algorithm for maximizing the value of some function

Particles are encoded as dictionaries that contain the particles position, the particles velocity, and the particles
best known position seen so far. Each of these values are encoded as vectors containing values for each dimension in the
function being optimized.
"""



def matyas_function(x, y):
    """
    Optimization function being searched through for the minimum value. This function's minimum value is at f(0,0) = 0
    and has a search domain of -10 <= x,y <= 10. This function was taken from the wikipedia article on "Test functions
    for optimization": https://en.wikipedia.org/wiki/Test_functions_for_optimization

    :param x: X value
    :param y: Y value
    :return: Result of the matyas function
    """
    return 0.26*(x**2 + y**2) - 0.48*x*y
