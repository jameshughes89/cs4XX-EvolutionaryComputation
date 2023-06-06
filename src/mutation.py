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
    """
    if start_index < 0 or end_index < 0 or start_index > len(parent) or end_index > len(parent):
        raise ValueError(f"Index out-of-bounds: {start_index}, {end_index}")

    child = parent[:]
    child[start_index:end_index] = child[start_index:end_index][::-1]
    return child
