*******************
Genetic Programming
*******************

* Genetic programming is using a genetic algorithm for evolving programs/functions
* The genotype is typically a tree structure representing the program/function phenotype
* Genetic operators that work on the tree encoding are used

* Ultimately, it's a genetic algorithm that searches the space of programs/functions



Example Problem --- Breast Cancer Identification
================================================

* Consider the problem of determining if an individual has breast cancer [#]_

.. list-table:: Observations of Patients Tested for Breast Cancer
    :widths: 25 25 25 25 25 25 25
    :header-rows: 1

    * - ID
      - Thickness
      - Size
      - Shape
      - Bare Nuclei
      - Mitosis
      - Class
    * - 1000025
      - 5
      - 1
      - 1
      - 1
      - 1
      - Benign
    * - 1002945
      - 5
      - 4
      - 4
      - 10
      - 1
      - Benign
    * - 1017122
      - 8
      - 10
      - 10
      - 10
      - 1
      - Malignant
    * - 1018099
      - 1
      - 1
      - 1
      - 10
      - 1
      - Benign
    * - 1041801
      - 5
      - 3
      - 3
      - 3
      - 1
      - Malignant
    * - 1043999
      - 1
      - 1
      - 1
      - 3
      - 1
      - Benign
    * - 1044572
      - 8
      - 7
      - 5
      - 9
      - 4
      - Malignant
    * - ...
      - ...
      - ...
      - ...
      - ...
      - ...
      - ...


* The goal is to build a classifier to determine if a patient has breast cancer based on the observations

* What should the classifier be?

    * ``If size > 4 and (shape == 3 or shape == 5) then malignant else benign``?
    * ``If thickness > 4 and thickness < 9 then malignant else benign``?
    * ``If mitosis == 1 then malignant else benign``?


* It would take careful study and a deep understanding of the problem to build a classifier manually
* However, AI and Machine Learning are often used to automate the process of building a classifier

    * The AI and Machine Learning would try to generalize trends that exists in the observations within the data


* Unfortunately, most evolutionary computation algorithms are not particularly designed to find models like this

    * Often they are used for combinatorial or real number optimization


* This is where genetic programming comes in

    * With the use of a clever representation, genetic programming optimizes programs/functions



Representation
==============


* S-expressions (symbolic expressions) are commonly used as the representation for genetic programming
* S-expressions are used to represent nested instructions and data

* These s-expressions are commonly visualized as tree structures


.. figure:: tree_examples.png
    :width: 500 px
    :align: center

    Three s-expressions shown as trees representing three different programs/functions. The left tree represents
    the s-expression ``((1.2 - x) * y)``, the centre tree represents ``((length < 5.2) or not(red))``, and the
    right tree represents ``if((open and right_closed)) then(forward) else(turn_right)``. The light coloured nodes
    represent operators while the darker nodes represent operands, both constants and variables.


* Consider the above program/function above for the breast cancer identification problem

    * ``If size > 4 and (shape == 3 or shape == 5) then malignant else benign``?


* If ``TRUE`` means malignant and ``FALSE`` benign, the program/function can be written as the following s-expression

    * ``((size > 4) and ((shape == 3) or (shape == 5)))``


* This s-expression can also be represented as the following tree

.. figure:: breast_cancer_tree.png
    :width: 500 px
    :align: center

    The program/function ``If size > 4 and (shape == 3 or shape == 5) then malignant else benign`` represented as a tree
    structure.



Language
--------


Types vs. Untyped
-----------------



Typical Genetic Programming Setup
=================================

* A genetic programming algorithm is setup very similar to an ordinary genetic algorithm

    * Initialize a population
    * Evaluation
    * Selection
    * Genetic Operators
    * Termination


* The key differences are around the tree representation
* For example, the genetic operators must work with the trees

.. figure:: ../genetic-operators/genetic_programming_crossover.png
    :width: 600 px
    :align: center

    One point crossover on a tree structure. The two randomly selected subtrees are exchanged.


.. figure:: ../genetic-operators/genetic_programming_mutation.png
    :width: 600 px
    :align: center

    One point mutation on a tree structure. A randomly selected node in the tree is replaced with a randomly generated
    subtree. In this example, the subtree was replaced with a variable, but it could be been a more complex subtree.


* Typically, for genetic programming, mutation rates are kept very low (less than 5%)

    * But ultimately, the value to use is a value that works well


* Populations are typically very large
* With large populations, common selection strategies can become problematic
* A strategy called *over-selection* is sometimes used

    * Split the population into two groups

        * Top :math:`x%` in group A
        * Bottom :math:`100% - x%` in group B


    * Select from both groups independently

        * For example, :math:`80%` of the new population comes from group A and 20% from group B


* However, it is still common to see tournament and roulette wheel selection used in genetic programming



Bloat
=====

Replication Accuracy Theory
---------------------------


Removal Bias Theory
-------------------


Nature of Programming Space Theory
----------------------------------


Strategies to Address Bloat
---------------------------



Example Problem --- Symbolic Regression
=======================================



Interesting Applications
========================



For Next Class
==============

* TBD

----------------------

.. [#] `Data based on data from the UCI Machine Learning Repository <http://archive.ics.uci.edu/dataset/15/breast+cancer+wisconsin+original>`_