********
Problems
********

* The maximization of the decimal integer value of an unsigned binary number was a *toy problem*

    * It is a trivial problem that, in practice, one would not use evolutionary computation for


* Evolutionary computation is typically used for problems with no known reasonable approach to address

    * It's a strategy to be used as a last resort
    * It is computationally expensive
    * It's often harder to understand compared to other algorithms
    * Depending on the problem, it is notorious for overfitting


* For learning purposes, classic toy problems will be used in this course
* But it is important to know which types of problems evolutionary computation is appropriate for



Systems
=======

.. figure:: system_box.png
    :width: 500 px
    :align: center

    Abstract representation of a general system. Systems typically receive some input, perform some function, and
    produce some form of output.


* Above is a simple black-box representation is a system
* The system receives some number of inputs
* The system performs some operation on the input
* The system produces some form of output

* Thinking of a system in this way helps distinguish the three important components

* For concrete examples, consider

    * Calculating a grocery bill

        * Input --- Prices of the items being purchased
        * Model --- Sum the prices plus a sales tax calculation
        * Output --- A grocery bill


    * Designing an aircraft wing

        * Input --- Shape of the wing
        * Model --- Equations of complex fluid dynamics
        * Output --- Estimates of drag and lift


    * Photosynthesis

        * Input --- Light, carbon dioxide, and water
        * Model --- Light reactions and the Calvin Cycle
        * Output --- Oxygen and sugar


    * Calculating the time it takes to drive to work

        * Input --- Route taken
        * Model --- Spacetime
        * Output --- Time taken



Optimization
------------

.. figure:: system_optimization.png
    :width: 500 px
    :align: center

    Given a system, if the goal is to find the best set of inputs, then it is called an optimization problem.


* Best path to work



Modelling
---------

.. figure:: system_modelling.png
    :width: 500 px
    :align: center

    Given a system, if the goal is to define the functionality and processes to produce the output, then it is called
    modelling.


* Writing software




Simulation
----------

.. figure:: system_simulation.png
    :width: 500 px
    :align: center

    Given a system, if the goal is to know the output of applying some input to a model, then it is called simulation.


* Aircraft wing design

    * Can kinda' depend though as optimization could be just a bunch of simulations
    * Maybe a warning?



Search Problems
===============


Optimization vs Constraints
===========================


Hardness
========


Continuous vs Discrete
----------------------


What to Know About Hardness
---------------------------


For Next Class
==============

* TBD