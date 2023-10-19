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

* Here, all particle positions and velocities are assigned random values to start

    * However, any form of initialization may be used
    * For example, seeding the particle positions with already known *good* points in space


.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-initialization]
    :end-before: # [end-initialization]


* Notice in the above code that the particles' starting positions, although randomly selected, are bound
* Also notice that the particles' best and global best positions are initialized


Hyperparameters
^^^^^^^^^^^^^^^

* For reference, below are the hyperparameters selected

.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-hyperparameters]
    :end-before: # [end-hyperparameters]


* The inertia, social, and cognitive terms are set to the values suggested bu `van den Bergh <https://repository.up.ac.za/bitstream/handle/2263/24297/00thesis.pdf?sequence=1>`_
* The number of dimensions is dictated by the Matyas function
* The other values are arbitrary selected



Evaluation
==========



Update Velocity & Speed
=======================



Termination Requirement
=======================



For Next Class
==============

* TBD