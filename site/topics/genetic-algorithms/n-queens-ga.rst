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

* The randomly generated population is not likely to be particularly good
* However, some will probably be better than others
* A fitness function will be used to measure the effectiveness of each chromosome

* The fitness function will count the number of conflicting queens
* Each pair of conflicting queens will only be counted once

* With the representation used, it's not possible for two queens to be in the same row or column
* Thus, only the diagonals need to be checked

.. literalinclude:: /../src/attacking_fitness.py
    :language: python
    :lineno-match:
    :pyobject: value_fitness


* For each queen, check the up and down diagonals to the right

    * There is no need to check to the left as any conflict to the left would already be counted


* The basic idea here is

    * Given a queen at index ``attacker_column`` with value ``attacker_row``
    * In order for a queen ``offset`` indices away to be in the same diagonal
    * It **must** be in the row ``attacker_row - offset`` or ``attacker_row + offset``


.. figure:: 8_queens_conflicts.png
    :width: 250 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Eight_queens_puzzle

    :math:`8 \times 8` chess board configuration with 4 conflicts. Only :math:`5` queens are shown here for
    demonstration purposes.


* Consider the above figure and the chromosome ``<? 6, 3, 4, 0, ?, 1, ?>

    * The questionmarks repreesnt irrelevant values for this example


* When evaluating the queens from left to right

    * The queen at index ``1`` has a value of ``6`` and conflicts with two queens

        * It conflicts with the queen at index ``3``

            * The offset is ``2`` and the value at index ``1`` equals the value at index ``3`` minus the offset ``2``
            * ``6 - 2 == 4``


        * It also conflicts with the queen at index ``6``

            * The offset is ``5`` and the value at index ``6`` equals the value at index ``6`` minus the offset ``5``
            * ``6 - 5 == 1``


    * The queen at index ``2`` also has a conflict with the queen at index ``3``

        * The offset is ``1`` and the value at index ``2`` equals the vlaue at index ``3`` plus the offset ``1``
        * ``3 + 1 == 4``


    * Lastly, the queen at index ``3`` conflicts with the queen at index ``6``

        * ``4  - 3 == 1``


    * As mentioned above, there is no need to look to the left of any queen as those conflicts would already be counted

        * For example, the queen at index ``6``\s conflicts were already counted



* With this fitness function, the fitness of each candidate solution within the population can be calculated and stored

.. literalinclude:: /../src/ga_n_queens.py
    :language: python
    :lineno-match:
    :start-after: # [begin-evaluation]
    :end-before: # [end-evaluation]



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
    * :download:`n queens GA </../src/ga_n_queens.py>`


