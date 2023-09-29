**********************
Tuning Hyperparameters
**********************

* All the evolutionary computation algorithms used require some form of hyperparameter tuning
* Further, given the modular nature of these algorithms, each part of the algorithm is itself a hyperparameter

    * These may also come with additional hypermarkets that require some tuning


* There exists no best way to perform parameter tuning, but there are some common strategies



Symbolic vs. Numeric Hyperparameters
====================================

* Symbolic hyperparameters are the modular portions of the algorithms

    * Crossover operator
    * Selection strategy


* Numeric hyperparameters are the numerical values that can be tuned

    * Crossover rate
    * Tournament size


* Regardless of the hyperparameter type, their values need to be set

    * A crossover rate needs to be set
    * A decision needs to be made on which selection to use

        * Symbolic hyperparameters may introduce additional numeric hyperparameters
        * For example, if tournament selection is selected, the tournament size needs to be specified


* Typically, symbolic hyperparameters are more high-level

    * They make up the evolutionary computation algorithm


* The numerical hyperparameters are low-level

    * Specifies the details of the algorithm's implementation 


* An *evolutionary computation algorithm instance* is one that has all the necessary hyperparameters set



Tuning Hyperparameters
======================

Starting Places
---------------


Empirical Tinkering
-------------------


Automated Approaches
--------------------



For Next Class
==============

* TBD