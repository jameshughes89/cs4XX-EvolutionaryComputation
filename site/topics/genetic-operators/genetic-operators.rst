*****************
Genetic Operators
*****************

* Below is a collection of common genetic operators for broad types of representations

    * This is by no means exhaustive
    * Further, it should not be assumed that they are particularly effective
    * They are intended to provide foundational ideas 


* These operators focus on representations for genetic algorithms

    * The motivation for focusing on genetic algorithms is they are quite a general form of evolutionary computation


* Although common genetic operators are presented, being creative and trying to invent new operators is encouraged



Genetic Operators for Binary Representations
============================================

* Binary representations are those that only contain two values, which are typically 0s and 1s


Crossovers
----------

One Point Crossover
^^^^^^^^^^^^^^^^^^^

* Randomly select an index
* Exchange the elements between the chromosomes after that index
* This crossover is not particularly *destructive*

    * The amount in which the information within the chromosomes gets changed is low


* This crossover works well when element adjacency in the chromosome is important


.. figure:: one_point_crossover.png
    :width: 450 px
    :align: center

    Result of applying one point crossover on two chromosomes. This example has index 5 as the randomly selected
    crossover point, thus, all elements after index 5 are exchanged between the parent chromosomes. Although this
    example shows one parent containing only 0s and the other containing only 1s, this is not a requirement;
    the parents could contain both 0s and 1s.


:math:`n` Point Crossover
^^^^^^^^^^^^^^^^^^^^^^^^^

* Randomly select :math:`n` indices
* Exchange the elements between every other pair of indices the indices

    * If an odd number of indices, exchange the elements from the last index to the end


* This is a generalization of one point crossover
* :math:`n=2` is popular (two point crossover)

.. figure:: n_point_crossover.png
    :width: 450 px
    :align: center

    Result of applying :math:`n` point crossover where :math:`n=3`. The randomly selected indices in this example are
    5, 8, and 14. All elements between indices 5 and 8 (exclusively) are exchanged along with all
    the elements from index 14 to the end of the chromosome.


Uniform Crossover
^^^^^^^^^^^^^^^^^

* Select some random number of indices at random
* Exchange the elements at those indices
* Often implemented by giving each index a 50/50 chance to be selected for crossover

* This crossover is relatively *destructive*
* Not particularly effective on chromosomes where element adjacency is important

.. figure:: uniform_crossover.png
    :width: 450 px
    :align: center

    Result of applying uniform crossover where the a total of 8 values were exchanged.


Mutations
---------

Bit Flip Mutation
^^^^^^^^^^^^^^^^^

* Select some number of bits and *flip* them

    * Change 0s to 1s and 1s to 0s


* The number of bits that get flipped is arbitrary

    * Could be hard coded
    * Could be randomly selected each time


* Similar to uniform crossover, but instead of exchanging elements between parents, just change the binary symbol

* As the number of bits that are flipped increases, so does the level of *destruction* this mutation causes


.. figure:: bit_flip_mutation.png
    :width: 450 px
    :align: center

    Result of applying a bit flip mutation to some chromosome. Here, a total of 10 bits were flipped during the
    mutation, which is a rather high number of bits to flip. Although this example shows the parent chromosome
    containing only 1s, this is not a requirement; it could have contained 0s that got changed to 1s.



Genetic Operators for Integer Representations
=============================================

* Integer representations are those that consist of integer values

* The crossovers used for binary representations are typically used for integer representations


Single Point Mutation
---------------------

* Sometimes called "Random Resetting"

* Similar to the bit flip mutation

* Select an index at random
* Replace the value at the selected index with some other valid integer

* A single point mutation can be generalized to an :math:`n` point mutation by selecting multiple indices to change

* This mutation is helpful in situations where the values within the chromosome represent cardinal attributes

    * Where the order of the possible integer values *do not* necessary matter

        * For example, the amount of values within a set


* This mutation is also helpful in situations where each possible integer is equally likely to be within the chromosome


Creep Mutation
--------------

* Select an index at random
* Change the value at that index to one relatively *close to* the current value

    * For example, if the value at the selected index is 7, replace it with an 8


* What *close to* means will depend on the context

* This mutation is often used in situations where the values within the chromosome represent ordinal attributes

    * Where the order of the possible integer values matter



Genetic Operators for Floating Point Number Representations
===========================================================



Genetic Operators for Permutation Representations
=================================================



Genetic Operators for Tree Representations
==========================================



For Next Class
==============

* TBD
