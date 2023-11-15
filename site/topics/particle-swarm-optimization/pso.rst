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


* PSO is particularly well designed for real/floating point number optimization
* It is relatively simple to implement compared to other forms of evolutionary computation

    * It has relatively few hyperparameters to tune too


* Further, it is simple to extend and enhance



Particles
=========

* PSO consists of a population of *particles* that represent points in some search space

    * Like candidate solutions from a genetic algorithm


* Unlike chromosomes, these particles do not have the traditional variation operators of mutation and crossover
* Instead, the particles have a propensity to more towards areas that the particles *likes*
* However, these particles are also influenced by the population of particles

    * They also have a propensity to move towards areas that the population *likes*


* In terms of an optimization problem

    * Each particle has a propensity to move towards the best area of the search space it has encountered
    * While also having a propensity to move to the best part of the search space the population has encountered


* Each particle also has velocity and inertia


.. figure:: particles_moving.gif
    :width: 500 px
    :align: center
    :target: https://en.wikipedia.org/wiki/Particle_swarm_optimization

    Particles moving through a three-dimensional space represented in two-dimensions with the third dimension being
    represented by colour. Arrows associated with each particle represents the particle's velocity. Over time, the
    particles, although acting independent, while also being influenced by particles within the population, cluster
    around the global minimum.


Representation
--------------

* POS is often used for real/floating point number optimization
* Thus, each particle is typically represented as an :math:`n` dimensional vector encoding its position in space

    * Where :math:`n` is the dimensionality of the problem
    * For example, in the above figure, each particle would be represented as a three-dimensional vector
    * ``<1.42345478, 4.334678, 3.31345786555567>``


* Each particle has a

    * Position in space, represented as an :math:`n` dimensional vector containing a position in space

        * :math:`\vec{x}(t)` --- Position at time :math:`t`


    * Velocity, which is also represented as an :math:`n` dimensional vector containing deltas

        * :math:`\vec{v}(t)` --- Velocity at time :math:`t`


    * Best visited position (:math:`n` dimensional vector)

        * :math:`\vec{p}_{best}` --- Particle's best known position


    * Access to the swarm's best known position in space (:math:`n` dimensional vector)

        * :math:`\vec{g}_{best}` --- Global best known position



.. _pso_velocity:

Velocity
========

* The velocity determines where the particle will be for the next iteration of the algorithm
* In other words, the velocity :math:`\vec{v}(t)` is used to determine the position of particle :math:`\vec{x}(t+1)`


Velocity Calculation
--------------------

* Velocities are typically initialized with some random values within some range
* But as the algorithm executes, the velocity of the particles change as they become influenced by

    * The *particles'* best known position in space
    * The *population's* best known position in space



Inertia Term: :math:`\omega\vec{v_{i}}(t)`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Each particle has some velocity
* When particles' velocities are being updated, the changes are applied to an already moving particle
* These particles *want* to continue moving the way they are

    * They resist change


* Thus, the first part of a velocity update takes into consideration the current velocity of the particle

    * :math:`\omega\vec{v_{i}}(t)`

* Where

    * :math:`i` is some particle
    * :math:`\vec{v_{i}}(t)` is the particle's velocity at time :math:`t`
    * :math:`\omega` is some coefficient use to control how much the particles want to resist change

        * :math:`\omega \in [0, 1]`


Cognitive Term: :math:`c_{1}\vec{r_{1}}(\vec{p_{i}}_{best} - \vec{x_{i}}(t))`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Each particle *wants* to move towards the area of the search space it prefers

    * The best known location for that particle


* Thus, part of the velocity update alters the velocity such that it will move the towards this part of the space

    * :math:`c_{1}\vec{r_{1}}(\vec{p_{i}}_{best} - \vec{x_{i}}(t))`


* Where

    * :math:`i` is some particle
    * :math:`c_{1}` is some coefficient used to control how much the particle is influenced by its best known position

        * :math:`c_{1} \in [0, 2]`
        * The higher the :math:`c_{1}`, the more the particle is influenced by its best known position


    * :math:`r_{1}` is some stochastic vector discussed below
    * :math:`\vec{p_{i}}_{best}` is the particle's best known position within the search space
    * :math:`\vec{x_{i}}(t)` is the particle's position at time :math:`t`


* The difference between the particle's best known position and current position dictates where the particle needs to go

    * :math:`\vec{p_{i}}_{best} - \vec{x_{i}}(t)`


* :math:`c_{1}` and :math:`r_{1}` scale the vector


.. figure:: plot_best_vs_current_position.png
    :width: 500 px
    :align: center

    Vector (blue) showing the difference between the particle's best known position (red) and its current position
    (green). The vector :math:`(-1, -3)` is shown starting at the current position :math:`(3, 4)`. If the particle
    were to have exactly this velocity for one time step, it would return to the best known position.


Social Term: :math:`c_{2}\vec{r_{2}}(\vec{g}_{best} - \vec{x_{i}}(t))`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* Similarly, each particle is influenced by the population's best known position

    * :math:`c_{2}\vec{r_{2}}(\vec{g}_{best} - \vec{x_{i}}(t))`

