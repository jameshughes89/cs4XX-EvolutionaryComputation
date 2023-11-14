import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Problem settings
def sum_of_squares_equation(x):
    """
    Calculate the sum of squares for a list of numbers.

    :param x: List of numbers for which the sum of squares will be calculated.
    :type x: list of numbers
    :return: The sum of squares of the input numbers.
    :rtype: float
    """
    return sum([i**2 for i in x])


# Memetic Algorithm
class MemeticAlgorithm:
    def __init__(self, pop_size, dimensions, mutation_rate, crossover_rate, max_generations):
        self.pop_size = pop_size
        self.dimensions = dimensions
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.max_generations = max_generations
        self.population = np.random.randn(pop_size, dimensions)
        self.best_solution = None
        self.best_fitness = float("inf")
        self.fitness_history = []

    def fitness(self, solution):
        """
        Calculate the fitness score of a given solution.

        :param solution: A list or data structure representing the solution to be evaluated.
        :type solution: list or data structure
        :return: A numerical value representing the fitness score of the solution.
        :rtype: float
        """
        return sum_of_squares_equation(solution)

    def select_parents(self):
        """
        Perform tournament selection to choose parents for the next generation.
        This function conducts a tournament selection process to select parents from the current population.
        It randomly pairs individuals and selects the one with the higher fitness value as a parent.

        :return: An array containing the selected parents for the next generation.
        :rtype: numpy.ndarray
        .. note::
        The number of selected parents is equal to the population size defined for the genetic algorithm.
        """
        parents = []
        for _ in range(self.pop_size):
            i, j = np.random.randint(0, self.pop_size, 2)
            if self.fitness(self.population[i]) < self.fitness(self.population[j]):
                parents.append(self.population[i])
            else:
                parents.append(self.population[j])
        return np.array(parents)

    def crossover(self, parent1, parent2, rand=None):
        """
        Perform a crossover operation between two parent individuals.

        :param parent1: The first parent individual.
        :type parent1: array-like
        :param parent2: The second parent individual.
        :type parent2: array-like
        :returns: A tuple containing two child individuals resulting from the crossover operation. If the crossover rate is below the specified threshold, the function returns the parents unaltered.
        :rtype: tuple
        """
        if rand is None:
            rand = np.random.rand()

        if rand < self.crossover_rate:
            crossover_point = np.random.randint(1, self.dimensions)
            child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
            child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, solution, rand_values=None):
        """
        Apply mutation to the given solution.
        This method applies mutation to the input solution by randomly altering the values of
        its elements. The mutation is controlled by the `mutation_rate` property of the object.
        For each element in the solution, a random value is generated using a standard normal
        distribution (mean = 0, standard deviation = 1), and if a randomly generated value is
        less than the `mutation_rate`, the corresponding element in the solution is modified
        by adding the random value. Returns the mutated solution as a NumPy array.

        :param solution: The solution to be mutated, represented as a NumPy array.
        :type solution: numpy.ndarray
        :returns: The mutated solution, with random changes applied to some elements.
        :rtype: numpy.ndarray
        """
        if rand_values is None:
            rand_values = np.random.rand(self.dimensions)

        for i in range(self.dimensions):
            if rand_values[i] < self.mutation_rate:
                solution[i] += np.random.randn()

        return solution

    def local_search(self, solution):
        """
        Perform Hill Climbing local search to improve a given solution.
        This function applies Hill Climbing local search by iteratively generating new solutions by adding small random steps
        to the current solution. If a generated solution results in a better fitness value than the current solution, it
        replaces the current solution with the new one. This process is repeated for a fixed number of iterations (10 by
        default).

        :param solution: numpy array-like. The initial solution to be optimized.
        :return: numpy.ndarray. The optimized solution after a number of local search steps.
        """
        for _ in range(10):  # number of local search steps
            new_solution = solution + np.random.randn(self.dimensions) * 0.1  # small random step
            if self.fitness(new_solution) < self.fitness(solution):
                solution = new_solution
        return solution

    def run(self):
        """
        Evolve a population of solutions over multiple generations using a genetic algorithm.
        This method runs the genetic algorithm for a specified number of generations, aiming to find the
        best solution with the highest fitness in the population.

        :param max_generations: The number of generations to run the genetic algorithm.
        :type max_generations: int
        :return: A tuple containing the best solution found and its fitness score.
        :rtype: Tuple[Any, float]
        :note: This method updates the internal state of the genetic algorithm object, including the population, fitness history, and the best solution found so far.
        """
        for generation in range(self.max_generations):
            new_population = []
            parents = self.select_parents()
            for i in range(0, self.pop_size, 2):
                parent1, parent2 = parents[i], parents[i + 1]
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                child1 = self.local_search(child1)
                child2 = self.local_search(child2)
                new_population.extend([child1, child2])

            self.population = np.array(new_population)
            current_best = min(self.population, key=self.fitness)
            current_best_fitness = self.fitness(current_best)
            self.fitness_history.append(current_best_fitness)

            if current_best_fitness < self.best_fitness:
                self.best_solution = current_best
                self.best_fitness = current_best_fitness

        return self.best_solution, self.best_fitness


# Parameters for the memetic algorithm
pop_size = 50
dimensions = 2
mutation_rate = 0.1
crossover_rate = 0.7
max_generations = 50

# Running the memetic algorithm
ma = MemeticAlgorithm(pop_size, dimensions, mutation_rate, crossover_rate, max_generations)
best_solution, best_fitness = ma.run()

# Animation to show the best solution over generations
fig, ax = plt.subplots()
(line,) = ax.plot([], [], lw=2)


def init():
    ax.set_xlim(0, max_generations)
    ax.set_ylim(0, max(best_fitness, max(ma.fitness_history)))
    return (line,)


def update(frame):
    line.set_data(range(frame + 1), ma.fitness_history[: frame + 1])
    return (line,)


ani = animation.FuncAnimation(fig, update, frames=max_generations, init_func=init, blit=True)


# Displaying the animation
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Best Solution Over Generations")
plt.show()

# Output the best solution and its fitness
best_solution, best_fitness
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
