**********************
Differential Evolution
**********************

Introduction to Differential Evolution (DE)
===========================================
* DE is a method in evolutionary computation that optimizes solutions to problem by iteratively improving a candidate solution based on a quality measure.
* It's a type of metaheuristic, making few assumptions about the problem, enabling exploration of large solution spaces.
* DE works well for multidimensional real-valued functions, not requiring differentiability, allowing application to non-continuous, noisy, or time-varying problem.

    .. figure:: Differential_evolution_flow_chart.png

        :width: 224 px
        :align: center
        Figure 1: Differential Evolution (DE) is a type of evolutionary algorithm that optimizes a problem by iteratively improving a candidate solution with regard to a given measure of quality.
            Image credit: `Xiu Zhang <https://www.researchgate.net/publication/310811940_Shift_based_adaptive_differential_evolution_for_PID_controller_designs_using_swarm_intelligence_algorithm>`_


Algorithm Overview and Mechanics
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
------------------------

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
-----------------

During crossover, a trial vector is created by mixing parameters from the mutated vector with those from a target vector:

.. math::

    U_{i,j} = 
    \begin{cases} 
    V_{i,j} & \text{if rand}(j) \leq CR \text{ or } j = \text{rand}(D) \\
    X_{i,j} & \text{otherwise}
    \end{cases}

  where \( CR \) is the crossover rate, and \( \text{rand}(D) \) ensures that \( U_i \) gets at least one component from \( V_i \).


Selection mechanism
-------------------

The selection mechanism is based on the fitness of the trial vector compared to the target vector:

