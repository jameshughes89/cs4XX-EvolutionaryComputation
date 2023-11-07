**************
Novelty Search
**************

    "... almost like a riddle, novelty search suggests a surprising new perspective on achievement:
    To achieve your highest goals, you must be willing to abandon them."

    - Joel Lehman and Kenneth O. Stanley [1]_



Evolutionary Computation is Hard
================================

Conventional evolutionary computation techniques typically define an objective (or fitness) function, which in turn
defines the topology of the search space. The algorithm's task then is to curate a population that will allow it to
traverse this space in the pursuit of finding a global optimum.

The problem that frequently arises is that the population gets "stuck" around local optima and cannot progress past them
to explore new areas of the search space - so-called *early convergence*.

For example, imagine the algorithm's task is to solve a maze. It is presented with the following maze:

    .. figure:: simple_maze_walls.png
        :width: 223 px
        :align: center

        A very simple maze. The starting point is the red dot, the objective is the green dot.

A sensible objective function for the maze solver could be *distance to the objective*.

While evolutionary computation doesn't *always* take the greedy solution of simply moving towards the objective, it does
reward individuals in the population who get closer. Effectively, it rewards that behavior *more often than not*.

So, it is entirely possible that the computation will reach a point where it has a population clustered around the dead
end - the local optimum - and that attempts to vary that population will fail to move it away towards a new area in the
search space.



Stepping Stones
---------------

While this is an oversimplified toy problem, this is a fundamental problem that appears again and again in evolutionary
computation. The obvious intuition to a human observer is that the maze finder first had to move down - *against* the
direction of its objective function - into a new area. Only then would resuming pursuit of the objective function be
helpful.

    .. figure:: stepping.png
        :width: 224 px
        :align: center

        The maze with two stepping stones drawn in blue. The first stepping stone is in the opposite direction of the
        objective function, while the second stepping stone is mostly orthogonal to the objective function.

The point further down that had to be reached on the way to the global optimum is called a *stepping stone*. Traditional
evolutionary computation can sometimes fail when the objective function points *away* from the stepping stones rather
than *towards* them. This can happen often, because the objective function has no way of knowing what the stepping
stones are and no way of rewarding them.

While identifying stepping stones for a specific problem is possible with the application of domain knowledge, there is
no easy way to identify them in general. Fundamentally, the act of finding the stepping stones *is* the problem that
needs to be solved. If finding them was trivial, you wouldn't even need to be doing evolutionary computation in the
first place.



Deception
---------

A problem for which a sensible objective function often leads away from the stepping stones is called *deceptive*.
In a nutshell, deception is the reason why evolutionary computation is hard. Much of the work of creating better
evolutionary algorithms boils down to thinking of different ways to overcome deception.

While the many techniques for overcoming deception are interesting, the problem that presents itself is that not all
techniques work equally well for all problems. The exact nature or workings of the deception may vary, and it is
possible that *none* of the currently known techniques may be effective for a given problem.

So, the question arises: What do we do when, despite our best efforts, our attempts at making use of an objective
function persistently lead us astray?



Novelty Search
==============

    .. figure:: stepping.png
        :width: 419 px
        :align: center

        An example of the difference between a traditional fitness based search and a novelty search. [1]_

It is important to realize that using a fitness function to solve problems was in fact a *choice*. While it is very
often a good and sensible choice, in the case of a highly deceptive problem it may be best to re-evaluate the assumption
that using fitness to guide search was a good idea.

    "The best way to solve any problem is to remove its cause."

    - Martin Luther King, Jr

But what are the alternatives? Random search certainly will not be an acceptable solution to many problems. So it is
true that we do need *something* to guide the search. In particular, is there an alternative approach that would guide
search towards finding those elusive stepping stones?

Consider the following thought experiment: Imagine an evolutionary algorithm just performed mutation on some individual.
According to a traditional objective based search, there are three categories of outcome:

* The fitness of the individual is now higher. (Good)
* The fitness is now lower. (Bad)
* The fitness is now relatively unchanged. (Neutral)

Imagine though that a mutation was neutral - *but* created a new individual that represented something *very different*
from anything seen before. Is that really a neutral outcome?

    .. figure:: saddle.png
        :width: 600 px
        :align: center

No!

That neutral change brought us to an unexplored area of the search. It, or neighbours near it, may well be one of the
stepping stones our search needs to find. Intuitively, it makes sense that a search that would reward such a mutation
could be beneficial.

