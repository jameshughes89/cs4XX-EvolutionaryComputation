********************************************
Symbolic Regression with Genetic Programming
********************************************

* The purpose of this topic is to perform symbolic regression with genetic programming
* The genetic programming system being used is DEAP (Distributed Evolutionary Algorithms in Python)
* Much of the heavy lifting required to implement a genetic programming algorithm is managed by DEAP



Problem --- Regression Analysis
===============================

* Regression is finding the relationships between dependent and independent variables given some observations
* A common and simple form of regression is *linear regression*

    * Find a *linear* relationship between some dependent and independent variables


.. figure:: linear_regression_linear_data.png
    :width: 500 px
    :align: center

    Observations of some phenomenon plotted in two dimensions. The dependent variable is plotted along the y-axis and
    the independent variable is along the x-axis. From a quick glance, this data clearly has some linear relationship.




Linear
accuracy 0.9999994486146649 (R^2)
coef 4.50016122
int 7.220999868042664


Nonliear
0.010924289363573592 (R^2)
[-3.07039458]
916.5506746535088

SR
0.16208662410178923 MSE

1.10051099017284868*X**2 -4.4395784214070755
add(add(protected_divide(mul(ARG0, ARG0), 9.949160766203782), mul(ARG0, ARG0)), -4.4395784214070755)



DEAP
====



Language
========



DEAP Setup
==========


Bloat Control
-------------


Bookkeeping
-----------



Running and Results
===================



For Next Class
==============

* Check out the following script

    * :download:`Symbolic Regression with Genetic Programming </../src/gp_symbolic_regression.py>`


* `Read DEAP's sample symbolic regression implementation <https://deap.readthedocs.io/en/master/tutorials/advanced/gp.html>`_
* `Read through DEAP's various genetic programming examples <https://deap.readthedocs.io/en/master/examples/index.html#genetic-programming-gp>`_



