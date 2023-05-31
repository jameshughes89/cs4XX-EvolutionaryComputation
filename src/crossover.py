def one_point_crossover(parent_1: list, parent_2: list, crossover_point: int) -> tuple[list, list]:
    """
    One point crossover. All elements at and after the crossover point are swapped between the two chromosomes.
    For example, with a crossover point of 2, [0,0,0,0,0], [1,1,1,1,1] -> [0,0,1,1,1], [1,1,0,0,0]. A crossover point of
    0 is allowed, but results in all contents being swapped.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param crossover_point: The index of the starting point of where all elements will be swapped between chromosomes
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if the crossover point is out-of-bounds
    """
    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if crossover_point < 0 or crossover_point > len(parent_1) - 1:
        raise ValueError(f"crossover_point out-of-bounds: {crossover_point}")
    child_1 = parent_1[:]
    child_2 = parent_2[:]
    child_1[crossover_point:], child_2[crossover_point:] = child_2[crossover_point:], child_1[crossover_point:]
    return child_1, child_2
