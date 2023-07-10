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
    only help with building the intuition around how GAs work.


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
* How do we start the problem?
   * Initialize population
   * ... and other parameters


Evaluation
==========
* What is a ``good'' solution
* How to weed out ``good'' from ``less-good''


Selection
=========
* How do we pick solutions to persist?


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


For Next Class
==============

* TBD

    * TBD
