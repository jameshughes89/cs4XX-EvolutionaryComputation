**********************************
:math:`n` Queens Genetic Algorithm
**********************************

* The purpose of this topic is to emphasize the similarities between genetic algorithm implementations
* Although the first genetic algorithm implementation was solving a different problem, much of the algorithm is the same



Problem
=======

* The optimization version of the :math:`n` queens problem is going to be used

    * Given an :math:`n \times n` chess board
    * Place :math:`n` queens on the chess board
    * While minimizing the number of conflicting/attacking queens


* In other words, minimize the number of queens in the same row, column, or diagonal


.. figure:: ../representation/10_queens.png
    :width: 300 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Eight_queens_puzzle

    A configuration of :math:`10` queens on a :math:`10 \times 10` chess board with zero conflicts. This would be an
    optimal solution where :math:`n=10`.


* The reason the optimization version of the problem is being used is because it has a gradient for the search to follow
* The all or nothing (valid configuration or not) version of the problem has no gradient

* The phenotype space (problem space) includes all possible configurations of the :math:`n` queens on an :math:`n \times n` board

    * Assuming queens are not allowed on the same square, this is :math:`n \times n \choose n`


* However, as previously discussed, by using a permutation encoding, the genotype space (search space) is only :math:`n!`



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
    * :download:`n Queens GA </../src/ga_n_queens.py>`


