********************************
Implementing a Genetic Algorithm
********************************

* The purpose of this topic is to see a simple genetic algorithm (GA)
* Although simple, it includes all the necessary parts to make it a complete GA
* Despite never seeing a GA before, or knowing the intuition behind the underlying ideas, the topic should be manageable



Problem
=======

.. note::

    The problem being *solved* is deliberately kept very simple. This is because (a) the purpose of this topic is to
    see a working GA, not solve a complex problem, and (b) well understood problems are often much simpler to reason
    about. Knowing what a good/bad solution is, and having an idea of why certain solving strategies work or not, will
    help with building the intuition around how GAs work.


* The problem being solved is to maximize the integer value of an unsigned binary number

    * Find the largest binary number representable with :math:`n` bits


* For this problem, the *search space* is all possible unsigned binary numbers of length :math:`n`

* Given this problem description, the best solution is obviously a string of :math:`n` ones
* Consider an example with :math:`n=10`, how would these candidate solutions be ranked in terms of *goodness*?

    * :math:`1111111111` (1023)
    * :math:`1011001001` (713)
    * :math:`0001111111` (127)
    * :math:`0000000000` (0)


* Thus, the GA being written will *evolve* bit strings to maximize the integer value of an unsigned binary number

* Realistically, one would not use a GA to solve such a problem

    * GAs are typically used for very challenging problems with no other effective means of solving


* However, this problem provides an opportunity to consider how the GA can and must work to find the best solution



Initialization
==============

* Before evolution can begin, an initial *population* of *candidate solutions* needs to be created
* A single candidate solution is a potential solution to the problem being solved
* For example, :math:`1011001001` is a valid candidate solution for finding the largest binary value where :math:`n=10`


Representation
--------------

* It is sometimes non-trivial to determine how a candidate solution should be represented, or encoded, in the program

    * An encoded candidate solution is called a *chromosome*


* For the integer maximization of an unsigned binary number, there are some obvious reasonable and simple encodings
* Here, a list of ``0``\s and ``1``\s will be used
* Thus, the candidate solution :math:`1011001001` can be encoded as the chromosome ``[1, 0, 1, 1, 0, 0, 1, 0, 0, 1]``

* A single chromosome can be created by generating random lists of ``0``\s and ``1``\s of some predetermined length

    * For the example used here, the length was :math:`n=10`


Population
----------

* A *population* is a collection of candidate solutions
* A population can be created by creating a list of randomly generated chromosomes

* In this example, a single chromosome is a list of ``0``\s and ``1``\s

    ``[1, 0, 1, 1, 0, 0, 1, 0, 0, 1]``


* A population is a list of chromosomes

    .. code-block:: text

        [[1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 1, 1, 0, 1, 0, 0, 0],
         [1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
         ...
         ...
         [0, 1, 1, 1, 1, 0, 0, 0, 0, 1]]


* Each chromosome is randomly generated
* Below is an example of how one could create a population for this problem

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-initialization]
    :end-before: # [end-initialization]


* The number of chromosomes within the population is defined by a hyperparameter called ``POPULATION_SIZE``
* The number of bits in the binary number (:math:`n`) is called ``BIT_STRING_LENGTH``



Evaluation
==========

* After generating the population, the candidate solutions are often not particularly *good*
* However, some will likely be better than others
* Regardless, a mechanism for evaluating the quality, or *fitness*, of candidate solutions is needed
* This mechanism is called the *fitness function*

* Below is an example fitness function for this problem

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :pyobject: value_fitness


* With this fitness function, the fitness of each candidate solution within the population can be calculated and stored

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-evaluation]
    :end-before: # [end-evaluation]



Selection
=========

* Ideally, more fit candidate solutions should be *more likely* to persist within the population

    * And less fit candidate solutions should be more likely to die off


* However, it is not as simple as always selecting the best candidate solutions

    * Doing so would cause the population to *converge* too early
    * This can result in finding sub-optimal solutions


* This is where it becomes important to think about the population, not individual candidate solutions
* The fitness function is a metric for the ultimate goal --- finding a *candidate solution* that best solves the problem
* But focusing on this metric is detrimental to the *population*
* Instead, the population should also emphasize *diversity*

* This can be done in any way someone wants

    * There are no hard rules on how selection is to be done


* A simple and popular selection technique is *tournament selection*

    * Randomly select a subset of chromosomes within the population
    * Select the best of the subset
    * Repeat until the next generation's population is full


.. literalinclude:: /../src/selection.py
    :language: python
    :lineno-match:
    :pyobject: tournament_selection


* This ``tournament_selection`` function returns a single chromosome
* This function must be run multiple times until the next generation's population is full

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-selection]
    :end-before: # [end-selection]


* In the above code, the list ``mating_pool`` will ultimately become the next generation's population
* The size of the tournament is defined by a hyperparameter called ``TOURNAMENT_SIZE``


