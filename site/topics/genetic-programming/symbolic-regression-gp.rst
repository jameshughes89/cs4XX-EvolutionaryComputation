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



Data
====

* The data being used will be tabular data

.. list-table:: Example Data for Symbolic Regression
    :widths: 25 25 25
    :header-rows: 1

    * - ARG1 (:math:`X_1`)
      - ARG2 (:math:`X_2`)
      - ARG3 (:math:`y`)

    * - -3.168334936427432069e+01
      - 3.632539499451265641e+01
      - -5.755503747607460809e+02

    * - -3.597718491118718731e+01
      - 1.636337813259562779e+01
      - -2.942380144735846557e+02

    * - 4.352352435635705774e+01
      - -1.541892093015873577e+01
      - -3.354514356502435248e+02

    * - 4.197055084109130263e+01
      - 1.254917338770126101e+01
      - 2.634167376922860626e+02


Evaluation
==========



Language
========

* With symbolic regression, genetic programming will be searching the space of mathematical expressions
* This includes both the operators and operands
* The language is the set of operators and operands that the genetic programming system can use in the search
* The trouble is, it's not always clear which operators and operands should be included
* Thus, the design of the language may need to be tuned for evolution like other hyperparameters

* Fortunately, with symbolic regression, there is a common set to start with

    * Typical arithmatic operators
    * Maybe some trigonometry functions
    * Maybe natural log and Euler's number


* However, there is a potential problem with divide as the evolutionary search may try to divide by zero
* For this reason, it is common to see a *protected divide* used instead

    * If attempting to divide by zero, return infinity


.. literalinclude:: /../src/gp_symbolic_regression.py
    :language: python
    :lineno-match:
    :pyobject: protected_divide


* Setting up the language with DEAP is then done like below

.. literalinclude:: /../src/gp_symbolic_regression.py
    :language: python
    :lineno-match:
    :start-after: # [begin-language]
    :end-before: # [end-language]


* The first line, creating the ``PrimitiveSet`` object, is where the language operators and operands will be added

    * It also specifies the number of independent variables the function will have as the second argument
    * Here, it assumes the independent variables are stored in some list called ``independent_variables``


* Each operator is added to the primitive set object along with the number of operands that operator requires

    * The operator is the first argument, and is passed as a function
    * Most of the added operators in this example are taken from the ``operator`` library
    * The protected divide, described above, is also added
    * The ``neg`` operator is the negation (multiply by -1) and only requires one operand


* Finally, the constant values are added with ``addEphemeralConstant``

    * In this example, integers between -10 and 10 are eligible


.. warning::

    There is no guarantee or suggestion that this is a *good* language, but it is at least a reasonable place to start.


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