In practice, a novelty based search algorithm is very similar to a traditional fitness based search, with two key
differences.



The Archive
-----------

An individual's fitness can be evaluated in isolation. An individual's *novelty* however, requires considering how it
compares to the *entire* population. Not only that, but for something to be novel, it has to be different from the
population of *all* past populations.

That is obviously not a practical approach, since it grows unbounded both in terms of time and memory complexity.
Without considering the past though, it is possible that the search could alternate between rediscovering the same
supposedly novel solutions and stop venturing out further into the search space.

    .. figure:: archive.png
        :width: 600 px
        :align: center

    Think of each individual as being a researcher striving to get some new finding interesting enough to be published.
    Photo credit: `Niklas Ohlrogge <https://unsplash.com/@ohlrogge>`_

The compromise to be made is remembering *some* of the past - this is called the *archive*. When an individual from the
population achieves a sufficiently high novelty score, it is enshrined in the archive. The novelty of an individual is
compared against the population *and* the archive. The archived individuals in effect "push" the population away from
that part of the search space during selection, guiding the search towards unexplored parts of the space.



The Novelty Metric
------------------

Similar to an objective search based on fitness, in practice in order to perform a search based on novelty a novelty
function needs to be defined. What exactly that function will be is dependent on the problem at hand, and finding a good
function may be non-trivial, or perhaps impossible. In such cases, a novelty search would not be a successful approach.

    The aim is to characterize how far away the new individual is from the rest of the
    population and its predecessors in behavior space, i.e. the space of unique behaviors.
    A good metric should thus compute the sparseness at any point in the behavior space.
    Areas with denser clusters of visited points are less novel and therefore rewarded
    less.

    A simple measure of sparseness at a point is the average distance to the k-nearest
    neighbors of that point, where k is a fixed parameter that is determined experimen-
    tally. [1]_

Or, as an equation:

.. math::

   ρ(x) = \frac{1}{k} \sum_{n=1}^{k}dist(x, μi)

Or, as a picture:

    .. figure:: sparsity.png
        :width: 600 px
        :align: center

    The points on the right are generally in more *sparse* regions of the space than the points on the left.
    Image credit: `Sean Lie <https://www.cerebras.net/blog/harnessing-the-power-of-sparsity-for-large-gpt-ai-models>`_

For the maze problem, distance in behavior space could be represented as the distance between the final points of
different individuals. In other words, solutions that end in different places represent different behaviors.

.. note::

    Distance in behavior space is a much broader conceptual idea than just things that can be represented as physical
    distances. For example, for the problem of symbolic regression using genetic programming, you could shrink the
    encoding down to just a single string where each letter represents a node value (such as '+' or '5') and then
    consider the edit distance between two strings.



Potential Problems
==================

While novelty search is an interesting concept, a clever observer might have thought of a few things that might present
challenges for such an approach. Some of these will be discussed below.



Unbounded Domain
----------------

Recall the example of the basic maze:

    .. figure:: simple_maze_walls.png
        :width: 223 px
        :align: center

        A very simple maze. The starting point is the red dot, the objective is the green dot.

Novelty search is able to succeed here because after exploring the dead end and the surrounding area, it is inevitable
that the search will eventually begin to favor exploring the area around the goal.

But what happens if we remove the walls?

    .. figure:: simple_maze.png
        :width: 224 px
        :align: center

        The maze without walls.

If the x and y dimensions are unbounded - that is to say the potential area to explore is infinite - intuitively, there
is no assurance that the search will be guided towards the solution. It would be possible to endlessly discover novel
solutions in farther and farther regions of the space.

In order to prevent this behavior, it is necessary to impose artificial domain restrictions on the problem. This is not
ideal, since it requires application of problem specific knowledge. Furthermore, if the global optimum lies *outside*
the artificial domain restrictions, the algorithm was doomed before it began.



Unoptimized Solutions
---------------------

The ending result of a novelty search is a collection of novel points. While hopefully the global optimum is *near* one
of those points, it is perhaps unlikely that one of the points will achieve it exactly.

    .. figure:: unoptimized.png
        :width: 600 px
        :align: center

        A potential solution that is clearly in need of being further optimized.

