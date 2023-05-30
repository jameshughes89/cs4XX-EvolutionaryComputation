"""
A simple genetic algorithm for maximizing an integer.

The integer is encoded as a bit string (list of 0s or 1s). Fitness is calculated with either the value of the bit string
or the number of 1s in the bit string (both are included for a comparison). Crossover is a single point crossover and
mutation is a bit flip mutation. 
"""