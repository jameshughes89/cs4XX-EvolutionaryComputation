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




:math:`n` Point Crossover
^^^^^^^^^^^^^^^^^^^^^^^^^


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
    :width: 400 px
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