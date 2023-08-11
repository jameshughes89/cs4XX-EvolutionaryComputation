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

* Before evolution can begin, an initial population of candidate solutions


Representation
--------------

* The permutation representation previously discussed will be used

    * A chromosome will be a list of length :math:`n`
    * Each of the :math:`n` indices correspond to each of the :math:`n` queens
    * Each index will be the queen's respective column in the chess board
    * The elements within the list will be a permutation of the integers between :math:`0` and :math:`n-1`
    * The value at each index will be the queen's respective row in the chess board


* Since the values and indices are unique, no two queens can be in the same row or column

* An example chromosome when :math:`n=8` is

    ``<0, 5, 7, 6, 3, 2, 1, 4>``


Population
----------

* A population is a list of chromosomes

    .. code-block:: text

        [<0, 5, 7, 6, 3, 2, 1, 4>,
         <4, 5, 2, 3, 6, 7, 1, 0>,
         <0, 1, 2, 3, 4, 5, 6, 7>,
         ...
         ...
         <4, 3, 2, 7, 6, 1, 0, 5>]



* The chromosomes, and thus the population, will be randomly generated for this implementation of a genetic algorithm

.. literalinclude:: /../src/ga_n_queens.py
    :language: python
    :lineno-match:
    :start-after: # [begin-initialization]
    :end-before: # [end-initialization]


* The number of chromosomes within the population is defined by a hyperparameter called ``POPULATION_SIZE``
* The length of the chromosomes will match the number of queens, which is defined by the hyperparameter ``N_QUEENS``
* The chromosomes are permutations of the sequence of integers from :math:`0` to :math:`n-1`

* Note that ``sample`` is from Python's ``random`` library

    * `It returns a k length list of unique elements chosen from a population sequence <https://docs.python.org/3/library/random.html#random.sample>`_



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


