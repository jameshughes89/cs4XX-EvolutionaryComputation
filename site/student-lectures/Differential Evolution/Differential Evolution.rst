*******************************************
Introduction to Differential Evolution (DE)
*******************************************
* DE is a method in evolutionary computation that optimizes a problem by iteratively improving a candidate solution based on a quality measure.
* It's a type of metaheuristic, making few assumptions about the problem, enabling exploration of large solution spaces.
* DE works well for multidimensional real-valued functions, not requiring differentiability, allowing application to non-continuous, noisy, or time-varying problem.

    .. figure:: image_1_CSCI_340.png
        :width: 224 px
        :align: center

        Figure 1: Differential Evolution (DE) is a type of evolutionary algorithm that optimizes a problem by iteratively improving a candidate solution with regard to a given measure of quality.

******************
Algorithm Overview
******************
* DE maintains a population of candidate solutions, creating new ones by combining existing solutions using simple formulae.
* The algorithm operates as a black box, only requiring a measure of quality for candidate solutions.
* It's iterative, with the aim (not guarantee) of discovering a satisfactory solution.

  .. code-block:: none

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

*******************
Algorithm Mechanics
*******************
* Initialization of Agents:
  * DE starts by randomly positioning agents (candidate solutions) within the search-space. This random initialization allows for a diverse exploration of the solution space.
* Mutation in DE:
  * Mutation involves generating new candidates in the population. This is achieved by adding the weighted difference between two randomly selected vectors from the population to a third vector, creating a mutated vector.
* Crossover Process:
  * In the crossover step, parameters from the mutated vector are mixed with those of a target vector (another pre-determined agent) to produce a trial vector. This process contributes to the diversity of solutions.
* Selection Mechanism:
  * During selection, if the trial vector shows a lower cost function value (better fitness) compared to the target vector, it replaces the target vector in the subsequent generation. This ensures that only the fittest solutions are retained.
* Evolution and Termination:
  * The population evolves over generations, with each vector in the population serving as the target vector once per generation, ensuring NP competitions in each generation. The algorithm concludes based on specific termination criteria, such as reaching a predetermined number of iterations or achieving sufficient fitness.

****************
Parameters in DE
****************
* Critical parameters: Population size (NP), Crossover probability (CR), and Differential weight (F).
* The choice of these parameters significantly impacts optimization performance.
* Research has focused on finding optimal parameter settings for various problem.

*************************
Advantages and Challenges
*************************
* Advantages: DE's simplicity, efficiency in handling non-differentiable, noisy, or changing problems.
* Challenges: Parameter setting can be critical; it does not guarantee finding the global optimum.

********************************
Applications and Recent Advances
********************************

* Global optimisation is necessary in fields such as engineering, statistics, and finance.
* Many practical problems have objective functions that are non-differentiable, non-continuous, non-linear, noisy, flat, multi-dimensional, or have many local minima, constraints or stochasticity.
* Such problems are difficult, if not impossible, to solve analytically.
* Differential Evolution (DE) can be used to find approximate solutions to such problems.


*******************************
Conclusion and Future Direction
*******************************

* Summarize the strengths and potential of Differential Evolution (DE) in solving complex optimization problems.
* Discuss open research areas and future directions in the development of DE algorithms.

