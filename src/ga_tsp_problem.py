import os
import time
import math
import json
import random
import matplotlib.pyplot as plt

def load_cities(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as f:
        data = json.load(f)
    coords = data["NODE_COORD_SECTION"]
    cities = {int(c[0]): (c[1], c[2]) for c in coords}
    return cities

def euclid_dist(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def route_dist(route, cities):
    dist = 0
    for i in range(len(route)):
        city_a = cities[route[i]]
        city_b = cities[route[(i + 1) % len(route)]] 
        dist += euclid_dist(city_a, city_b)
    return dist

def fitness(route, cities):
    return 1 / route_dist(route, cities)

def initial_population(pop_size, cities):
    city_ids = list(cities.keys())
    population = []
    for _ in range(pop_size):
        route = city_ids[:]
        random.shuffle(route)
        population.append(route)
    return population

def sorry_loosers(population, cities, k=5):
    fight = random.sample(population, k)
    fight.sort(key=lambda route: route_dist(route, cities))
    return fight[0]

def crossover(daddy, mommy):
    size = len(daddy)
    start, end = sorted(random.sample(range(size), 2))
    
    child = [None] * size
    child[start:end] = daddy[start:end]
    
    mommy_el = [city for city in mommy if city not in child]
    pos = 0
    for i in range(size):
        if child[i] is None:
            child[i] = mommy_el[pos]
            pos += 1
    return child

def ninja_turtles(route, mutation_rate = 0.01): # that's the mutation btw :D 
    route = route[:]
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route

def bright_future(population, cities, elite_size=1, mutation_rate=0.01): # the next gen :D
    population.sort(key=lambda r: route_dist(r, cities))
    natural_selection = population[:elite_size] 

    while len(natural_selection) < len(population):
        daddy = sorry_loosers(population, cities)
        mommy = sorry_loosers(population, cities)
        child = crossover(daddy, mommy)
        child = ninja_turtles(child, mutation_rate)
        natural_selection.append(child)

    return natural_selection

def genetic_algorithm(filename, pop_size=100, generations=500, mutation_rate=0.01):
    cities = load_cities(filename)
    population = initial_population(pop_size, cities)

    best_route = min(population, key=lambda r: route_dist(r, cities))
    best_distance = route_dist(best_route, cities)

    progress = [best_distance]  

    for gen in range(generations):
        population = bright_future(population, cities, elite_size=1, mutation_rate=mutation_rate)
        current_best = min(population, key=lambda r: route_dist(r, cities))
        current_distance = route_dist(current_best, cities)

        if current_distance < best_distance:
            best_route, best_distance = current_best, current_distance

        progress.append(best_distance)

        if gen % 50 == 0:
            print(f"Gen {gen}: Best distance = {best_distance:.2f}")

    return best_route, best_distance, progress, cities

def plot_route(cities, route, filename="best_route.png"):
    x = [cities[city][0] for city in route] + [cities[route[0]][0]]
    y = [cities[city][1] for city in route] + [cities[route[0]][1]]
    plt.figure(figsize=(8,6))
    plt.plot(x, y, 'o-r')
    for i, city in enumerate(route):
        plt.text(cities[city][0], cities[city][1], str(city))
    plt.title("Best Route Found")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()


def plot_convergence(progress, filename="convergence.png"):
    plt.figure(figsize=(8,6))
    plt.plot(progress, 'b-')
    plt.title("Convergence of GA")
    plt.xlabel("Generation")
    plt.ylabel("Distance")
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    start = time.time()
    best_route, best_distance, progress, cities = genetic_algorithm(
        "../resources/tsp/berlin52.json", pop_size=200, generations=500
    )
    runtime = time.time() - start
    
    print("Best Distance:", best_distance)
    plot_convergence(progress, "convergence.png")
    plot_route(cities, best_route, "best_route.png")
