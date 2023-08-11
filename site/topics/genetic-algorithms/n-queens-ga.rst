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



Crossover
---------


Mutation
--------



Termination Requirement
=======================

* A generational GA will be used with a pre set number of generations defined by the hyperparameter ``GENERATIONS``

.. literalinclude:: /../src/ga_n_queens.py
    :language: python
    :lineno-match:
    :start-after: # [begin-generation-loop]
    :end-before: # [end-generation-loop]


* This loop performs

    * Evaluation
    * Selection
    * Crossover
    * Mutation


* Once the loop runs to completion, some final results are calculated and reported

    * Calculate the final populations fitness
    * Report the population and the population's fitness


.. literalinclude:: /../src/ga_n_queens.py
    :language: python
    :lineno-match:
    :start-after: # [begin-ending]
    :end-before: # [end-ending]



For Next Class
==============

* Download and look at

    * :download:`The Selection Script </../src/selection.py>`
    * :download:`The Crossover Script </../src/crossover.py>`
    * :download:`The Mutation Script </../src/mutation.py>`
    * :download:`n queens GA </../src/ga_n_queens.py>`


