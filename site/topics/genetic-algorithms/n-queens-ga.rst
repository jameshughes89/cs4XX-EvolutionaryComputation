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

* Tournament selection will be used here

    * It's simple, and effective


.. literalinclude:: /../src/ga_n_queens.py
    :language: python
    :lineno-match:
    :start-after: # [begin-selection]
    :end-before: # [end-selection]


* Mind the use of the argument ``direction``

    * This indicates that chromosomes with *loser* fitness values are better
    * By default it assumes higher fitness is better


.. literalinclude:: /../src/selection.py
    :language: python
    :lineno-match:
    :pyobject: tournament_selection



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


