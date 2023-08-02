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



Examples
========



Typical Behaviour
=================



Final Notes
===========



For Next Class
==============

* TBD