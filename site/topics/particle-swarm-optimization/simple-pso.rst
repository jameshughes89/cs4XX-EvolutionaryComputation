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

* A particle's position corresponds to the arguments that are to be provided to the function
* Therefore, provide the particle's coordinates to the function to evaluate

* Once the function's value is returned, update the particle's best known position and global best position if necessary

* Notice that each particle does not need to know what it's fitness value is
* The algorithm only cares about

    * Each particle's best known *position*
    * The global best *position*


.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-evaluation]
    :end-before: # [end-evaluation]


Update Velocity & Speed
=======================



Termination Requirement
=======================



For Next Class
==============

* TBD