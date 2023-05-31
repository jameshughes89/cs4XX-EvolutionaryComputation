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
