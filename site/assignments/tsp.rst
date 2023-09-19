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
    * ``"TYPE"`` --- The type of the instance

        * All should be ``"TSP"``


    * ``"DIMENSION"`` --- The number of vertices (cities)
    * ``"EDGE_WEIGHT_TYPE"`` --- How the edge weight is calculated

        * All should be ``"EUC_2D"``
        * This means the weight of each edge is the Euclidean distance between the vertices


    * ``"NODE_COORD_SECTION"`` --- A list coordinates

        * Each coordinate is encoded as a list containing the city number, x, and y coordinate

            * ``[n, x, y]``

        * This is the value that will be used for calculating the distance of a Hamiltonian cycle
        * The length of this list should be equal to the instance's ``"DIMENSION"``
        * For implementing the GA for TSP, consider pre-calculating a distance matrix from the list of coordinates


Python provides a simple way to load JSON files directly into dictionaries.

.. code-block:: python

    import json

    tsp_json = open(SOME_JSON_FILE)
    tsp_dictionary = json.load(tsp_json)



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


