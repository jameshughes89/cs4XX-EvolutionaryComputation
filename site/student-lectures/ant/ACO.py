import random
import math

# Define parameters
n_cities = 5  # Number of cities
alpha = 1.0  # Pheromone importance
beta = 2.0  # Distance importance
rho = 0.1  # Pheromone evaporation rate
Q = 100  # Pheromone deposit constant
iterations = 100  # Number of iterations
ants_count = 10  # Number of ants

# Example distance matrix (symmetric)
distances = [
    [0, 10, 15, 20, 25],
    [10, 0, 35, 25, 30],
    [15, 35, 0, 30, 5],
    [20, 25, 30, 0, 15],
    [25, 30, 5, 15, 0]
]

# Initialize pheromone matrix
pheromones = [[1.0 for _ in range(n_cities)] for _ in range(n_cities)]


# Function to calculate the total distance of a tour
def calculate_total_distance(tour):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]  # Return to start
    return total_distance


# Function to update pheromones based on the ants' paths
def update_pheromones(pheromones, ants_paths, ants_distances):
    for i in range(n_cities):
        for j in range(n_cities):
            pheromones[i][j] *= (1 - rho)  # Evaporate pheromones

    for path, dist in zip(ants_paths, ants_distances):
        for i in range(len(path) - 1):
            pheromones[path[i]][path[i + 1]] += Q / dist  # Deposit pheromones

# [START SELECT PATH]
# Function to select the next city for an ant based on pheromone and distance
def select_next_city(current_city, visited_cities, pheromones, distances, alpha, beta):
    probabilities = []
    total = 0
    for city in range(n_cities):
        if city not in visited_cities:
            pheromone = pheromones[current_city][city] ** alpha
            distance = (1 / distances[current_city][city]) ** beta
            probability = pheromone * distance
            probabilities.append(probability)
            total += probability
        else:
            probabilities.append(0)

    # Normalize probabilities
    probabilities = [p / total for p in probabilities]

    # Select the next city based on probabilities
    next_city = random.choices(range(n_cities), probabilities)[0]
    return next_city
# [END SELECT PATH]

# ACO Algorithm
def aco_algorithm():
    best_path = None
    best_distance = float('inf')

    for _ in range(iterations):
        ants_paths = []
        ants_distances = []

        for _ in range(ants_count):
            visited_cities = [random.randint(0, n_cities - 1)]  # Start from a random city
            while len(visited_cities) < n_cities:
                current_city = visited_cities[-1]
                next_city = select_next_city(current_city, visited_cities, pheromones, distances, alpha, beta)
                visited_cities.append(next_city)

            total_distance = calculate_total_distance(visited_cities)
            ants_paths.append(visited_cities)
            ants_distances.append(total_distance)

            if total_distance < best_distance:
                best_distance = total_distance
                best_path = visited_cities

        # Update pheromones
        update_pheromones(pheromones, ants_paths, ants_distances)

    return best_path, best_distance


# Run the ACO algorithm
best_path, best_distance = aco_algorithm()
print("Best path:", best_path)
print("Best distance:", best_distance)