Variation Operators
===================

* Variation operators, sometimes called genetic operators, are used to alter the chromosomes

    * With only selection, the chromosomes will never change


* Like most things with GAs, there are no real hard rules on how this is done
* Typically there should be a way to exploit what is already known to be good
* And there should be a way to add some new information to the chromosomes to better explore the search space


Crossover
---------

* Crossover is a variation operator that acts on two chromosomes
* The idea is, if two candidate solutions are relatively good, then mixing them together may produce something good

* Again, there is no one correct way to perform crossover
* A simple crossover one could use is ``one_point_crossover``

    * Given two chromosomes
    * Select an arbitrary index
    * Swap the contents of the chromosomes from that index to the end


* For example, selecting index ``2`` for the following chromosomes

    .. code-block:: text

               v                    v
        [0, 0, 0, 0, 0]      [0, 0, 1, 1, 1]
                         ->
        [1, 1, 1, 1, 1]      [1, 1, 0, 0, 0]
               ^                    ^


.. literalinclude:: /../src/crossover.py
    :language: python
    :lineno-match:
    :pyobject: one_point_crossover


* This function only returns two chromosomes, so it must be run multiple times

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :emphasize-lines: 2
    :start-after: # [begin-crossover]
    :end-before: # [end-crossover]


* Notice that the crossover is applied to adjacent candidate solutions within the ``mating_pool`` list

    * The fact that they are adjacent is arbitrary


* Also notice ``random() < CROSSOVER_RATE``
* Crossover is typically not always applied
* Thus, this provides a way for selected candidate solutions to persist in the next generation unchanged
* The probability of crossover being applied is defined by a hyperparameter called ``CROSSOVER_RATE``

    * Value would be ``0 <= CROSSOVER_RATE <= 1``


Potential Problem
^^^^^^^^^^^^^^^^^

* There is a potential problem with this crossover on this problem
* Consider the following population on a smaller version of the problem where :math:`n=5`

    .. code-block:: text

        [[1, 0, 1, 1, 1],
         [1, 0, 0, 0, 1],
         [0, 0, 1, 1, 1],
         [1, 0, 1, 1, 1],
         [0, 0, 0, 1, 0]]


* Notice how there exists no ``1`` in any of the chromosomes' index ``1``
* Because of this, it is actually not possible to ever find the optimal solution through crossover
* This is because there is no way to add new information to the candidate solutions
* It is only possible to transfer the existing information between the candidate solutions


Mutation
--------

* Mutation is a variation operator that acts on a single chromosome
* It is also great for adding new information to the candidate solutions

* Like crossover, there is no correct way to perform mutation
* Here, a ``bit_flip_mutation`` will be used

    * Given a chromosome
    * Select an arbitrary index
    * Flip the bit at the selected index (``0`` -> ``1``/``1`` -> ``0``)


* For example, selecting index 2 for the following chromosome

    .. code-block:: text

        [0, 0, 0, 0, 0]  ->  [0, 0, 1, 0, 0]
               ^                    ^


.. literalinclude:: /../src/mutation.py
    :language: python
    :lineno-match:
    :pyobject: bit_flip_mutation


* Similar to crossover, the application of mutation is probabilistic based on a hyperparameter called ``MUTATION_RATE``

    * Where ``0 <= MUTATION_RATE <= 1``


.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :emphasize-lines: 2
    :start-after: # [begin-mutation]
    :end-before: # [end-mutation]



Termination Requirement
=======================

* The above describes a single generation of the GA
* For this algorithm to work, many generations will need to be executed
* This then begs the question, *when does one stop the algorithm*

    * After some set number of generations?
    * After the optimal solution is found?
    * After there have been no improvements in the population?
    * ...


* Again, like most things with GAs, there really is no correct answer
* Here, for ease, the algorithm is run for some number of generations specified by the hyperparameter ``GENERATIONS``

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-generation-loop]
    :end-before: # [end-generation-loop]


* Notice that this generation loop performs

    * Evaluation
    * Selection
    * Variation Operators


* Also notice the bookkeeping variables storing some values from evolution

    * ``generation_max_fitness`` and ``generation_average_fitness``
    * These are not required, but help with visualizing what happened


* Also notice the tags like ``# [begin-evaluation]``

    * These can be ignored
    * They are only there for making it easier to reference the code in the course notes


* Once the loop terminates, the population should be evaluated one last time to find the best candidate solution

.. literalinclude:: /../src/ga_max_bitstring.py
    :language: python
    :lineno-match:
    :start-after: # [begin-ending]
    :end-before: # [end-ending]



For Next Class
==============

* Download and look at

    * :download:`The Selection Script </../src/selection.py>`
    * :download:`The Crossover Script </../src/crossover.py>`
    * :download:`The Mutation Script </../src/mutation.py>`
    * :download:`Bitstring GA </../src/ga_max_bitstring.py>`


