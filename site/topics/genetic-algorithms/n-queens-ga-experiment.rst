*********************************************************
Experimenting with the :math:`n` Queens Genetic Algorithm
*********************************************************



Run Multiple Times and Plot
===========================

#. If not done already, download the

    * :download:`Selection Script </../src/selection.py>`
    * :download:`Crossover Script </../src/crossover.py>`
    * :download:`Mutation Script </../src/mutation.py>`
    * :download:`n Queens GA </../src/ga_n_queens.py>`


#. Get the :math:`n` queens genetic algorithm running

    * Play around with the hyperparameters
    * Try to make the problem more difficult by increasing the value of :math:`n`


#. Create a learning curve plot

    * See the bitstring genetic algorithm for an example of how this was done


.. figure:: fitness_over_time_nqueens.png
    :width: 500 px
    :align: center

    Learning curve for some run of the :math:`n` queens genetic algorithm. This plot is for a run where
    :math:`n=20`, the population size was 100, the number of generations was 250, and a tournament size of 2. Since this
    is a minimization problem, lower fitness values are better.


Creating a Distribution
-----------------------

* Since genetic algorithms are stochastic processes, one should expect variability between runs

    * Every time the algorithm is run, different results will likely be obtained
    * This is to be expected given the amount of randomness involved

        * Initial population is created randomly
        * Selection is done randomly
        * Genetic operators are applied randomly
        * Genetic operators apply operations on random parts of the chromosomes


* This means it is not possible to run the algorithm once to truly measure its effectiveness

    * Learning curves are really only good for a quick eyeball test of the evolutionary learning process


* Instead, a distribution of results should be created along with summary statistics


#. Run the algorithm a total of :math:`100` times and save the best fitness result of each run

    * This will create a list of 100 fitness values


#. Calculate some simple summary statistics of the :math:`100` runs' results

    * Mean and/or median
    * Standard deviation and/or interquartile range
    * Anything else that could be interesting


#. Plot the fitness values in a histogram to see the distribution of results

    * `Use matplotlib's hist function <https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html>`_


.. figure:: distribution_of_results_nqueens.png
    :width: 500 px
    :align: center

    Distribution of the results of 100 runs of the :math:`n` queens genetic algorithm where :math:`n=20`, population
    size was 100, generations was 250, and a tournament size of 2.


#. To make the problem harder, repeat these questions for :math:`n=30`



Change Operators
================



Change Representation
=====================



Comparing Results
=================



For Next Class
==============

* TBD

