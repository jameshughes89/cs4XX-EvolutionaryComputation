***************************
Particle Swarm Optimization
***************************

* Particle Swarm Optimization (PSO) is a stochastic population based optimization technique

    * Like many forms of evolutionary computation


* It consists of *particles* that all act independently, but are influenced by the population
* PSO is particularly well designed for real/floating point number optimization


.. figure:: birds_flying.gif
    :width: 500 px
    :align: center

    A flock of birds. Each bird is making decisions independently that are informed by other birds around them. As a
    result, it appears as if the flock is moving in some well coordinated way.



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
    * Velocity, which is also represented as an :math:`n` dimensional vector containing deltas
    * Best visited position (:math:`n` dimensional vector)
    * Access to the swarm's best known position in space (:math:`n` dimensional vector)



Velocity
========



Position Update
===============



Algorithm
=========



Simple Enhancements
===================



For Next Class
==============

* TBD
