**************
Representation
**************



Genotype vs. Phenotype
======================




:math:`n` Queens Example
------------------------

* Consider the :math:`n` queen problem

    * Place :math:`n` queens on an :math:`n \times n` chess board such that none can attack any other


* The phenotype is the :math:`n \times n` chess board configuration of :math:`n` queens


.. figure:: ../representation/10_queens.png
    :width: 300 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Eight_queens_puzzle

    A valid configuration of :math:`10` queens on a :math:`10 \times 10` chess board. This particular configuration is
    called a "staircase solution".


2D Genotype
^^^^^^^^^^^

* For the genotype, a 2D list encoding could be used

    * It would require an :math:`n \times n` list
    * :math:`n` cells in the list would be filled, representing the queen locations


* This would be a very *direct* representation

    * The *translation* from the genotype to phenotype trivial


* With this encoding, there would be a search space of size :math:`n \times n \choose n`

    * For :math:`8` queens, this is :math:`{64 \choose 8} = 4,426,165,368`


* This search space includes all possible valid board configurations
* However, it also includes a lot more invalid board configurations


1D List of Coordinates
^^^^^^^^^^^^^^^^^^^^^^^

* 2D encodings can be tricky to work with
* Perhaps a 1D list of :math:`(x, y)` coordinates would work

    * It would require a list of length :math:`n`
    * Each value in the list would be a queen's :math:`(x, y)` coordinate


* This representation is a little less direct than the 2D list

    * There would need to be some translation to get to the phenotype
    * This is not a problem though


* This encoding can also represent all possible configurations

* For the size of the search space

    * There are :math:`n` queens to be placed
    * Each queen has a :math:`(x, y)` coordinate
    * There are :math:`n \times n` possible positions for each queen


* Therefore, with this encoding, the search space has a size of :math:`(n \times n)^{n}`

    * For :math:`8` queens, this is :math:`64^{8} = 2.815 \times 10^{14}`


* Although a 1D encoding may be easier to work with, this encoding is worse in terms of the size of the search space

    * It's worse since it's possible for queens to be placed in the same :math:`(x, y)` coordinate



Binary Representation
=====================



Integer Representation
======================



Permutation Representation
==========================



Real Value Representation
=========================




Tree Representation
===================



For Next Class
==============

* TBD
