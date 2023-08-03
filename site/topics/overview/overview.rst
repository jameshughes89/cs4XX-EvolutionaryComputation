********
Overview
********

* Given a population of individuals within an environment with limited resources
* Competition for those resources occurs
* This competition causes natural selection
* This causes the overall fitness of the population to rise

    * An evolutionary "arms race"


* In the context of Evolutionary Computation (EC)

    * Given some problem and a mechanism for measuring solution quality

        * The problem is the environment


    * Generate a fixed size population of solutions to the problem

        * The fixed sized population is the limited resource


    * Apply the quality measure to the solutions
    * More fit solutions reproduce to fill the next generation's population

        * More fit individuals compete better


.. figure:: ../intro/ec_idea.png
    :width: 500 px
    :align: center

    High-level idea of most evolutionary computation algorithms.


* There are two big forces at play

    #. Variation

        * Genetic operators like mutation and crossover
        * Increases population diversity
        * Pushes the population towards novelty


    #. Selection

        * Surviving within the population
        * Decreases population diversity
        * Pushes the population towards quality



Types of Evolutionary Computation
=================================

* Given how flexible the framework of EC is, there is a large and growing list of *types*
* Their differences often come down to specific details, their encodings, and types of problems they are designed for
* But they are all population-based iterative processes with selection and variation mechanisms

* Common popular EC algorithms are

    * Genetic Algorithms

        * Typically have a string or array/list encoding


    * Evolutionary Strategies

        * Works well with real numbers


    * Differential Evolution

        * Works well with real numbers
        * Does not use a gradient/problem does not need to be differentiable


    * Particle Swarm Optimization

        * Works well with real numbers


    * Evolutionary Programming

        * Evolves finite state machines


    * Genetic Programming

        * Evolves *programs*
        * Typically encoded as a tree structure



Components
==========

Representation
--------------


Fitness
-------


Population
----------


Selection
---------


Genetic Operators
-----------------



Example
=======

* Consider the :math:`n` queen problem

    * Place :math:`n` queens on an :math:`n \times n` chess board such that none can attack any other


.. figure:: ../representation/10_queens.png
    :width: 300 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Eight_queens_puzzle

    A valid configuration of :math:`10` queens on a :math:`10 \times 10` chess board. This particular configuration is
    called a "staircase solution".


* Consider what the parts of the GA would be for this problem


Representation
--------------

* The phenotype is the :math:`n \times n` chess board configuration of :math:`n` queens

* For the genotype, a 2D array encoding could be used

    * It would require an :math:`n \times n` array
    * :math:`n` cells in the array would be filled, representing the queen locations
    * This would be a very *direct* representation
    * It can represent all possible configurations


* Alternatively, a 1D array could be used

    * It would require an :math:`n` length array
    * Each value in the array could be a tuple representing the :math:`(x, y)` coordinate of each queen
    * This is still relatively direct, but does need a bit of translation to represent the phenotype
    * This can also represent all possible configurations


* The representation can be whatever one wants, but being clever about the encoding can have an impact on performance


Population
----------

* Assuming the use of the 2D array encoding, the population would be a collection of 2D arrays
* Alternatively, with the 1D array, the population would be a collection of 1D arrays
* Whatever encoding is used, the population would simply be a collection of coded values


Fitness
-------

* As discussed previously, there is value in turning the :math:`n` queens problem into an optimization problem

    * Instead of looking for a valid board configuration, minimize the number of conflicts
    * This provides a gradient


* An appropriate fitness function for this problem would be to count the number of conflicting queens
* How exactly this fitness value is calculated will depend on the encoding

* 2D array encoding

    * One way would be to look at each queen and check its rows, columns, and diagonals and count the conflicts


* 1D array encoding

    * This one is not as straightforward
    * However, one could *translate* the :math:`(x, y)` coordinates into an :math:`n \times n` chess board
    * Then, perform the same fitness check as the 2D array encoding


Variation Operators
-------------------

* This will depend on the representation
* But ultimately the choice can be whatever, but it will impact performance

* 2D array encoding

    * For mutation, move one of the queens to some other spot on the chess board

    * For crossover, it is less obvious
    * Swapping half the boards could be problematic as it may result in the boards not having :math:`n` queens
    * Instead, perhaps select a subset of queens to swap between chromosomes


* 1D array encoding

    * For mutation, randomly replace one of the coordinates with a newly generated coordinate

    * For crossover, a single point crossover could work

        * Select an index and swap all contents between parents after that index


    * However, this could result in duplicate coordinates existing in a chromosome

        * We can't have two of the :math:`n` queens exist in the same space on the board
        * Although perhaps not ideal, this can be delt with by applying a fitness penalty if this happens


Selection
---------

* There are so many possibilities for selection
* For simplicity, tournament selection could be used

    * Randomly select :math:`k` candidate solutions
    * Select the best candidate solution of the :math:`k` based on fitness
    * Repeat


* If a generational algorithm is used, this would be repeated until the new population is full
* If a steady state algorithm is used, chromosomes would need to be selected for replacement

    * There are many ways this could be done

        * Replace based on age
        * Replace based on fitness
        * Replace randomly


Initialization and Termination
------------------------------

* For initialization, for both encodings, randomly generate the chromosomes would work
* For termination, just run for some predetermined number of generations



Typical Behaviour
=================



Final Notes
===========



For Next Class
==============

* TBD