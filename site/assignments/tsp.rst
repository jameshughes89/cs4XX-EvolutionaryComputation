******************************
Travelling Salesperson Problem
******************************

* **Maximum Points**: 30
* **DUE**: Monday October 9, 2023 at 11:55pm; submitted on MOODLE.
* **Files**: `Files available on the GitHub repository <https://github.com/jameshughes89/cs4XX-EvolutionaryComputation/tree/main/resources/tsp>`_


Base Task
=========

The base task is to implement a Genetic Algorithm (GA) for the
`Travelling Salesperson Problem (TSP) <https://en.wikipedia.org/wiki/Travelling_salesman_problem>`_.



Marking Details
===============



Provided Files
==============

`Files containing JSON formatter TSP instances can be found on the github repository <https://github.com/jameshughes89/cs4XX-EvolutionaryComputation/tree/main/resources/tsp>`_

The instances were originally obtained from `TSPLIB <http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/>`_ but were
parsed to be in an easier to work with format --- JSON.

Only a subset of the TSPLIB files are provided --- those that contain 2D coordinates where the weights of the edges are
the Euclidean distance between vertices (cities).

Below is an example of a JSON file of a TSP instance. Only the first 27 lines of this file is shown.

.. literalinclude:: /../resources/tsp/a280.json
    :language: text
    :lineno-match:
    :lines: 1-27


The data is encoded similar to a dictionary.

    * ``"NAME"`` --- The name of the instance
    * ``"COMMENT"`` --- Some comment to go along with the instance
    * ``"TYPE"`` --- The type of the instance (all should be TSP)
    * ``"DIMENSION"`` --- The number of verticies (cities)
    * ``"EDGE_WEIGHT_TYPE"`` --- How the edge weight is calculated (all should be ``"EUC_2D"``)
    * ``"NODE_COORD_SECTION"`` --- A list of numbered coordinates

        * Each coordinate is encoded as a list containing the city number, x, and y coordinage
        * ``[n, x, y}``




Implementing the Genetic Algorithm
==================================


Enhancements
------------


Visualization
-------------


Vehicle Routing Problem
-----------------------



Report
======


LaTeX
-----


References and Citations
------------------------


Figures and Tables
------------------


Statistical Analysis
--------------------



What to Submit to Moodle
========================


