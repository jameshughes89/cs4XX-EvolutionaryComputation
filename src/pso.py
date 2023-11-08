"""
A particle swarm optimization algorithm for maximizing the value of some function

Particles are encoded as dictionaries that contain the particles position, the particles velocity, and the particles
best known position seen so far. Each of these values are encoded as vectors containing values for each dimension in the
function being optimized.
"""
import math

import numpy as np

# [begin-hyperparameters]
FUNCTION_DIMENSIONS = 2
START_POSITION_LOW_BOUND = -100
START_POSITION_HIGH_BOUND = 100
START_VELOCITY_LOW_BOUND = -0.1
START_VELOCITY_HIGH_BOUND = 0.1
NUMBER_OF_PARTICLES = 100
ITERATIONS = 100
INERTIA = 0.729844
COGNITIVE = 1.496180
SOCIAL = 1.496180

FUNCTION_NUMBER = 0

VELOCITY_DECAY_RATE = 0.9

POSITION_WRAP_METHOD = 1
VELOCITY_WRAP_METHOD = 2
# [end-hyperparameters]


class Functions:
    def __init__(self, function_number):
        match function_number:
            case 0:
                self.function = eggholder_function
                self.domain = [[-512, 512], [-512, 512]]
            case 1:
                self.function = schaffer2_function
                self.domain = [[-100, 0], [0, 100]]

    def hard_bounds(self, position):
        for index in range(len(position)):
            position[index] = min(max(position[index], self.domain[index][0]), self.domain[index][1])
        return position

    def half_bounds(self, position, old_position):
        for index in range(len(position)):
            if position[index] < self.domain[index][0]:
                position[index] = (old_position[index] + self.domain[index][0]) / 2
            elif position[index] > self.domain[index][1]:
                position[index] = (old_position[index] + self.domain[index][1]) / 2
        return position

    def wrap_bounds(self, position):
        for index in range(len(position)):
            position[index] = min(max(position[index], self.domain[index][0]), self.domain[index][1])
        return position


def eggholder_function(x, y):
    """
    Optimization function being searched through for the minimum value. This function's minimum value is at f(512,404.2319) = -959.6407
    and has a search domain of -512 <= x,y <= 512. This function was taken from the wikipedia article on "Test functions
    for optimization": https://en.wikipedia.org/wiki/Test_functions_for_optimization

    :param x: X value
    :param y: Y value
    :return: Result of the matyas function
    """
    y47 = y + 47
    value = -x * math.sin(math.sqrt(abs(x-y47)))
    value -= math.sin(math.sqrt(abs(x / 2 + y47))) * y47
    return value


def schaffer2_function(x, y):
    """
    Optimization function being searched through for the minimum value. This function's minimum value is at f(0, 0) = 0
    and has a search domain of -100 <= x,y <= 100. This function was taken from the wikipedia article on "Test functions
    for optimization": https://en.wikipedia.org/wiki/Test_functions_for_optimization

    :param x: X value
    :param y: Y value
    :return: Result of the matyas function
    """
    numerator = math.sin(x * x - y * y) * math.sin(x * x - y * y) - 0.5
    denominator = 1 + 0.001 * (x * x + y * y)
    return 0.5 + numerator / denominator / denominator


if __name__ == "__main__":
    function = Functions(FUNCTION_NUMBER)

    while(True):
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
                particle_value = function.function(*particle["position"])
                if particle_value < function.function(*particle["best_known_position"]):
                    particle["best_known_position"] = particle["position"]
                if particle_value < function.function(*global_best):
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

                match VELOCITY_WRAP_METHOD:
                    case 0:
                        pass
                    case 1:
                        particle['velocity'] = function.hard_bounds(particle["velocity"])
                    case 2:
                        particle['velocity'] = function.hard_bounds(particle["velocity"] * VELOCITY_DECAY_RATE)

                old_position = particle["position"]
                particle["position"] = particle["position"] + particle["velocity"]

                match POSITION_WRAP_METHOD:
                    case 0:
                        particle["position"] = function.hard_bounds(particle["position"])
                    case 1:
                        particle["position"] = function.half_bounds(particle["position"], old_position)
                    case 2:
                        particle["position"] = function.wrap_bounds(particle["position"])
            # [end-position-update]
        # [end-iteration-loop]

        # [begin-ending]
        print(global_best, function.function(*global_best))
        print(function.function(0, 0))
        if function.function(*global_best) < -960:
            exit(0)
        # [end-ending]