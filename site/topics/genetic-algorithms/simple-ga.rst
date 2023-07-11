********************************
Implementing a Genetic Algorithm
********************************

* The purpose of this topic is to see a simple genetic algorithm (GA)
* Although simple, it includes all the necessary parts to make it a complete GA
* Despite never seeing a GA before, or knowing the intuition behind the underlying ideas, the topic should be manageable



Problem
=======

.. note::

    The problem being *solved* is deliberately kept very simple. This is because (a) the purpose of this topic is to
    see a working GA, not solve a complex problem, and (b) well understood problems are often much simpler to reason
    about. Knowing what a good/bad solution is, and having an idea of why certain solving strategies work or not, will
    help with building the intuition around how GAs work.


* The problem being solved is to maximize the integer value of an unsigned binary number

    * Find the largest binary number representable with :math:`n` bits


* Given this problem description, the best solution is obviously a string of :math:`n` ones
* Consider an example with :math:`n=10`, how would these candidate solutions be ranked in terms of *goodness*?

    * :math:`1111111111` (1023)
    * :math:`1011001001` (713)
    * :math:`0001111111` (127)
    * :math:`0000000000` (0)


* Thus, the GA being written will *evolve* bit strings to maximize the integer value of an unsigned binary number

* Realistically, one would not use a GA to solve such a problem

    * GAs are typically used for very challenging problems with no other effective means of solving


* However, this problem provides an opportunity to consider how the GA can and must work to find the best solution



Initialization
==============

* Before evolution can begin, an initial *population* of *candidate solutions* needs to be created
* A single candidate solution is a potential solution to the problem being solved
* For example, :math:`1011001001` is a valid candidate solution for finding the largest binary value where :math:`n=10`


Representation
--------------

* It is sometimes non-trivial to determine how a candidate solution should be represented, or encoded, in the program

    * An encoded candidate solution is called a *chromosome*


* For the integer maximization of an unsigned binary number, there are some obvious reasonable and simple encodings
* Here, a list of ``0``\s and ``1``\s will be used
* Thus, the candidate solution :math:`1011001001` can be encoded as the chromosome ``[1, 0, 1, 1, 0, 0, 1, 0, 0, 1]``

* A single chromosome can be created by generating random lists of ``0``\s and ``1``\s of some predetermined length

    * The example used here, the length was :math:`n=10`


Population
----------

* A population is a collection of candidate solutions
* A population can be created by creating a list of randomly generated chromosomes

* In this example, a single chromosome is a list of ``0``\s and ``1``\s

    ``[1, 0, 1, 1, 0, 0, 1, 0, 0, 1]``


* A population is a list of chromosomes

    .. code-block:: text

        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         ...
         ...
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 1]]


* The number of chromosomes within the population is defined by some hyperparameter
* Each chromosome is randomly generated
* Below is an example of how one could create a population for this problem in Python

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-initialization]
    :end-before: # [end-initialization]



Evaluation
==========

* After generating the population, the candidate solutions are often not particularly *good*
* However, some will likely be better than others
* Regardless, a mechanism for evaluating the quality, or *fitness*, of candidate solutions is needed
* This mechanism is called the *fitness function*

* Below is an example fitness function for this problem in Python

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :pyobject: value_fitness


* With this fitness function, the fitness of each candidate solution within the population can be calculated and stored

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-evaluation]
    :end-before: # [end-evaluation]



Selection
=========

* Ideally, more fit candidate solutions should be *more likely* to persist within the population

    * And less fit candidate solutions should be more likely to die off


* However, it is not as simple as always selecting the best candidate solutions

    * Doing so would cause the population to *converge* too early
    * This can result in finding sub-optimal solutions


* This is where it becomes important to think about the population, not individual candidate solutions
* The fitness function is a metric for the ultimate goal --- finding a *candidate solution* that best solves the problem
* But focusing on this metric is detrimental to the *population*
* Instead, the population should also emphasize *diversity*

* This can be done in any way someone wants

    * There are no hard rules on how selection is to be done


* A simple and popular selection technique is *tournament selection*

    * Randomly select a subset of chromosomes within the population
    * Select the best of the subset
    * Repeat until the next generation's population is full

.. literalinclude:: /../src/selection.py
    :language: python
    :lineno-match:
    :pyobject: tournament_selection


* This ``tournament_selection`` function returns a single chromosome
* This function must be run multiple times until the next generation's population is full

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-selection]
    :end-before: # [end-selection]


* In the above code, the list ``mating_pool`` will ultimately become the next generation's population



Variation Operators
===================

* Only having population of the same solutions is boring
* How to make different solutions
   * More fun?
   * Better ones?
   * Maybe both!!

* PROBLEM WITH ONLY CROSSOVER (no diversity)


Termination Requirement
=======================
* Don't have infinite resources to run EC forever
* Have to end loop somehow...



TODO
====

- plot
- play with hyperparams
- selection pressure (random vs always best)
- fitness variables
- invent your own stuff


For Next Class
==============

* TBD

    * TBD
