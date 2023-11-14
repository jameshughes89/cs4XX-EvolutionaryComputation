import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# Problem settings
def sum_equation(x):
    """Example equation: the sum of squares."""
    return sum([i**2 for i in x])


# Genetic Algorithm
class GeneticAlgorithm:
    def __init__(
        self, pop_size, dimensions, mutation_rate, crossover_rate, max_generations
    ):
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
        return sum_equation(solution)

    def select_parents(self):
        """Tournament selection"""
        parents = []
        for _ in range(self.pop_size):
            i, j = np.random.randint(0, self.pop_size, 2)
            if self.fitness(self.population[i]) < self.fitness(self.population[j]):
                parents.append(self.population[i])
            else:
                parents.append(self.population[j])
        return np.array(parents)

    def crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_rate:
            crossover_point = np.random.randint(1, self.dimensions)
            child1 = np.concatenate(
                [parent1[:crossover_point], parent2[crossover_point:]]
            )
            child2 = np.concatenate(
                [parent2[:crossover_point], parent1[crossover_point:]]
            )
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, solution):
        for i in range(self.dimensions):
            if np.random.rand() < self.mutation_rate:
                solution[i] += np.random.randn()
        return solution

    def run(self):
        for generation in range(self.max_generations):
            new_population = []
            parents = self.select_parents()
            for i in range(0, self.pop_size, 2):
                parent1, parent2 = parents[i], parents[i + 1]
                child1, child2 = self.crossover(parent1, parent2)
                child1 = self.mutate(child1)
                child2 = self.mutate(child2)
                new_population.extend([child1, child2])

            self.population = np.array(new_population)
            current_best = min(self.population, key=self.fitness)
            current_best_fitness = self.fitness(current_best)
            self.fitness_history.append(current_best_fitness)

            if current_best_fitness < self.best_fitness:
                self.best_solution = current_best
                self.best_fitness = current_best_fitness

        return self.best_solution, self.best_fitness


# Parameters for the genetic algorithm
pop_size = 50
dimensions = 2
mutation_rate = 0.1
crossover_rate = 0.7
max_generations = 50

# Running the genetic algorithm
ga = GeneticAlgorithm(
    pop_size, dimensions, mutation_rate, crossover_rate, max_generations
)
best_solution, best_fitness = ga.run()

# Animation to show the best solution over generations
fig, ax = plt.subplots()
(line,) = ax.plot([], [], lw=2)


def init():
    ax.set_xlim(0, max_generations)
    ax.set_ylim(0, max(best_fitness, max(ga.fitness_history)))
    return (line,)


def update(frame):
    line.set_data(range(frame + 1), ga.fitness_history[: frame + 1])
    return (line,)


ani = animation.FuncAnimation(
    fig, update, frames=max_generations, init_func=init, blit=True
)

# Displaying the animation
plt.xlabel("Generation")
plt.ylabel("Best Fitness")
plt.title("Best Solution Over Generations")
plt.show()


# Output the best solution and its fitness
print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)
