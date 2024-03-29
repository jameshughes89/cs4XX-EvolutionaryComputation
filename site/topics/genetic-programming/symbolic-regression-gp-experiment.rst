**************************************
Experimenting with Symbolic Regression
**************************************

* The purpose of this topic is to

    * Gain more hands on experience working with a genetic programming
    * Think about multi-objective problems



Run on Multiple Instances
=========================

* `A total of 20 instances are made available on the GitHub repository <https://github.com/jameshughes89/cs4XX-EvolutionaryComputation/tree/main/resources/regression-data>`_
* All instances are made up of tabular data where the rows are observations and columns are the variables
* The dependant variable is always the last column
* Many of these instances are more than two or three dimensions, so visualizing and plotting the data may be difficult

* Each of these instances were generated by some function
* Further, normally distributed noise was added to each data point

* The goal is to find the function that was used to generate each instance



Language
========

* The language that is included in the provided code may not be sufficient to effectively model the data
* Try changing the language by adding or removing some operators
* Also consider adding floating point numbers as constants



Multi-Objective Problem
=======================

* A strategy for managing bloat is to add negative selection pressure to larger chromosomes

    * Given chromosomes with similar or identical fitness values, it is better to select those with smaller trees


* Try adding tree size as part of the fitness measure and see if this helps simplify the generated chromosomes

    * Going through DEAP's documentation will be helpful for learning how to do this

        * `Defining a fitness that has more than one objective <https://deap.readthedocs.io/en/master/tutorials/basic/part2.html#a-first-individual>`_
        * `Having a fitness function return multiple values <https://deap.readthedocs.io/en/master/tutorials/basic/part2.html#evaluation>`_



For Next Class
==============

* TBD


