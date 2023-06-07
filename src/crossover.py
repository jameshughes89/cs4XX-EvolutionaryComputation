def order_crossover(parent_1: list, parent_2: list, start_index: int, end_index: int) -> tuple[list, list]:
    """
    Order crossover. All elements between the two indices are moved to the children and the remaining missing elements
    are copied in the order that they appear in the other parent. Copying starts at end_index and returns to index zero
    when the end of the chromosome is hit. For example, indices of 2 and 5, [0,1,2,3,4,5,6], [4,6,3,5,2,0,1] ->
    [?,?,2,3,4,?,?], [?,?,3,5,2,?,?] -> [6,5,2,3,4,0,1], [1,4,3,5,2,6,0]. Out of order indices, indices with a
    difference of 0, and indices covering the whole length of the chromosome are allowed, but result in no change.

    :param parent_1: Chromosome to be used in crossover
    :param parent_2: Chromosome to be used in crossover
    :param start_index: Starting index of copied segment
    :param end_index: Ending index of copied segment (excluded in segment)
    :return: The two chromosomes after the crossover is applied
    :raises ValueError: If the parents are not the same length of if an index is out-of-bounds
    """

    def copy_missing_elements(parent: list, child: list, start_index: int, end_index: int) -> list:
        """
        Copy the missing elements from the other parent into the child. Elements are copied in order that they appear
        in the parent, starting at the end index, and looping to index 0 where necessary.

        :param parent: Chromosome to copy missing elements from
        :param child: Chromosome to have missing elements copied too
        :param start_index: Starting index of copied segment (where to stop copying missing elements to)
        :param end_index: Ending index of copied segment (where to start copying missing elements from)
        :return: child chromosome with the missing elements copied
        """
        source_index = end_index % len(parent_1)
        target_index = end_index % len(parent_1)
        while target_index != start_index:
            if parent[source_index] not in child[start_index:end_index]:
                child[target_index] = parent[source_index]
                target_index = (target_index + 1) % len(parent_1)
            source_index = (source_index + 1) % len(parent_1)
        return child

    if len(parent_1) != len(parent_2):
        raise ValueError(f"chromosomes must be the same length: {len(parent_1)}, {len(parent_2)}")
    if start_index < 0 or end_index < 0 or start_index > len(parent_1) - 1 or end_index > len(parent_1):
        raise ValueError(f"Index out-of-bounds: {start_index}, {end_index}")
    child_1 = parent_1[:]
    child_2 = parent_2[:]
    if start_index > end_index:
        return child_1, child_2
    child_1 = copy_missing_elements(parent_2, child_1, start_index, end_index)
    child_2 = copy_missing_elements(parent_1, child_2, start_index, end_index)
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
