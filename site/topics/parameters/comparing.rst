************************************
What Comparing Distributions *Means*
************************************

* Given two evolutionary computation instances, how does one determine which is *better*?


Random Variables
================

.. warning::

    The content within this topic is kept at a high level and deliberately skips some formalisms and rigor. For the
    purpose of this course, the level of detail provided should be sufficient.


* Consider a random variable as some phenomenon that can be observed
* When observing the random variable, some quantitative measurement can be taken

    * The time it takes to recover from the flu
    * The amount of nuts a squirrel buries a day
    * The number of people with blond hair that walk by this building between 10am -- 11am on Tuesdays
    * The best fitness value of a genetic algorithm run


* Whatever the measurement is, they can be recorded and represented as distributions
* Consider the following two random variables

.. figure:: random_variable_1.png
    :width: 666 px
    :align: center

    Output of some random variable represented as a box. The data is shown as a list of numbers and as a distribution.
    A total of 50 data points were observed and recorded.


.. figure:: random_variable_2.png
    :width: 666 px
    :align: center

    Output of another random variable represented as a box. The data is shown as a list of numbers and as a
    distribution. A total of 50 data points were observed and recorded.


* Regardless of what these random variables are, one may wonder, *are these random variables actually different*?

    * If considering the flu recovery time

        * The random variables may be recovery times of two different groups of people
        * Does one group recover faster?


    * With the squirrels, does one squirrel bury more nuts in a day than the other?
    * Does one year have more blond people walking past the building on Tuesdays from 10am -- 11am?
    * Does one evolutionary computation algorithm implementation perform better than another?


.. figure:: random_variables_together.png
    :width: 666 px
    :align: center

    The two random variables' measurements plotted against each other.


* When visually analyzing the above comparison of the two random variables, there does appear to be a difference

    * But the data is clearly noisy
    * A range of values are obtained for each random variable
    * And there are only 50 observations of each random variable


* It is difficult to say if these random variables are truly producing different distributions

    * They may effectively be the same
    * The two groups do not take different amounts of time to recover from the flu
    * The squirrel I named Jimbo does not actually bury more nuts than the squirrel I named Sir Lora
    * There really isn't more blond people this year vs. last
    * My algorithm isn't really performing better than the next persons'



Example --- Drug Trial
======================


Null Hypothesis
---------------

* Always start by assuming that there is no real difference
* This is called the *Null Hypothesis*

* It may feel like an arbitrary position to take, but with this assumption, it allows one to start to form an argument

#. Assume the drug has no actual impact on the recovery time
#. If the drug has no impact, then it would be like both groups had the placebo
#. If both groups had the placebo, it really would not have mattered which person was assigned to which group
#. Thus, it should be possible to assign each individual and their corresponding recovery time to one of the two groups randomly
#. The resulting distributions should be similar


Permutation/Randomization Test
------------------------------


Interpreting Results
--------------------



For Next Class
==============

* TBD