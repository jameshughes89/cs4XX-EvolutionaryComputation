def bit_flip_mutation(parent: list, index: int) -> list:
    """
    Bit flip mutation. Flip the bit at the specified index. In other words, if the bit is a 0, change it to be a 1, and
    if the bit is a 1, change it to be a 0. For example, with mutation index of 2, [0,0,0,0,0] -> [0,0,1,0,0].

    :param parent: Chromosome to be mutated
    :param index: Index of the bit to be flipped
    :return: The chromosome after the mutation is applied
    :raises ValueError: If the index is out-of-bounds
    """
    if index < 0 or index > len(parent) - 1:
        raise ValueError(f"Index out-of-bounds: {index}")
    child = parent[:]
    child[index] = (child[index] + 1) % 2
    return child


def inversion_mutation(parent: list, start_index: int, end_index: int) -> list:
    """
    Inversion mutation. Reverse the order of elements between the specified indices. The end index is not included in
    the reversal. For example, with starting and ending indices of 1 and 4, [0,1,2,3,4] -> [0,3,2,1,4]. Out of order
    indices, indices with a difference of 0, and indices with a difference 1 are allowed, but result in no change.

    :param parent: Chromosome to be mutated
    :param start_index: Starting index of the inversion mutation
    :param end_index: Ending index of the inversion mutation (excluded in reversal)
    :return: The chromosome after the mutation is applied
    :raises ValueError: If either index is out-of-bounds
    """
    if start_index < 0 or end_index < 0 or start_index > len(parent) or end_index > len(parent):
        raise ValueError(f"Index out-of-bounds: {start_index}, {end_index}")

    child = parent[:]
    child[start_index:end_index] = child[start_index:end_index][::-1]
    return child


def swap_mutation(parent:list, index_1: int, index_2: int) -> list:
    """
    Swap mutation. Swap the values between the two specified indices. For example, with swap indices of 0 and 3,
    [0, 1, 2, 3, 4] -> [3, 1, 2, 0, 4]. Providing the same index for both index values results in no change.

    :param parent: Chromosome to be mutated
    :param index_1: Index to be swapped with index_2
    :param index_2: Index to be swapped with index_1
    :return: The chromosome after the mutation is applied
    :raises ValueError: If either index is out-of-bounds
    """
    if index_1 < 0 or index_2 < 0 or index_1 > len(parent) - 1 or index_2 > len(parent) - 1:
        raise ValueError(f"Index out-of-bounds: {index_1}, {index_2}")
    child = parent[:]
    child[index_1], child[index_2] = child[index_2], child[index_1]
    return child