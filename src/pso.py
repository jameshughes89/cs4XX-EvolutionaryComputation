"""
A particle swarm optimization algorithm for maximizing the value of some function

Particles are encoded as dictionaries that contain the particles position, the particles velocity, and the particles
best known position seen so far. Each of these values are encoded as vectors containing values for each dimension in the
function being optimized.
"""

import numpy as np

# [begin-hyperparameters]
FUNCTION_DIMENSIONS = 2
START_POSITION_LOW_BOUND = -10
START_POSITION_HIGH_BOUND = 10
START_VELOCITY_LOW_BOUND = -0.1
START_VELOCITY_HIGH_BOUND = 0.1
NUMBER_OF_PARTICLES = 10
ITERATIONS = 100
INERTIA = 0.729844
COGNITIVE = 1.496180
SOCIAL = 1.496180
# [end-hyperparameters]


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
    # [begin-initialization]
    particles = []
    for _ in range(NUMBER_OF_PARTICLES):
        particle = {
            "position": np.random.uniform(START_POSITION_LOW_BOUND, START_POSITION_HIGH_BOUND, FUNCTION_DIMENSIONS),
            "velocity": np.random.uniform(START_VELOCITY_LOW_BOUND, START_VELOCITY_HIGH_BOUND, FUNCTION_DIMENSIONS),
        }
        particle["best_known_position"] = particle["position"]
        particles.append(particle)
    global_best = particles[0]["position"]
    # [end-initialization]

    # [begin-iteration-loop]
    for _ in range(ITERATIONS):
        # [begin-evaluation]
        for particle in particles:
            particle_value = matyas_function(*particle["position"])
            if particle_value < matyas_function(*particle["best_known_position"]):
                particle["best_known_position"] = particle["position"]
            if particle_value < matyas_function(*global_best):
                global_best = particle["position"]
        # [end-evaluation]

        # [begin-position-update]
        for particle in particles:
            r1 = np.random.rand(FUNCTION_DIMENSIONS)
            r2 = np.random.rand(FUNCTION_DIMENSIONS)
            particle["velocity"] = (
                INERTIA * particle["velocity"]
                + COGNITIVE * r1 * (particle["best_known_position"] - particle["position"])
                + SOCIAL * r2 * (global_best - particle["position"])
            )
            particle["position"] = particle["position"] + particle["velocity"]
        # [end-position-update]
    # [end-iteration-loop]

    # [begin-ending]
    print(global_best, matyas_function(*global_best))
    # [end-ending]
