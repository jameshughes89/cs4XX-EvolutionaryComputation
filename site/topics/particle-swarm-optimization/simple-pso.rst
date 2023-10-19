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



Termination Requirement
=======================

* Any stopping criteria could be used
* Here, a predetermined set of iterations was specified
* In other words, the fitness and position update processes are repeated within a loop until all iterations complete


.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-iteration-loop]
    :end-before: # [end-iteration-loop]


* Finally, once complete, the global best position will be the best position found by the PSO algorithm

.. literalinclude:: /../src/pso.py
    :language: python
    :lineno-match:
    :start-after: # [begin-ending]
    :end-before: # [end-ending]



For Next Class
==============

* TBD