def roulette_wheel_selection(population: list, population_fitness: list, pill_landing: float) -> list:
    """
    Select a chromosome based on where the roulette wheel's ball (pill) lands. The probability of a given chromosome
    being selected is proportional to its fitness value.

    :param population: Population of chromosomes to select from
    :param population_fitness: Fitness values of the population
    :param pill_landing: Floating point Value between [0, 1) indicating where the pill lands
    :return: A copy of the selected chromosome
    :raises ValueError: If pill_landing is not between [0, 1) or if the population's fitness totals to 0
    """
    if pill_landing < 0 or pill_landing >= 1:
        raise ValueError(f"pill_landing must be between [0, 1): {pill_landing}")
    if sum(population_fitness) == 0:
        raise ValueError(f"Total fitness of population is 0")
    pill_landing_scaled = pill_landing * sum(population_fitness)
    cumulative_sum = [sum(population_fitness[: i + 1]) for i in range(len(population_fitness))]
    for i, candidate_probability_edge in enumerate(cumulative_sum):
        if pill_landing_scaled < candidate_probability_edge:
            return population[i][:]


def tournament_selection(population: list, population_fitness: list, selected_indices: list[int]) -> list:
    """
    Select the chromosome with the maximum fitness value of the chromosomes in the tournament. The chromosomes in the
    tournament if its index is contained within the selected_indices list.

    :param population: Population of chromosomes to select from
    :param population_fitness: Fitness values of the population
    :param selected_indices: List of indices in the tournament
    :return: A copy of the selected chromosome
    :raises ValueError: If the list of selected indices is empty or contains an out-of-bounds index
    """
    if len(selected_indices) == 0:
        raise ValueError(f"List of indices in the tournament must be non empty: {selected_indices}")
    for index in selected_indices:
        if index < 0 or index > len(population_fitness) - 1:
            raise ValueError(f"List of indices in the tournament contains out-of-bounds index: {index}")
    max_value = 0
    max_index = 0
    for index in selected_indices:
        if population_fitness[index] > max_value:
            max_value = population_fitness[index]
            max_index = index
    return population[max_index][:]
