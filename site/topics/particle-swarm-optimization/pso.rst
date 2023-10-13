***************************
Particle Swarm Optimization
***************************

* Particle Swarm Optimization (PSO) is a stochastic population based optimization technique

    * Like many forms of evolutionary computation


* It consists of *particles* that all act independently, but are influenced by the population


.. figure:: birds_flying.gif
    :width: 500 px
    :align: center

    A flock of birds. Each bird is making decisions independently that are informed by other birds around them. As a
    result, it appears as if the flock is moving in some well coordinated way.



Particles
=========



Velocity
========

* The velocity determines where the particle will be for the next iteration of the algorithm
* In other words, the velocity :math:`\vec{v}(t)` is used to determine the position of particle :math:`\vec{x}(t+1)`


Velocity Calculation
--------------------

* Velocities are typically initialized with some random values within some range
* But as the algorithm executes, the velocity of the particles change as they become influenced by

    * The particles' best known position in space
    * The population's best known position in space


* Velocity update for some particle :math:`i`

.. math::

    \vec{v_{i}}(t+1) = \omega\vec{v_{i}}(t)
        + c_{1}\vec{r_{1}}(\vec{p_{i}}_{best} - \vec{x_{i}}(t))
        + c_{2}\vec{r_{2}}(\vec{g}_{best} - \vec{x_{i}}(t))


Inertia Term: :math:`\omega\vec{v_{i}}(t)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Position Update
===============



Algorithm
=========



Simple Enhancements
===================



For Next Class
==============

* TBD
