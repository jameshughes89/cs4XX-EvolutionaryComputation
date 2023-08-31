*******************
Genetic Programming
*******************



Example Problem --- Loan Application
====================================

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

Language
--------


Types vs. Untyped
-----------------



Typical Genetic Programming Setup
=================================



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