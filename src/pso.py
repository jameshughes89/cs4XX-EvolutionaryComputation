"""
A particle swarm optimization algorithm for maximizing the value of some function

Particles are encoded as dictionaries that contain the particles position, the particles velocity, and the particles
best known position seen so far. Each of these values are encoded as vectors containing values for each dimension in the
function being optimized.
"""

import numpy as np

FUNCTION_DIMENSIONS = 2
LOW_BOUND = -10
HIGH_BOUND = 10
NUMBER_OF_PARTICLES = 10
ITERATIONS = 100
INERTIA = 0.729844
COGNITIVE = 1.496180
SOCIAL = 1.496180


def matyas_function(x, y):
    """
    Optimization function being searched through for the minimum value. This function's minimum value is at f(0,0) = 0
    and has a search domain of -10 <= x,y <= 10. This function was taken from the wikipedia article on "Test functions
    for optimization": https://en.wikipedia.org/wiki/Test_functions_for_optimization

    :param x: X value
    :param y: Y value
    :return: Result of the matyas function
    """
    return 0.26 * (x**2 + y**2) - 0.48 * x * y


if __name__ == "__main__":
    # Initialize
    particles = []
    for _ in range(NUMBER_OF_PARTICLES):
        particle = {
            "position": np.random.uniform(LOW_BOUND, HIGH_BOUND, FUNCTION_DIMENSIONS),
            "velocity": np.random.uniform(-0.1, 0.1, FUNCTION_DIMENSIONS),
        }
        particle["best_known_position"] = particle["position"]
        particles.append(particle)
    global_best = particles[0]["position"]

    # Run for a Specified Number of Iterations (Termination)
    for _ in range(ITERATIONS):
        # Calculate fitness
        for particle in particles:
            particle_value = matyas_function(*particle["position"])
            if particle_value < matyas_function(*particle["best_known_position"]):
                particle["best_known_position"] = particle["position"]
            if particle_value < matyas_function(*global_best):
                global_best = particle["position"]

        # Update velocity and position (variation)
        for particle in particles:
            r1 = np.random.rand()
            r2 = np.random.rand()
            particle["velocity"] = (
                INERTIA * particle["velocity"]
                + COGNITIVE * r1 * (particle["best_known_position"] - particle["position"])
                + SOCIAL * r2 * (global_best - particle["position"])
            )
            particle["position"] = particle["position"] + particle["velocity"]

    print(global_best, matyas_function(*global_best))