* Where

    * :math:`i` is some particle
    * :math:`c_{2}` is some coefficient used to control how much the particle is influenced by the population's best

        * :math:`c_{2} \in [0, 2]`


    * :math:`r_{2}` is some stochastic vector discussed below
    * :math:`\vec{g}_{best}` is the population's best known position within the search space
    * :math:`\vec{x_{i}}(t)` is the particle's position at time :math:`t`



Random/Stochastic Components: :math:`\vec{r_{1}}` and :math:`\vec{r_{2}}`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The cognitive and social portions of the velocity update included the vectors :math:`\vec{r_{1}}` and :math:`\vec{r_{2}}` respectively
* These vectors have values between :math:`[0, 1]` that are stochastically determined

    * Randomly determined for each velocity update calculation for each particle


* These random/stochastic vectors are important as they add a chance for novelty
* Further, they have been empirically shown to improve the search and prevent premature convergence


Putting the Velocity Update Together
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* The velocity update is the sum of the parts of the update

    * Inertia term + cognitive term + social term


* Velocity update for some particle :math:`i`

.. math::

    \vec{v_{i}}(t+1) = \omega\vec{v_{i}}(t)
        + c_{1}\vec{r_{1}}(\vec{p_{i}}_{best} - \vec{x_{i}}(t))
        + c_{2}\vec{r_{2}}(\vec{g}_{best} - \vec{x_{i}}(t))


* As discussed, there are three coefficients that need to be tuned for the algorithm
* As a starting place, `van den Bergh <https://repository.up.ac.za/bitstream/handle/2263/24297/00thesis.pdf?sequence=1>`_ suggests

    * :math:`\omega = 0.729844`
    * :math:`c_{1} = c_{2} = 1.496180`


* However, one should always aim to tune these values for their needs



.. _pso_position:

Position Update
===============

* After the particle's velocity is calculated, the particle's new position can be determined
* The new position is the sum of its current position and its current velocity

.. math::

    \vec{x_{i}}(t+1) = \vec{x_{i}}(t) + \vec{v_{i}}(t+1)


* Consider the below figure

    * The particle's current position :math:`\vec{x_{i}}(t)` is represented as the green vector
    * The particle's velocity :math:`\vec{v_{i}}(t+1)` is represented as the blue vector
    * The particle's new position is represented as the red dashed vector

        * The sum of the particle's current position and velocity
        * :math:`(3, 2) + (-1, 1) = (2, 3)`


.. figure:: plot_position_update.png
    :width: 500 px
    :align: center

    The summation of the particle's current position (green) and its velocity (blue) results in the particle's new
    position within the search space (red). One could also visualize this by having the velocity vector start at the end
    of the current position vector (instead of the origin, as it is currently shown).



Algorithm
=========

* The high-level idea of the algorithm is presented below

.. code-block:: text

    Initialize the particles' positions randomly
    Initialize the velocities randomly
    While stopping criteria is not met
        For all particles
            Evaluate the particle's fitness
            Update particle's and global bests if necessary

        For all particles
            Calculate the particle's new velocity
            Update the particle's position


* It may not be immediately obvious, but look for the similarities between this algorithm and a genetic algorithm

    * Initialization
    * Generational loop
    * Fitness evaluation
    * Variation operations


* The major differences are that

    * There is no real selection as all particles *survive*

        * Although, this *is* a selection strategy


    * The velocity and position updates are not mutation and crossover

        * However, consider the cognitive and social aspects of the velocity update
        * This *is* a mechanism for exploration and exploitation
        * In other words, they are in fact variation operators



Simple Enhancements
===================

* PSO's ability to be modified is one of the reasons it's popular

    * Like with most forms evolutionary computation, anything could be done


* Some quick examples of some modifications are

    * Neighbourhoods

        * Each particle is part of some *neighbourhood*
        * The neighbourhood's best is also recorded and impacts the velocity updates
        * :math:`c_{3}\vec{r_{3}}(\vec{n_j}_{best} - \vec{x_{i}}(t))` is added to the velocity update calculation
        * Where :math:`\vec{n_j}_{best}` is the :math:`j^{th}` neighbourhood's best known location
        * And :math:`c_{3}` is some tunable constant and :math:`\vec{r_{3}}` is another randomly determined vector


    * Velocity clamping

        * Disallow particles from having velocities over a certain value
        * This could be done by setting a ceiling, or an exponentially decaying velocity


    * Boundary/Position clamping

        * Dissalow particles from going beyond some boundaries
        * One could just set a limit and not allow particles beyond it
        * More creative strategies include having particles jump to the other side of the space
        * Or have the particles *bounce* off the boundary back in the other direction


    * Charged PSO

        * Particles repel one another
        * The velocity update includes a term for the particles' propensity to move away from one another



For Next Class
==============

* Check out the following script

    * :download:`The Selection Script </../src/pso.py>`
