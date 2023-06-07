def order_crossover(parent_1: list, parent_2: list, start_index: int, end_index: int) -> tuple[list, list]:
    """
    Order crossover. All elements between the two indices are moved to the children and the remaining missing elements
    are copied in the order that they appear in the other parent. Copying starts at end_index and returns to index zero
    when the end of the chromosome is hit. For example, indices of 2 and 5, [0,1,2,3,4,5,6], [4,6,3,5,2,0,1] ->
    [?,?,2,3,4,?,?], [?,?,3,5,2,?,?] -> [6,5,2,3,4,0,1], [1,4,3,5,2,6,0]. Out of order indices and indices with a
    difference of 0 are allowed, but result in no change.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param start_index: Starting index of copied segment
    :param end_index: Ending index of copied segment (excluded in segment)
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if an index is out-of-bounds
    """
    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if start_index < 0 or end_index < 0 or start_index > len(parent_1) or end_index > len(parent_1):
        raise ValueError(f"Index out-of-bounds: {start_index}, {end_index}")
    child_1 = parent_1[:]
    source_index = end_index % len(parent_1)
    target_index = end_index % len(parent_1)
    while target_index != start_index:
        if parent_2[source_index] not in parent_1[start_index:end_index]:
            child_1[target_index] = parent_2[source_index]
            target_index = target_index % len(parent_1)
        source_index = source_index % len(parent_1)
    child_2 = parent_2[:]
    source_index = end_index % len(parent_1)
    target_index = end_index % len(parent_1)
    while target_index != start_index:
        if parent_1[source_index] not in parent_2[start_index:end_index]:
            child_2[target_index] = parent_1[source_index]
            target_index = target_index % len(parent_1)
        source_index = source_index % len(parent_1)
    return child_1, child_2


def one_point_crossover(parent_1: list, parent_2: list, index: int) -> tuple[list, list]:
    """
    One point crossover. All elements at and after the crossover index are swapped between the two chromosomes.
    For example, with a crossover index of 2, [0,0,0,0,0], [1,1,1,1,1] -> [0,0,1,1,1], [1,1,0,0,0]. A crossover index of
    0 is allowed, but results in all contents being swapped.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param index: The index of the starting point of where all elements will be swapped between chromosomes
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if the index is out-of-bounds
    """
    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if index < 0 or index > len(parent_1) - 1:
        raise ValueError(f"Index out-of-bounds: {index}")
    child_1 = parent_1[:]
    child_2 = parent_2[:]
    child_1[index:], child_2[index:] = child_2[index:], child_1[index:]
    return child_1, child_2