What the solutions provided by a novelty search provide are good *starting* points for a traditional objective based
search. In other words, they may require some fine-tuning. This can be achieved by evaluating them and performing an
objective based search around the objectively best novel solution. Alternatively, you could take the approach of
beginning with a multi-objective search for novelty *and* fitness.



Increasing Time and Space Complexity
------------------------------------

The fact that evaluating novelty relies on comparing each individual to every other individual is already a bitter
prospect, since it means the time complexity of the search scales with the size of the population squared. In contrast,
conventional objective search would only have linear scaling.

If the length of the archive is allowed to grow though, it is actually even worse. As the computation progresses there
will be more and more elements in the archive to compare against. This means that the novelty metric becomes
progressively harder to evaluate.

    .. figure:: bookshelf.png
        :width: 600 px
        :align: center

        A smaller archive.
        Image credit: `Darren Richardson <https://unsplash.com/@campfire_guy>`_

To prevent that, the size of the archive would have to be fixed. A simple way of doing this would be to have the archive
be a fixed length queue. Then the question arises: Is an archive of fixed length still effective for preventing patterns
of rediscovery after old members of the archive are lost? The answer will depend on the length of the archive, and how
deceptive the problem is.



Lengthening the Behavioral Characterization
-------------------------------------------

In the maze example, the behavior space was characterized as where the solution ended up. That may have worked for the
simple maze problem, but what about a problem where describing the behavior is more complex? In other words, what if the
dimensionality of the characterization was larger? Does the novelty search as a method scale well in such situations?

While this is not an easy question to answer in general, here is one scenario from work by Lehman and Stanley [1]_:

    .. figure:: dimensionality.png
        :width: 278 px
        :align: center

        Examining the effect of increasing dimensionality of the behavioral characterization.

In that example, they found that this did not have a detrimental effect on the search. Intuitively, this makes sense.
Each dimension of the characterization is essentially an opportunity to explore novelty. Even if some of them are
unproductive (searching there does not find novelty), the search will focus on the areas that *do* yield novelty.



Reducing the Precision of the Behavioral Characterization
---------------------------------------------------------

In the maze example, the behavior space was represented by a coordinate, which was a real number. Real numbers allow
for minute differences in behavior. It is possible though that a problem might need a characterization that is discrete.
In such a case, can novelty search still perform well?

    .. figure:: discrete.png
        :width: 600 px
        :align: center

    As the precision decreases, larger areas of the behavior space are conflated as being the same single point.
    The novelty metric is unable to distinguish between different behaviors that are in the same grid.

Again, the answer here is not clear in general, but Lehman and Stanley had the following finding [1]_:

    .. figure:: precision.png
        :width: 306 px
        :align: center

        Examining the effect of decreasing precision of the behavioral characterization.

In all but the most extreme cases, they found that the search still performed well. What happens here is that although
the discretization conflates some regions into a single point, it still preserves the fact that the adjacent regions are
*more* distant and still rewards exploring other sectors. In essence, it still preserves the property of finding the
necessary stepping stones.

In the extreme cases where the loss of precision was so great that the algorithm cannot go from searching in one region
to searching in a necessary adjacent stepping stone region, the search will fail.



Conclusion
==========

Using a novelty metric is an alternative way to guide a search. For highly deceptive problems, such an approach might
be more successful at finding the necessary stepping stones to move towards a global optimum.

    "While novelty search is not a panacea, the more salient point is that objective-based
    search, which is ubiquitous in EC, clearly does not always work well. The implica-
    tion is that while it seems natural to blame the search algorithm when search fails
    to reach the objective, the problem may ultimately lie in the pursuit of the objective
    itself."
        -  Joel Lehman and Kenneth O. Stanley [1]_

.. note::

    Novelty search isn't just about computer algorithms, we as humans also perform searches in our lives!

    Say you are on a lifelong journey to find the tastiest food, and you just tried a Jamaican dish for the first time.
    If it was terrible, you might decided to never try Jamaican cuisine again. That would be the objective approach.

    But maybe some other Jamaican dishes are really good! It could be an area worth more exploration.

.. figure:: food.png
    :width: 600 px
    :align: center

    Image credit: `Stefan Vladimirov <https://unsplash.com/@vladimirov>`_



----------------------

.. [1] `Abandoning Objectives: Evolution through the Search for Novelty Alone <https://www.cs.swarthmore.edu/~meeden/DevelopmentalRobotics/lehman_ecj11.pdf>`_
