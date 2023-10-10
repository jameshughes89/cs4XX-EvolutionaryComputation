************************
Multi-Objective Problems
************************

* For the most part, all problems looked at have been single objective problems
* However, it is not uncommon to have multiple objectives to optimize
* Sometimes these objectives compliment each other, and sometimes they are in conflict with one another

* Consider buying a house

    * Low price
    * Want at least 4 bedrooms
    * Want to have a small commute distance
    * Proximity to amenities
    * Style


* Some of these features are subjective

    * Style
    * The amenities one cares about


* Some complement one another

    * Small commute and amenities are probably related


* Some are in conflict

    * At least 4 bedrooms and close to amenities
    * Low price


.. figure:: house_multiobjective_plot.png
    :width: 500 px
    :align: center

    One may want a large house but to pay as little as possible. These objectives are in conflict with one another. Each
    point represents a potential house. 



Scalarization
=============

* Scalarization is the process of *scaling* the various features to be optimized and combining them into a single value

    * It is a way to turn multi-objective problems into a single objective problem


* It is an *a priori* process, meaning the decisions about the scaling must be done before the search starts


Weighted Sum
------------

* The simplest strategy is a *weighted sum*
* Scale each individual objective being optimized and add them together to make a single value

    :math:`w_{1}f_{1}(x) + w_{2}f_{2}(x) + w_{3}f_{3}(x) + ... + w_{m}f_{m}(x)`

    Or

    :math:`\sum_{i}^{m}w_{i}f_{i}(x)`


* Where

    * :math:`x` is some chromosome
    * :math:`m` is the number of objectives being optimized
    * :math:`f_{i}(x)` is a function returning the :math:`i^{th}` objective's fitness on chromosome :math:`x`
    * :math:`w_i` is the weight/scale of objective :math:`i`


* If one objective is more important than another, assign it a stronger weight
* Use negative weights to account for objectives that are to be minimized/maximized

* Unfortunately, however, weighted sums do not work too well beyond two or three objectives
* Further, it's not always easy to assign the weights



Dominance
=========

Pareto Sets
-----------



For Next Class
==============

* TBD