.. math::

    X_i^{'} = 
    \begin{cases} 
    U_i & \text{if fitness}(U_i) \leq \text{fitness}(X_i) \\
    X_i & \text{otherwise}
    \end{cases}


Simple Example of Differential evolution
========================================

This section illustrates a basic application of Differential Evolution (DE) to optimize a simple mathematical function, specifically aiming to find the minimum value of a quadratic function \( f(x) = x^2 \).

Initialization
--------------

The process begins with initializing a population of candidate solutions:

.. math::

    P = \{x_1, x_2, x_3, x_4\}

where \( P \) represents the population, and each \( x_i \) is a randomly chosen value within a predefined range (e.g., -10 to 10).

Mutation
--------

Mutation involves creating a mutant vector for each candidate:

.. math::

    V = a + F \cdot (b - c)

where \( a, b, \), and \( c \) are distinct vectors randomly selected from the population, and \( F \) is a scaling factor (e.g., 0.8).

Crossover
---------

A trial vector is created by mixing elements from the mutant vector and the target vector:

.. math::

    T = \text{crossover}(V, x_i)

This step introduces variability, combining the mutated and target vectors.

Selection
---------

The trial vector is compared with the target vector, and the one with the better fitness value (lower \( f(x) \)) is retained:

.. math::

    x_i^{'} = 
    \begin{cases} 
    T & \text{if } f(T) < f(x_i) \\
    x_i & \text{otherwise}
    \end{cases}

Repeat
------

The mutation, crossover, and selection steps are repeated for several generations until a stopping criterion is met, such as a maximum number of generations or a satisfactory error threshold.

In this example, the DE algorithm iteratively adjusts the values of \( x \) in the population to find the one that minimizes \( f(x) = x^2 \). Over generations, the population of \( x \) values should converge towards 0, the point where the function attains its minimum value.



Evolution and Termination
=========================

* **Evolution Process:** 
  - The evolution process in Differential Evolution is a loop consisting of three main steps: mutation, crossover, and selection. Each of these steps plays a crucial role in navigating the search space and converging towards the optimal solution.

* **Termination Criteria:**
  - The termination of the DE algorithm is typically governed by one or more criteria, including:
    * Maximum Number of Generations: A common criterion is to stop the algorithm after a pre-defined number of generations have been completed.
    * Fitness Threshold: The algorithm can also terminate if a solution with a fitness value better than a defined threshold is found.
    * Stagnation: If there is no significant improvement in the population's fitness over a number of generations, the algorithm may terminate, indicating a possible convergence.
    * Resource Limitation: Constraints like computational time or memory usage can also be set as termination conditions.

  
  .. figure:: Differential_Evolution_optimizing_the_2D_ackley_function.gif
    :width: 500 px
    :align: center

    Figure 2: The Differential Evolution (DE) algorithm is an iterative process that starts with a population of candidate solutions, and iteratively improves them by combining them with other solutions.
    Image credit: `Pablormier <https://pablormier.github.io/2017/09/05/a-tutorial-on-differential-evolution-with-python>`_


Advantages and challenges
=========================


  .. image:: Differential_evolution_optimizing_the_2D_ackley_function.gif
    :width: 224px
    :align: center

    Figure 2: The Differential Evolution (DE) algorithm is an iterative process that starts with a population of candidate solutions, and iteratively improves them by combining them with other solutions.
    Image credit: `Pablormier <https://pablormier.github.io/2017/09/05/a-tutorial-on-differential-evolution-with-python>`_


Advantages and challenges
=========================

* Advantages: DE's simplicity, efficiency in handling non-differentiable, noisy, or changing problems.
* Challenges: Parameter setting can be critical; it does not guarantee finding the global optimum.



Types of Differential Evolution
===============================


* Global optimisation is necessary in fields such as engineering, statistics, and finance.
* Many practical problems have objective functions that are non-differentiable, non-continuous, non-linear, noisy, flat, multi-dimensional, or have many local minima, constraints or stochasticity.
* Such problems are difficult, if not impossible, to solve analytically.
* Differential Evolution (DE) can be used to find approximate solutions to such problems.

Adaptive Differential Evolution (ADE)
-------------------------------------
- **Characteristics:** ADE adjusts its strategy parameters, like the mutation factor (F) and crossover rate (CR), based on the performance feedback during the optimization process. This adaptability enhances its performance across diverse problems.
- **Applications:** Effective in problems where the landscape changes over time or is poorly understood.

Self-Adaptive Differential Evolution (SaDE)
-------------------------------------------
- **Characteristics:** In SaDE, the strategy parameters are encoded into the individuals themselves, allowing them to evolve alongside the solution. This leads to a more integrated and dynamic adaptation process.
- **Applications:** Useful in dynamic environments and in problems where the optimal parameter setting is not known a priori.

JADE (Adaptive DE with Optional External Archive)
-------------------------------------------------
- **Characteristics:** JADE introduces a learning mechanism for parameter adaptation and maintains an external archive for enhancing population diversity. It's known for its balanced exploration and exploitation capabilities.
- **Applications:** Works well with multi-modal functions and scenarios where maintaining diversity in the population is crucial.

Success-History Based Adaptive Differential Evolution (SHADE)
-------------------------------------------------------------
- **Characteristics:** SHADE uses historical data to adapt its parameters, making it more responsive to the problem's characteristics. This history-based approach improves convergence speed and solution quality.
- **Applications:** Particularly effective for complex, high-dimensional optimization problems.

Multi-Objective Differential Evolution (MODE)
---------------------------------------------
- **Characteristics:** MODE focuses on finding a set of optimal solutions (Pareto front) for problems with multiple conflicting objectives. It employs specialized selection and diversity maintenance strategies.
- **Applications:** Ideal for real-world problems involving trade-offs between two or more conflicting objectives, like engineering design problems.

Constrained Differential Evolution
----------------------------------
- **Characteristics:** This variant incorporates mechanisms to handle constraints, such as penalty functions, feasibility-based rules, or repair algorithms, ensuring that the solutions are viable in real-world scenarios.
- **Applications:** Suitable for optimization problems with specific constraints, such as resource limitations or design requirements.

Parallel and Distributed DE
----------------------------
- **Characteristics:** Utilizes parallel or distributed computing environments to enhance computational efficiency. It's capable of handling large-scale and computationally intensive optimization problems.
- **Applications:** Useful in scenarios with massive data sets or where the computational cost is prohibitively high for a single processor.

Hybrid DE
---------
- **Characteristics:** Combines DE with other optimization techniques, leveraging the strengths of each. This can lead to improved convergence rates and solution accuracies.
- **Applications:** Applicable in situations where a single algorithm may not be effective enough, such as highly complex or specialized optimization problems.

Conclusion
==========

In conclusion, Differential evolution (DE) has a wide range of applications and continues to advance, offering solutions to complex optimization problems. Its adaptability, robustness, and simplicity make it invaluable across various domains, while recent advancements further enhance its performance and scope. Understanding the diverse types of DE algorithms can aid in selecting the most suitable approach for specific optimization challenges.
