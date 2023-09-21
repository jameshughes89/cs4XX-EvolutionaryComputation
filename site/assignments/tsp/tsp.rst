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

A total of **5** additional points will be awarded for enhancing and modifying the GA. In general, each
enhancement/modification will award **1** additional point, but depending on the complexity of the
enhancement/modification, additional or fewer points may be awarded. To be safe, do not aim to put in minimal effort
to obtain these marks if the goal is to obtain all **5** additional points.

The enhancements/modifications must be made clear to the marker as they will not dig through the implementation to try
to find what was done. If choosing not to write a report, at least provide a text file containing a description of what
was done. If writing a report, add a section within the report outlining what was done. If the
enhancements/modifications are not clear, points may not be awarded.

Below is a short list of possible enhancement/modifications

    * Elitism
    * New or modified genetic operators
    * New or modified selection
    * Adding additional heuristics to the search
    * Adding a new operation to the algorithm



Visualization
-------------

Having the GA generate a visualization of results will provide an additional **2** points. How this is done is up to
each individual, but ensure it is interesting, effective, clear, and well presented to ensure the points are awarded.
The more creative the better.

For example, having a final static visualization of a route is *fine*, but not particularly interesting. It would be
better if the GA periodically presents the best path or a set of paths from the population. If planning on doing this in
real time, it is not recommended to have this happen for each generation as it would take a very long time. Instead,
perhaps only show the visualization every so often or save images to create an animation after evolution is done.

Do not feel that visualizing the routes is the only option. It could be a visualization of some mechanism within the GA,
or maybe something entirely different. Like already mentioned, the more creative the better.


Vehicle Routing Problem
-----------------------

If a GA is also applied to the *vehicle routing problem*, **5** additional points may be obtained. Be sure to have a
working TSP implementation before attempting this more complex problem. Points will only be awarded for a complete and
working implementation of a GA for the vehicle routing problem

The vehicle routing problem is, to describe it briefly, a generalization of TSP that is multi-objective (more than one
value needs to be optimized). Expect it to be non-trivial to apply a GA to. There are several variations of this
problem, so feel free to attempt any of the variations.

If this is being attempted, search for data and be sure to obtain problem instances of various sizes. It may also be
possible to find tables of best known results online.

`The Wikipedia article for the vehicle routing problem provides a description of the problem <https://en.wikipedia.org/wiki/Vehicle_routing_problem>`_.
Be sure to read through the article if this problem is being attempted.




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

* Submit everything via Moodle by 11:55pm on the due date
* Include the full implementation of the GA along with any special running instructions if necessary
* Include the report
* Include anything else the marker may need for effectively evaluating the work

