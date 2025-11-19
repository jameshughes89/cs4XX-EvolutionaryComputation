***************************
Particle Swarm Optimization
***************************

* **Maximum Points**: 25
* **DUE**: Monday December 1, 2025 at 11:55pm; submitted on MOODLE.

.. warning::

    Claiming that objectives/tasks/enhancements were complete within the report when in reality they were not is (a) a
    serious form of academic misconduct --- falsifying results --- and (b) against the student code of conduct.

    These violations are subject to severe penalty. All violations will be reported and investigated fully.



Base Task
=========

The base task is to implement Particle Swarm Optimization (PSO) to be run on a series of
`test optimization functions <https://en.wikipedia.org/wiki/Test_functions_for_optimization>`_.


Marking Details
===============

A total of 25 points may be obtained on this assignment. Although it is not required to complete all portions of the
assignment (one may choose to only try to obtain, for example, 20 points), all portions must be completed correctly and
effectively to receive all 25 points.

Below is a high-level overview of how points will be awarded. Details on each task are provided later in the assignment
description.

* A total of **4** points will be awarded for having a working implementation of PSO for the test functions

    * A total of **3** additional points may be awarded for adding enhancements to the PSO algorithm
    * Using PSO for a multi-objective problems may award an additional **4** points
    * Generating an effective visualization for evolution/solutions may award up to **2** additional points

    * A complete report will award up to **4** points

        * Using LaTeX to generate the report will award an additional **2** points
        * Including proper references/citations awards an additional **2** points
        * Including figures and tables awards an additional **2** points
        * Performing an effective statistical analysis will award an additional **2** points


.. note::

    A working PSO implementation is required in order to obtain any points for the additional tasks described within the
    assignment.



Provided Files
==============

No files are provided, however, a series of test optimization problems can be found on
`Wikipedia <https://en.wikipedia.org/wiki/Test_functions_for_optimization>`_.



Implementing Particle Swarm Optimization
========================================

The first portion of the assignment is to implement PSO for various test optimization problems. It does not matter how
PSO is implemented as long as the high-level framework of the algorithm is followed.

Feel free to start from the PSO implementations available on the GitHub repository. Being creative and experimental is
encouraged, and further, this creativity will provide plenty of content to discuss in the report.

Do not feel compelled to use the existing implementations of the PSO that are in the repository. Additionally, the
language used does not particularly matter; however, if you would like to use a language other than C, C++, C#, Java, or
Python, please ask first for approval.

Assuming the PSO implementation is working and there are no serious issues, **4** points will be awarded.


Enhancements and Modifications
------------------------------

A total of **3** additional points may be awarded for enhancing and modifying the PSO implementation. In general, each
enhancement/modification will award **1** additional point, but depending on the complexity of the
enhancement/modification, additional or fewer points may be awarded. To be safe, do not aim to put in minimal effort
to obtain these marks if the goal is to obtain all **3** additional points.

The enhancements/modifications must be made clear to the marker as they will not dig through the implementation to try
to find what was done. If choosing not to write a report, at least provide a text file containing a description of what
was done. If writing a report, add a section within the report outlining what was done. If the
enhancements/modifications are not clear, points may not be awarded.

Below is a short list of possible enhancement/modifications:

    * Charged PSO
    * Applying speed limits
    * Bounding the search space
    * Using Pareto-Sets on multi-objective problems


Visualization
-------------

Generating a visualization of results may provide an additional **2** points. How this is done is up to each individual,
but ensure it is interesting, effective, clear, and well presented to ensure the points are awarded. The more creative
the better.


Multi-Objective Optimization
----------------------------

An additional **4** points may be awarded if PSO is used on multi-objective problems.
`The Wikipedia article contains several multi-objective problems to choose from <https://en.wikipedia.org/wiki/Test_functions_for_optimization>`_.



Report
======

Writing a simple report will award up to **4** additional points; however, a total of **12** points may be obtained by
completing all portions of the report sufficiently.

.. warning::

    Writing a report is non-trivial and will likely take much longer than implementing the algorithm.


