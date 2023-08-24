***********************************
Selection and Population Management
***********************************

* One of the main driving forces of evolutionary computation algorithms is the variation operators
* Another major driving force is the selection strategy

    * This determines an individual's ability to survive and have offspring based on their fitness values


* Selection is based on the *relative* fitness values of the individual
* It works independently from the actual problem and representation



Generational vs. Steady State
=============================

* All the algorithms provided so far have been implemented as a generational algorithm

    * A whole new population is created based on the current population
    * The new population becomes the current population
    * The population size remains the same
    * There are very discrete transitions between generations


* With the generational algorithm, depending on how the genetic operators are applied, the new population is filled with

    * Copies of unchanged selected chromosomes
    * Mutated selected chromosomes
    * Offspring resulting from crossover on selected chromosomes


* On the other hand, steady state algorithms provide a more continuous type of evolution

    * Not as clear discrete transitions between generations


* With steady state

    * Given a single population of size :math:`\mu`
    * Select some number of chromosomes :math:`\lambda` and apply the variation operators to produce the offspring
    * Replace :math:`\lambda` chromosomes in the population with the offspring


* The *generational gap* is the proportion of the the population that was replaced

    * :math:`\frac{\lambda}{\mu}`


* If the number of chromosomes selected is equal to the population size, it is equivalent to a generational algorithm

    * If :math:`\lambda = \mu`
    * When the generational gap is :math:`\frac{\lambda}{\mu} = 1`


* With a generational algorithm, the whole population is replaced
* But with a generational gap less than one, there needs to be another selection mechanism for replacement

    * Determining which candidate solutions of the population are to be replaced with the :math:`\lambda` offspring


Tournament Selection
====================

* Two very basic selections *could* be implemented

#. Uniform selection

    * Each chromosome has an equal chance at being selected

        * :math:`p(i) = \frac{1}{\mu}`, where :math:`p(i)` is the probability of an individual chromosome being selected

    * Some forms of evolutionary computation use this selection exclusively
    * However, in general, it's not going to perform well as there is nothing guiding the search

        * The algorithm will not converge


#. Select the top chromosomes only and apply the genetic operators

    * As already seen, this will not perform well as the population will converge too quickly on some local optimum


* An alternative highly effective selection is to go somewhere in between these ideas
* This is where tournament selection comes in

    * Randomly pick a subset of :math:`k` chromosomes from the population
    * Select the best of these :math:`k` chromosomes


.. figure:: tournament_selection.png
    :width: 600 px
    :align: center
    :target: https://www.tutorialspoint.com/genetic_algorithms/genetic_algorithms_parent_selection.htm

    Tournament selection being performed on a population of size 13. Here, :math:`k = 3`, meaning three chromosomes were
    selected at random. Of the three, the candidate solution with the highest fitness is then returned as the selected
    chromosome.


* The value of :math:`k` is typically kept low, but can be adjusted as needed

    * If :math:`k = 1`, this would be the same as a uniform selection
    * If :math:`k = \mu`, this would be the same as always selecting the best



Fitness Proportional Selection
==============================



Rank Based Selection
====================



Survivor Selection
==================



Selection Pressure
==================



Diversity
=========



Novelty
=======



For Next Class
==============

* TBD
