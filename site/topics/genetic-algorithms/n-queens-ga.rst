**********************************
:math:`n` Queens Genetic Algorithm
**********************************

* The purpose of this topic is to emphasize the similarities between genetic algorithm implementations
* Although the first genetic algorithm implementation was solving a different problem, much of the algorithm is the same


Problem
=======



Initialization
==============

Representation
--------------

Population
----------



Evaluation
==========



Selection
=========



Variation Operators
===================

* Given the permutation representation, special considerations should be made when implementing the variation operators
* The operators should ensure the chromosome remain a permutation

    * Consider a one point crossover on permutations

    .. code-block:: text

               v                    v
        [0, 1, 2, 3, 4]      [0, 1, 2, 1, 0]
                         ->
        [4, 3, 2, 1, 0]      [4, 3, 2, 3, 4]
               ^                    ^


    * This crossover may destroy the fact that the chromosomes are permutations


Crossover
---------


Mutation
--------



Termination Requirement
=======================



For Next Class
==============

* Download and look at

    * :download:`The Selection Script </../src/selection.py>`
    * :download:`The Crossover Script </../src/crossover.py>`
    * :download:`The Mutation Script </../src/mutation.py>`
    * :download:`n queens GA </../src/ga_n_queens.py>`


