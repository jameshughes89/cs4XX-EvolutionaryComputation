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

* An *order crossover* is commonly used for permutation representations

* Keep all elements between two randomly selected indices

.. figure:: ../genetic-algorithms/order_crossover_1.png
    :width: 500 px
    :align: center

    Keep the segment of the chromosome between two arbitrarily selected indices. This only shows one of the two children
    that this crossover would produce.


* Then, copy the elements from chromosome :math:`A`, in order, if they do *not* appear in chromosome :math:`B`

    * Start copying from *after* the kept segment


.. figure:: ../genetic-algorithms/order_crossover_2.png
    :width: 500 px
    :align: center

    Copy the elements from the other parent, in order, starting after the kept segment. Only copy values that are not
    already contained within the child. Again, this only shows one of the two children this crossover would produce.


.. literalinclude:: /../src/crossover.py
    :language: python
    :lineno-match:
    :pyobject: order_crossover


Mutation
--------

* Similar to crossover, one must be careful with the choice of mutation when working with permutations
* Fortunately, swap mutation is a very simple mutation that is permutation safe

    * Select two indices and swap the values between them

.. figure:: ../genetic-algorithms/swap_mutation.png
    :width: 500 px
    :align: center

    Swap mutation on some chromosome. The values at indices ``1`` and ``4`` are swapped in this example.


.. literalinclude:: /../src/mutation.py
    :language: python
    :lineno-match:
    :pyobject: swap_mutation



Termination Requirement
=======================



For Next Class
==============

* Download and look at

    * :download:`The Selection Script </../src/selection.py>`
    * :download:`The Crossover Script </../src/crossover.py>`
    * :download:`The Mutation Script </../src/mutation.py>`
    * :download:`n queens GA </../src/ga_n_queens.py>`


