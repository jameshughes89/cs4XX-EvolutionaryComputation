*******************
Project Description
*******************

* **Maximum Points**: 30
* **Topic Selection Due Date**: October 25, 2023, submitted via email
* **PR Merge Date**: If Applicable, At Least One Day Before the Lecture Date
* **Presentation Date**: November 28th -- December 6th
* **DUE**: Wednesday December 6th, 2023 at 11:55pm; submitted on MOODLE.



Base Task
=========

* Select a topic for a project
* Implement the project idea
* Produce a report or give a presentation
* Submit the final implementation
* Groups of up to two are permitted



Marking Details
===============

A total of 30 points may be obtained for the project. Although it is not required to complete all portions of the
project (one may choose to only try to obtain, for example, 20 points), all portions must be completed correctly and
effectively to receive all 30 points.

Below is a high-level overview of how points will be awarded. Details on each task are provided later in the assignment
description.

* A total of **10** points will be awarded for having a working implementation of the project topic

    * **10** additional points may be awarded for enhancements/modifications, novelty, interesting-ness, analysis, etc.


* A total of **10** additional points may be awarded for completing a project presentation *or* report

    * A project presentation will award up to **4** points

        * Including proper references/citations awards an additional **2** points
        * Including figures and tables awards an additional **2** points
        * Performing an effective statistical analysis will award an additional **2** points


    * A complete report will award up to **2** points

        * Using LaTeX to generate the report will award an additional **2** points
        * Including proper references/citations awards an additional **2** points
        * Including figures and tables awards an additional **2** points
        * Performing an effective statistical analysis will award an additional **2** points


.. note::

    Points will be awarded for *either* a project presentation *or* a final report. In other words, it is only necessary
    to complete one of the two options (presentation or report).


Project Topics
==============

It is the students' responsibility to select a project topic and have it approved by the instructor. Once approved, the
project direction is up to the students. Students are encouraged to be creative and ambitious. Further, marks will not
be lost due to the quality of the final results.

Most project ideas fall under one of the following categories:

    * Application --- Apply an algorithm to a particular problem of interest
    * Enhancements/Modifications --- Implement a novel idea into an algorithm and analyze results
    * New Algorithm --- Create a new algorithm tha follows the high-level idea of evolutionary computation


Do not be afraid to try something different. The instructor values creativity will make every attempt to be as accepting
of project ideas as possible.

Topics will be selected on a first-come first-served basis, however, if multiple groups want to do the same project, the
instructor will work the the groups to direct them such that the details differ between groups.

All topic choices, along with preferred presentation date (if choosing to give a presentation) are to be submitted to
the instructor via email.


Modifications, enhancements, novelty , etc.
-------------------------------------------

How the points for the modifications, enhancements, etc. are awarded will depend heavily on the specific project. Thus
it is difficult to be specific about how the points will be awarded. As a starting place, consider that the points will
be awarded for a combination of modifications, enhancements, novelty, analysis, interesting-ness, etc.

Like with most aspects of the course, the instructor and marker will be looking for excuses to award points to students
for their work. In other words, be creative, emphasize what is felt to be worth points, and make clear *why* it is felt
that what was done is worth the points.



Report
======

Writing a simple report will award up to **5** additional points; however, a total of **13** points may be obtained by
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

