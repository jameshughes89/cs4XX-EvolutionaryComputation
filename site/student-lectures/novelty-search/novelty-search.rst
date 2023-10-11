**************
Novelty Search
**************



What is it?
===========

* It's super cool, i swear!


Ho to do it
===========

* Consider a drug trial
* A group of 50 people is given a new drug that is intended to reduce the recovery time of the flu
* Another group is given a placebo
* No one in either group knows if they are given the new drug or the placebo

* Here, the random variables are the two groups and the observations are the recovery times of the people in each group

    * Further, the recovery time is itself a random variable
    * This is the property/characteristic trying to be understood


.. figure:: the_name_of_my_fig.png
    :width: 500 px
    :align: center

    This is a caption     


* With the above example

    * The average recovery time for the placebo group was roughly 15.4 days
    * The average recovery time for the drug group was roughly 13.8 days
    * The drug group recovered, on average, 1.6 days faster


* One may be tempted to conclude that the drug clearly works
* However, the average recovery time is a summary statistic of a distribution
* When observing the distributions, it is clear that there is more nuance

* Additionally, there were only 50 observations from each group
* Every individual is different and every observation is different
* If I were to do this again, the distributions would look different
* What are the odds that this result just happened by chance?


Null Hypothesis
---------------

* Always start by assuming that there is no real difference
* This is called the *Null Hypothesis*

* It may feel like an arbitrary position to take, but with this assumption, it allows one to start to form an argument

#. Assume the drug has no actual impact on the recovery time
#. If the drug has no impact, then it could be expected that the average recovery time would be no different than the placebo
#. If both groups had the placebo, it really would not have mattered which person was assigned to which group
#. Thus, it should be possible to assign each individual and their corresponding recovery time to one of the two groups randomly
#. Therefore, the difference in the average recovery times between the two randomly assigned groups would be an example of what one would get by dumb luck


Permutation/Randomization Test
------------------------------

* Assuming the null hypothesis
* Shuffling the groups once and calculating the difference between the group averages will give one example of a *chance* difference

* It is possible to generate all possible combinations of assigning the 100 people to two groups
* If all possible combinations are generated, all possible average *by chance* differences can be calculated

    * Although, in this example, there are a lot
    * A total of :math:`1.01 \times 10^{29}` combinations of splitting 100 people into two groups of 50
    * In cases where it is intractable to generate all combinations, simply generate some large number of combinations
    * Here, :math:`1,000,000` combinations will be generated


.. figure:: chance_average_group_differences.png
    :width: 500 px
    :align: center

    Distribution of the "by chance" average group differences after 1,000,000 shuffles of the two groups. This
    distribution is **not** the recovery times like in the above distributions.


Interpreting Results
--------------------

* The key question to ask now is, *how likely is it that the original observation actually happened by chance?*

.. figure:: chance_average_group_differences_with_observation.png
    :width: 500 px
    :align: center

    Original observed average group difference in recovery time between the drug group and the placebo group shown on
    the distribution of the chance average group differences. The number of chance observations with the same or lower
    recovery times than the originally observed will inform how likely our observation could happen by chance.


* Of the :math:`1,000,000` combinations randomly generated
* There were :math:`205` with a by chance recovery time the same or better than the originally observed 1.6 days faster
* In other words, there is a 0.0205% chance that the original observation happened by dumb luck

    * :math:`\frac{205}{1000000} = 0.000205 = 0.0205\%`
    * There is a roughly one in 50,000 chance this would have happened by dumb luck


* This is where the idea of a probability value (p-value) comes in
* There is a 0.000205 probability that the drug's improved recovery time happened by chance


T-Tests and Mann-Whitney U tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The permutation test is explained to provide the intuition into what p-values actually mean
* In practice, using a t-test or Mann-Whitney U test is sufficient for this course



For Next Class
==============

* Although not entirely related, `check out 3 Blue 1 Brown's video on Bayes' Rule <https://www.youtube.com/watch?v=lG4VkPoG3ko>`_