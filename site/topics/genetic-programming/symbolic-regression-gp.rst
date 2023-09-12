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


.. figure:: regression_linear_data.png
    :width: 500 px
    :align: center

    Observations of some phenomenon plotted in two dimensions. The dependent variable is plotted along the y-axis and
    the independent variable is along the x-axis. From a quick glance, this data clearly has some linear relationship.


* Given the above observations, the goal is to draw a *line of best fit*

    * Which should look a lot like :math:`y = mx + b`


* The mathematics behind finding this line is interesting, but outside the scope of this course
* `Fortunately, scikit-learn provides a way to find this line <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html>`_


.. figure:: regression_linear_data_linear_model.png
    :width: 500 px
    :align: center

    Linear model plotted on top of the observations. The resulting model is :math:`\hat{y} = 0.999885x + 0.997937` and
    has an :math:`R^{2}` value of :math:`0.9999885`.


* The linearly regressed model for the above observations is :math:`\hat{y} = 0.999885x + 0.997937`

    * Note that :math:`\hat{y}` denotes that it is not :math:`y`, but only a prediction/estimation of :math:`y`


* This particular model has an :math:`R^{2}` of :math:`0.9999885`

    * This is a measure of *goodness*
    * The closer to 1.0, the better the fit


Linear Regression on Nonlinear Relationships
--------------------------------------------

* With linear regression, trouble arises when the observed data has nonlinear relationships
* It is still possible to find a high-quality model, but it would require several assumptions and a lot of guesswork

.. figure:: regression_nonlinear_data.png
    :width: 500 px
    :align: center

    Observed data with clear nonlinear relationships. The data appears to be parabolic or hyperbolic, but may be neither
    depending on which segment of the function was observed. It is not possible to effectively fit a straight line to
    describe the relationship between the dependent and independent variable.


* Nevertheless, looking for a linear model for such nonlinear data is doomed to fail


.. figure:: regression_nonlinear_data_linear_model.png
    :width: 500 px
    :align: center

    Linear model generated with linear regression on the nonlinear data. The resulting model is
    :math:`\hat{y} = -3.070395x + 916.550675`, which has an :math:`R^{2} = 0.010924`. Although this is the best possible
    straight line that fits this data, it is clear that it is not effectively fitting the data due to the limitation of
    the modelling strategy.


Symbolic Regression
-------------------

* An alternative strategy is something called *symbolic regression*
* It is a form of regression analysis that requires fewer assumptions and works with nonlinear data

* By using symbolic regression, the underlying nonlinear relationships may be found

.. figure:: regression_nonlinear_data_nonlinear_model.png
    :width: 500 px
    :align: center

    Nonlinear model found with symbolic regression. The model is :math:`\hat{y} = 1.100511x^{2} - 4.439578` and has
    a mean squared error of :math:`0.162087`.


* It is clear that :math:`\hat{y} = 1.100511x^{2} - 4.439578` effectively describes the relationships in the data
* The *mean squared error* is :math:`0.162087`

    * This is not the same as :math:`R^{2}`
    * With mean squared error, a value closer to 0.0 is better


.. note::

    In reality, symbolic regression produced ``add(add(protected_divide(mul(x, x), 9.949161), mul(x, x)), -4.439578)``,
    which was simplified to :math:`\hat{y} = 1.100511x^{2} - 4.439578`.



DEAP
====

* Due to the complexity, it is not common to implement genetic programming from scratch
* Instead, a genetic programming system will be used, which does much of the heavy lifting for the user
* Many systems exist in various programming languages

* `DEAP is a framework for evolutionary computation algorithms in Python <https://deap.readthedocs.io/en/master/>`_

    * Distributed Evolutionary Algorithms in Python --- DEAP
    * It's a package for implementing evolutionary computation algorithms


* DEAP is not only for genetic programming, but many evolutionary computation algorithms
* It includes algorithm and tools for implementing multiple types of algorithms, enhancements, and analysis

* Although any genetic program could be used, DEAP will be used here

    * `The GitHub page is available here <https://github.com/deap/deap>`_
    * It is encouraged to contribute to the repository if possible


* It is strongly recommended to have a look at DEAP's documentation

    * `It includes a description of genetic programming with DEAP <https://deap.readthedocs.io/en/master/tutorials/advanced/gp.html>`_
    * `It also has a guided tutorial on how to perform symbolic regression with DEAP <https://deap.readthedocs.io/en/master/examples/gp_symbreg.html>`_
    * `Further, additional and more advanced tutorials can be found here <https://github.com/DEAP/deap/tree/master/examples/gp>`_



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



