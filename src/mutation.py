def bit_flip_mutation(parent: list, mutation_point: int) -> list:
    """
    Bit flip mutation. Flip the bit at the specified index. In other words, if the bit is a 0, change it to be a 1, and
    if the bit is a 1, change it to be a 0. For example, with mutation point of 2, [0,0,0,0,0] -> [0,0,1,0,0].

    :param parent: Chromosome to be mutated
    :param mutation_point: Index of the bit to be flipped
    :return: The chromosome after the mutation is applied
    :raises ValueError: If the mutation point is out of bounds
    """
    if mutation_point < 0 or mutation_point > len(parent) - 1:
        raise ValueError(f"mutation_point out of bounds: {mutation_point}")
    child = parent[:]
    child[mutation_point] = (child[mutation_point] + 1) % 2
    return child
