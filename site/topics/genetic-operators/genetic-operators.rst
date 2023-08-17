*****************
Genetic Operators
*****************



Genetic Operators for Binary Representations
============================================

* Binary representations are those that only contain two values, which are typically ``0``\s and ``1``s


Crossovers
----------

One Point Crossover
^^^^^^^^^^^^^^^^^^^

* Randomly select an index
* Exchange the elements between the chromosomes after that index

.. figure:: one_point_crossover.png
    :width: 450 px
    :align: center

    Result of applying one point crossover on two chromosomes. This example has index ``5`` as the randomly selected
    crossover point, thus, all elements after index ``5`` are exchanged between the parent chromosomes. Although this
    example shows one parent containing only ``0``\s and the other containing only ``1``\s, this is not a requirement;
    the parents could contain both ``0``\s and ``1``\s.


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
    ``5``, ``8``, and ``14``. All elements between indices ``5`` and ``8`` (exclusively) are exchanged along with all
    the elements from index ``14`` to the end of the chromosome.


Uniform Crossover
^^^^^^^^^^^^^^^^^



Mutations
---------

Bit Flip Mutation
^^^^^^^^^^^^^^^^^

* Select some number of bits and *flip* them

    * Change ``0``\s to ``1``\s and ``1``\s to ``0``\s


* The number of bits that get flipped is arbitrary

    * Could be hard coded
    * Could be randomly selected each time


.. figure:: bit_flip_mutation.png
    :width: 450 px
    :align: center

    Result of applying a bit flip mutation to some chromosome. Here, a total of 10 bits were flipped during the
    mutation, which is a rather high number of bits to flip. Although this example shows the parent chromosome
    containing only ``1``\s, this is not a requirement; it could have contained ``0``\s that got changed to ``1``\s.



Genetic Operators for Integer Representations
=============================================



Genetic Operators for Floating Point Number Representations
===========================================================



Genetic Operators for Permutation Representations
=================================================



Genetic Operators for Tree Representations
==========================================



For Next Class
==============

* TBD