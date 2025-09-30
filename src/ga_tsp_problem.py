import os
import math
import json
import random
import time
import itertools
import numpy as np
import pandas as pd
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

def ninja_turtles(route, mutation_rate=0.01):
    route = route[:]
    for i in range(len(route)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(route)-1)
            route[i], route[j] = route[j], route[i]
    return route

def bright_future(population, cities, elite_size=1, mutation_rate=0.01):
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

    return best_route, best_distance, progress, cities

def nearest_neighbor(cities, start_city=1):
    unvisited = set(cities.keys())
    route = [start_city]
    unvisited.remove(start_city)

    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda c: euclid_dist(cities[last], cities[c]))
        route.append(next_city)
        unvisited.remove(next_city)

    return route, route_dist(route, cities)

def plot_convergence(progress, label, filename=None):
    plt.plot(progress, label=label)
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()


def plot_all_convergences(all_progress, filename="all_convergences.png"):
    plt.figure(figsize=(8,6))
    for label, progress in all_progress:
        plt.plot(progress, label=label)
    plt.title("Convergence of GA with Different Parameters")
    plt.xlabel("Generation")
    plt.ylabel("Best Distance")
    plt.legend()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()


def plot_route(cities, route, filename=None, title="Best Route"):
    x = [cities[city][0] for city in route] + [cities[route[0]][0]]
    y = [cities[city][1] for city in route] + [cities[route[0]][1]]

    plt.figure(figsize=(6,6))
    plt.scatter(x, y, c="red")
    plt.plot(x, y, c="blue", linewidth=1.2)

    for i, city in enumerate(route):
        plt.text(cities[city][0], cities[city][1], str(city), fontsize=6)

    plt.title(title)
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def plot_boxplot(all_results, labels, filename="boxplot.png"):
    plt.figure(figsize=(8,6))
    plt.boxplot(all_results, labels=labels)
    plt.ylabel("Best Distance")
    plt.title("GA Performance Variability Across Runs")
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.close()


def run_multiple(filename, pop_size, mutation_rate, generations, runs=10):
    distances = []
    runtimes = []
    cities = load_cities(filename)
    best_route = None

    for r in range(runs):
        start = time.time()
        route, dist, _, _ = genetic_algorithm(
            filename, pop_size=pop_size, generations=generations, mutation_rate=mutation_rate
        )
        runtime = time.time() - start
        distances.append(dist)
        runtimes.append(runtime)

        if best_route is None or dist < min(distances):
            best_route = route

    stats = {
        "mean_distance": np.mean(distances),
        "std_distance": np.std(distances),
        "best_distance": np.min(distances),
        "worst_distance": np.max(distances),
        "mean_runtime": np.mean(runtimes),
    }
    return stats, distances, best_route, cities

def run_full_experiments():
    tsp_files = {
        "berlin52": "../resources/tsp/berlin52.json",
        "a280": "../resources/tsp/a280.json",
        "pcb442": "../resources/tsp/pcb442.json"
    }

    results = []

    for name, file in tsp_files.items():
        print(f"\nRunning experiments on {name}...")

        cities = load_cities(file)
        nn_route, nn_dist = nearest_neighbor(cities, start_city=1)
        results.append({
            "instance": name,
            "method": "nearest_neighbor",
            "best_distance": nn_dist,
            "runtime": 0
        })
        plot_route(cities, nn_route, filename=f"{name}_nearest_neighbor.png", title=f"{name} - NN Route")

        all_results = []
        labels = []
        for mut in [0.01, 0.05]:
            stats, distances, best_route, cities = run_multiple(file, 200, mut, 500, runs=10)
            results.append({
                "instance": name,
                "method": "genetic_algorithm",
                "mutation_rate": mut,
                **stats
            })
            all_results.append(distances)
            labels.append(f"mut={mut}")
            plot_route(cities, best_route, filename=f"{name}_ga_mut{mut}.png", title=f"{name} - GA mut={mut}")

        plot_boxplot(all_results, labels, filename=f"{name}_boxplot.png")

    df = pd.DataFrame(results)
    df.to_csv("final_experiment_results.csv", index=False)
    print("\nAll experiments completed. Results saved to final_experiment_results.csv")
    return df

if __name__ == "__main__":
    df = run_full_experiments()
    print(df)

