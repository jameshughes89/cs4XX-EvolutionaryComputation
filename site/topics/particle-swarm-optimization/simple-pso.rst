****************
Implementing PSO
****************

* The purpose of this topic is to see an implementation of particle swarm optimization (PSO)
* It is a simple implementation that incorporates no enhancements
* The problem PSO is being applied to in this example is some arbitrary benchmark real number optimization problem
* Despite how simple the implementation is, it will still perform well



Problem
=======



Initialization
==============



Evaluation
==========



Update Velocity & Speed
=======================

* Once the random vectors for the cognitive and social terms are determined
* Each particle's velocity is updated

.. math::

    \vec{v_{i}}(t+1) = \omega\vec{v_{i}}(t)
        + c_{1}\vec{r_{1}}(\vec{p_{i}}_{best} - \vec{x_{i}}(t))
        + c_{2}\vec{r_{2}}(\vec{g}_{best} - \vec{x_{i}}(t))


* And with an updated velocity, the particle's position can then be updated

.. math::

    \vec{x_{i}}(t+1) = \vec{x_{i}}(t) + \vec{v_{i}}(t+1)



.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-position-update]
    :end-before: # [end-position-update]



Termination Requirement
=======================



For Next Class
==============

* TBD