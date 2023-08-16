*********************************************************
Experimenting with the :math:`n` Queens Genetic Algorithm
*********************************************************

* It is time to tinker with the provided :math:`n` queens genetic algorithm implementation
* The purpose of this is to

    * Gain more hands on experience working with a genetic algorithm
    * Implement different operators and see the impact of the changes
    * Implement a different representation to see how it impacts results
    * See how to start comparing results



Run Multiple Times and Plot
===========================

.. note::

    The easiest way to get the code up and running is to
    `fork <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_
    the github `repository <https://github.com/jameshughes89/cs4XX-EvolutionaryComputation>`_, download it, and run the
    setup described in the "README".

    Alternatively, the scripts can be downloaded individually to ``/src``, but this may require some additional setup for
    the dependencies. It is recommended to make a `virtual environment <https://docs.python.org/3/library/venv.html>`_
    and `download any required dependencies with pip <https://pypi.org/project/pip/>`_.


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
#. When happy with the results, save them somewhere to be used later for comparisons 



Change Operators
================

* For the following, try to be as creative as possible and feel free to try multiple ideas

    * It's always good to explore and tinker
    * It really does not matter how good or bad the results are in the end
    * If stuck, look up existing popular ideas for the operators to implement


* Additionally, test each change in isolation to simplify the analysis of the impact of the change

    * In other words, revert the previous changes before moving on to the next task


* Finally, run each 100 times and generate the summary statistics and distributions

    * Be sure to save the results somewhere for later comparisons


#. Change out the crossover operator for something else and run the experiments again
#. Change out the mutation operator for something else and run the experiments again
#. Change out the selection operator for something else and run the experiments again



Change Representation
=====================



Comparing Results
=================

* The summary statistics of a distribution of results is a great way for a quick perspective of the results
* Often, people will compare the summary statistics of two distributions to make a conclusion of what is *better*

    * If the results when using crossover X has a better mean than the results of crossover Y, then X is better, right?


* But in reality, this is a poor way to perform a comparison
* This is because, the goal is to compare the distribution of the results, not the summary statistics

* The simplest way to do this is to plot the distributions against each other and perform an eyeball test

.. figure:: distribution_of_results_nqueens.png
    :width: 500 px
    :align: center

    Comparison of two distribution of results of :math:`100` runs. These results were obtained by running the genetic
    algorithm as provided where :math:`n=20`, population size was 100, generations was 250, and a tournament size of 2.
    One run had a crossover rate of 70% and the other had a rate of 20%. It is clear, from this comparison, that using a
    crossover rate of 20% is superior.



Probability Value
-----------------

* The most correct way to compare is with a permutation/randomization test

    * This will be discussed briefly in a future topic
    * The idea of a permutation test is intuitive when related to what it means
    * Can get hairy


* More simply, use a t-test or MWU

    * t-test often requires assumptions that often do not hold
    * MWU is safe


Effect Size
-----------

* Effect size



For Next Class
==============

* TBD

