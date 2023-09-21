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

A total of 30 points may be obtained on this assignment. Although it is not required to complete all portions of the
assignment (one may choose to only try to obtain, for example, 20 points), all portions must be completed correctly and
effectively to receive all 30 points.

Below is a high-level overview of how points will be awarded. Details on each task are provided later in the assignment
description.

* A total of **5** points will be awarded for having a working implementation of the GA for TSP

    * A total of **5** additional points may be awarded for adding enhancements to the GA
    * Applying a GA to a more complex version of the problem, the *Vehicle Routing Problem*, will award **5** points
    * Generating an effective visualization for solutions may award up to **2** additional points

    * A complete report will award up to **5** points

        * Using LaTeX to generate the report will award an additional **2** points
        * Including proper references/citations awards an additional **2** points
        * Including figures and tables awards an additional **2** points
        * Performing an effective statistical analysis will award an additional **2** points


.. note::

    A working GA is required in order to obtain any points for the additional tasks described within the assignment.



Provided Files
==============

`Files containing JSON formatted TSP instances can be found on the github repository <https://github.com/jameshughes89/cs4XX-EvolutionaryComputation/tree/main/resources/tsp>`_

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


Python provides a simple way to load JSON files directly into dictionaries.

.. code-block:: python

    import json

    tsp_json = open(SOME_JSON_FILE)
    tsp_dictionary = json.load(tsp_json)


.. note::

    When implementing the GA, consider creating a distance matrix based on the list of coordinates. This way, the
    distances between each vertex only needs to be calculated once.



Implementing the Genetic Algorithm
==================================

The first portion of the assignment is to implement a GA for TSP. It does not matter how the GA is implemented as long
as the high-level framework of the algorithm is followed. Feel free to start from the GAs available on the GitHub
repository used for other problems. Being creative and experimental is encouraged, and further, this creativity will
provide plenty of content to discuss in the report.

Do not feel compelled to use the existing implementations of GAs that are in the repository. Additionally, the language
used does not particularly matter; however, if you would like to use a language other than C, C++, C#, Java, or Python,
please ask first for approval.

Make use of the provided TSP instances in JSON format. Also consider generating a distance matrix at runtime to reduce
the total number of distance calculations the GA has to do.

When running the GA for the purpose of gathering results, be sure to run it on a variety of instance of different sizes
(small, medium, large, and unreasonably large). Take note of everything you observe as this is worth discussing in the
report. `It is possible to find tables of the best known/optimal results online for the provided instances <http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/STSP.html>`_

Assuming the GA is working and there are no serious issues, **5** points will be awarded.


Enhancements and Modifications
------------------------------

A total of **5** additional points will be awarded for enhancing and modifying the GA. In general, each enhancement


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


