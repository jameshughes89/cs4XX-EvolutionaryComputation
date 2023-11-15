**********************
Differential Evolution
**********************

Introduction to Differential Evolution (DE)
===========================================
* DE is a method in evolutionary computation that optimizes solutions to problem by iteratively improving a candidate solution based on a quality measure.
* It's a type of metaheuristic, making few assumptions about the problem, enabling exploration of large solution spaces.
* DE works well for multidimensional real-valued functions, not requiring differentiability, allowing application to non-continuous, noisy, or time-varying problem.

    .. figure:: Differential_Evolution_flow_chart.png
        :width: 224 px
        :align: center
        Figure 1: Differential Evolution (DE) is a type of evolutionary algorithm that optimizes a problem by iteratively improving a candidate solution with regard to a given measure of quality.
            Image credit: `Xiu Zhang <https://www.researchgate.net/publication/310811940_Shift_based_adaptive_differential_evolution_for_PID_controller_designs_using_swarm_intelligence_algorithm>`_


Algorithm overview and mechanics
================================
* DE maintains a population of candidate solutions, creating new ones by combining existing solutions using simple formulae.
* The algorithm operates as a black box, only requiring a measure of quality for candidate solutions.
* It's iterative, with the aim (not guarantee) of discovering a satisfactory solution.

  .. code-block:: text

      create a population of possible solutions
      loop
        for-each possible solution
          pick three random solutions
          combine the three to create a mutation
          combine curr solution with mutation = child
          if child is better than curr solution then
            replace current solution with child
          end-if
        end-for
      end-loop
      return best solution found





Initialization of agents
========================

DE starts with the random positioning of agents (candidate solutions) within the search-space:

.. math::

    X_i = X_{\text{min}} + \text{rand}(0,1) \cdot (X_{\text{max}} - X_{\text{min}})

where \( X_i \) represents the position of the \( i^{th} \) agent, \( X_{\text{min}} \) and \( X_{\text{max}} \) are the lower and upper bounds of the search space, respectively.



Mutation in DE
==============
Mutation involves the generation of a new candidate vector by the weighted difference between two random vectors added to a third vector:

.. math::

    V_i = X_{\text{r1}} + F \cdot (X_{\text{r2}} - X_{\text{r3}})

Here, \( X_{\text{r1}}, X_{\text{r2}}, X_{\text{r3}} \) are three distinct vectors randomly selected from the population, and \( F \) is the mutation factor.




Crossover process
=================

During crossover, a trial vector is created by mixing parameters from the mutated vector with those from a target vector:

.. math::

    U_{i,j} = 
    \begin{cases} 
    V_{i,j} & \text{if rand}(j) \leq CR \text{ or } j = \text{rand}(D) \\
    X_{i,j} & \text{otherwise}
    \end{cases}

  where \( CR \) is the crossover rate, and \( \text{rand}(D) \) ensures that \( U_i \) gets at least one component from \( V_i \).



Selection mechanism
===================

The selection mechanism is based on the fitness of the trial vector compared to the target vector:

.. math::

    X_i^{'} = 
    \begin{cases} 
    U_i & \text{if fitness}(U_i) \leq \text{fitness}(X_i) \\
    X_i & \text{otherwise}
    \end{cases}



Evolution and termination
=========================

The evolution process involves repeating the mutation, crossover, and selection steps until a termination criterion is met.

This provides a comprehensive overview of the DE algorithm, highlighting the mathematical concepts that underpin each step.

  .. image:: Differential_Evolution_optimizing_the_2D_ackley_function.gif
    :width: 224px
    :align: center

    Figure 2: The Differential Evolution (DE) algorithm is an iterative process that starts with a population of candidate solutions, and iteratively improves them by combining them with other solutions.
    Image credit: `Pablormier <https://pablormier.github.io/2017/09/05/a-tutorial-on-differential-evolution-with-python>`_


Advantages and challenges
=========================
* Advantages: DE's simplicity, efficiency in handling non-differentiable, noisy, or changing problems.
* Challenges: Parameter setting can be critical; it does not guarantee finding the global optimum.



Applications and recent advances
================================

* Global optimisation is necessary in fields such as engineering, statistics, and finance.
* Many practical problems have objective functions that are non-differentiable, non-continuous, non-linear, noisy, flat, multi-dimensional, or have many local minima, constraints or stochasticity.
* Such problems are difficult, if not impossible, to solve analytically.
* Differential Evolution (DE) can be used to find approximate solutions to such problems.



Differential evolution (DE) vs. Genetic algorithm (GA) on the Traveling salesman problem (TSP)
===============================================================================================

* DE has a higher computational complexity due to complex vector operations.
* GA converges faster but is more prone to premature convergence, often getting stuck at local optima.
* DE is slower to converge but is more stable and robust, often avoiding premature convergence.
* DE's approach is more computationally intensive but provides more consistent results towards global optima.
* GA can quickly find satisfactory solutions but may not be optimal.
* For larger TSP instances, DE tends to outperform GA in finding optimal solutions despite taking longer.
* credit: `Brian Hegerty, Chih-Cheng Hung, and Kristen Kasprak <http://www.micai.org/2009/proceedings/complementary/cd/ws-imso/88/paper88.micai09.pdf>`_