The base report will consider spelling, grammar, prose, etc. for marking, thus, the marker will be analysing the report
both quantitatively and qualitatively.

There is no *right* way to write a report, nor is there a definitive structure. The most correct way is to write a
report that most effectively communicates what needs to be communicated.

Below is a list of things to consider including in the report. This list is a collection of suggested ideas to consider
and is not intended to be the standard template.

* Introduction

    * What is the problem?
    * Small literature review

        * What have other people done in the past that worked


* Problem description

    * What is the point of the test problems?
    * If applicable, what are multi-objective problems?


* Algorithm description

    * How was PSO implemented?

        * Can someone follow the description to recreate your work?


    * What enhancements/modifications were included?

        * Why were they done?
        * How were they done?


* Explain how the results will be analysed

    * What is being compared?
    * How will the comparison be done?

        * Mean
        * Distribution comparison
        * Probability values?


* Explains the results and discuss

    * What happened?
    * How would this compare to random?
    * How would this compare to other algorithms?
    * How were the results compared to the best known?
    * Did any of the implemented modifications or enhancements improve the results?


* Conclusions and possible future directions

    * What are the major takeaways?
    * How good was it?
    * What else could be done as next steps for continuing the analysis?


* Bibliography

    * References, if included


LaTeX
-----

An additional **2** points may be obtained if the report is written in LaTeX.

LaTeX is powerful software for writing and typesetting documents. Everything is written in plain text with various tags
that LaTeX will use to format the document nicely.

Although it is possible to download, write, and build everything locally on a personal computer, it is highly
recommended to use `Overleaf <https://www.overleaf.com/>`_. Overleaf is an online editor that takes care a lot of
tedious setup and it automatically backs up all work.

If using LaTeX, it is recommended that the report be written with the
`IEEE <https://www.overleaf.com/latex/templates/ieee-conference-template/grfzhhncsfqn>`_  conference template. Overleaf
makes it simple to start using the template.

Although it is possible to write the bibliography in the document with ``\bibitem``, it is far simpler to use
`BibTeX <https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex>`_.

Although LaTeX and BibTeX is not being taught, it should not be too difficult to get used to it with the help of
tutorials and examples available online.


References and Citations
------------------------

Including effective and proper references/citations may award an additional **2** points.

There is no correct number of references to include as that depends on the report itself.

LaTeX and BibTeX makes references and citations relatively simple. Further, with
`Google Scholar <https://scholar.google.com/>`_, getting references correct is trivial.


Figures and Tables
------------------

Effectively including figures, tables, etc. in the report may award an additional **2** points. Examples include an
algorithm flow diagram, a table of parameter settings, tables of results, result visualization, learning curves,
distributions of results, etc.

.. note::

    The tables and figures must effectively communicate relevant information. For example, a giant table of results is
    difficult to interpret. Instead, think of how the data can be represented succinctly and clearly.


Statistical Analysis
--------------------

Including proper statistical comparisons of results may award an additional **2** points.

Typically, different results will be obtained every time the algorithm is run. This is due to the stochastic nature of
these algorithms. For this reason, it is not possible to run these algorithms once to compare the results. Instead,
*distributions* of results need to be obtained and these distributions are then compared to one another.

In evolutionary computation, it is common to see 30 runs of each algorithm to obtain the distributions (30 runs of the
same algorithm with the same setup and hyperparameters).

It is not possible to say which statistical methods should be used for the analysis as that depends on what the goal is.
Below is a general guideline.

    * General summary statistics for each distribution

        * Mean, standard deviation, etc.


    * Comparing distributions

        * Student t-test or Mann-Whitney U


    * Measuring the difference between distributions (effect)

        * Cohen's D test



What to Submit to Moodle
========================

.. warning::

    Completing a requirement does not guarantee that the corresponding points will be awarded. Each requirement must be
    completed to the satisfaction of the marker.


* Submit everything via Moodle by 11:55pm on the due date
* Include the full implementation of PSO along with any special running instructions if necessary
* Include the report
* Include anything else the marker may need for effectively evaluating the work

