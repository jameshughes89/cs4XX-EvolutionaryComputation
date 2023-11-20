.. _lecture:

Artificial Immune System
========================

**What is Artificial Immune Systems?**
--------------------------------------
   In artificial intelligence, artificial immune systems (AIS) are a
   class of computationally intelligent, rule-based machine learning
   systems inspired by the principles and processes of the vertebrate
   immune system. The algorithms are typically modeled after the immune
   system's characteristics of learning and memory for use in
   problem-solving.

   AIS emerged in the mid-1980s with articles authored by Farmer,
   Packard and Perelson (1986) and Bersini and Varela (1990) on immune
   networks. However, it was only in the mid-1990s that AIS became a
   field in its own right.

   Forrest et al. (on negative selection) and Kephart et al.[2]
   published their first papers on AIS in 1994, and Dasgupta conducted
   extensive studies on Negative Selection Algorithms.

.. image:: \image001.png
   :alt: Immune system response
   :align: center

This is how are immune system response

Now, we will learn about some terms :

.. image:: \image002.png
   :alt: Comparison between IS and AIS
   :align: center

**Framework of AIS**
--------------------
a.Recognition via regions of complementarity and Shape space(S)

b.Cross reactivity

.. note:: *How do we represent it mathematically?*

   Set of coordinates: m = (m1, m2, m3,….ml),m

   Ab = (Ab1, Ab2,….Abl), Ag = (Ag1, Ag2, …Agl)


Types of shape space:

    1.Hamming

    2.Euclidean

    3.Manhattan

.. image:: \image003.png
   :alt: distances
   :align: center


**Techniques which are inspired by the immune system**
------------------------------------------------------
.. image:: \image005.jpg
   :alt: Algorithms in AIS
   :align: center

**1.Clonal selection algorithm:** Clonal selection algorithms are
   most commonly applied to optimization and pattern recognition.

**2.Negative selection algorithm:** This class of algorithms are
   typically used for classification and pattern recognition problem
   domains where the problem space is modeled in the complement of
   available knowledge. For example, in the case of an anomaly detection
   domain the algorithm prepares a set of exemplar pattern detectors
   trained on normal (non-anomalous) patterns that model and detect
   unseen or anomalous patterns.

**3.Immune network algorithm:** This class of algorithms focus on
   the network graph structures involved where antibodies (or antibody
   producing cells) represent the nodes and the training algorithm
   involves growing or pruning edges between the nodes based on affinity
   (similarity in the problems representation space). Immune network
   algorithms have been used in clustering, data visualization, control,
   and optimization domains, and share properties with artificial neural
   networks.

**4.Dendritic cell algorithm:** The DCA is abstracted and
   implemented through a process of examining and modeling various
   aspects of DC function, from the molecular networks present within
   the cell to the behaviour exhibited by a population of cells as a
   whole. Within the DCA information is granulated at different layers,
   achieved through multi-scale processing.


**Clonal Selection Algorithm**
------------------------------
.. image:: \image006.png
   :alt: Clonal Algorithm
   :align: center

* **Initial population:** The first step is the initial population valuation. Each member of this set is called a chromosome.In this step a set of valid solutions for the problem is produced randomly, additionally, there is a memory that is called M and it exists beside this set. In each execution cycle, algorithm saves the best founded solution on its memory.

* **Affinity calculation:** Affinity calculation gives a chromosome as input and computes its fitness value. In fact, with the aim of this function we can compare two chromosomes. This function plays the role of fitness function operator in genetic algorithms. So at this step a value is computed for each chromosome that could be used as a measure for comparison of chromosomes with each other at the next steps.

* **Selection operator:** At this step existed chromosomes are sorted based on their affinities and among them chromosomes that have better affinity value are selected and other chromosomes are deleted. At this step the number of existed chromosomes of population decreases and only better chromosomes move to the next step.

* **Clonal selection:** After sending better chromosomes to the next step, each chromosome duplicates and the duplicated chromosomes are placed among new population. Clonal operation are determined based on the value of the correlation function for each chromosome meaning that the chromosome that has more affinity value is allowed to copy more samples of itself among population. So also in this step, number of existed chromosomes among population changes. The following formula shows the number of chromosomes among population: where NS is the number of selected population, Pi is the number of samples that ith chromosome can copy to the new population.

* **Maturity operator:** This function takes a chromosome as an input and with a change on that chromosome generates a new sample. In fact this operator is the substitute operator of mutation operator at genetic algorithms and is responsible for creating diversity at population.

In order to get more diversity among population, we use four different maturity operators:

   • **Random maturity:** in this operator, a gene of a chromosome is selected at random and its value is changed randomly

   • **Swap maturity:** in this operator, the places of two randomly selected gene of a chromosome are swapped.

   • **Creep maturity:** this maturity operator works by adding a small (positive or negative) value to selected gene. It means that this operator can change the value of a gene smoothly (increase or decrease).

   • **Scramble maturity:** the value of all genes of a chromosome changes completely randomly and the new chromosome is generated.


**Applications of AIS**
-----------------------
- **Cybersecurity and Anomaly Detection:**
  AIS are particularly well-suited for identifying unusual patterns or anomalies which makes them invaluable in cybersecurity. They can detect novel viruses, intrusions, or other cyber threats that deviate from normal network behavior.

- **Pattern Recognition:**
  In tasks involving the recognition of patterns or regularities in data, AIS algorithms excel due to their ability to learn and adapt. This is useful in image processing, voice recognition, and other areas where pattern detection is crucial.

- **Optimization Problems:**
  AIS algorithms like clonal selection are applied to complex optimization problems. They can find optimal or near-optimal solutions in areas like resource allocation, scheduling, and route planning.

- **Machine Learning and Data Mining:**
  AIS can be used in clustering and classification tasks, making them a valuable tool in machine learning and data mining. They help in segmenting data into meaningful groups or classifying data points into predefined categories.

- **Robotics:**
  In robotics, AIS can contribute to the development of autonomous systems that adapt to changing environments and tasks. They can be used for pathfinding, environment mapping, and decision-making processes in robotics.

- **Bioinformatics and Computational Biology:**
  AIS find applications in bioinformatics for tasks like gene expression analysis, protein structure prediction, and understanding complex biological networks.

- **Fault Detection in Systems and Networks:**
  Due to their ability to recognize deviations from the norm, AIS are used in monitoring systems and networks for fault detection. This is vital in ensuring the reliability and efficiency of industrial and telecommunication systems.

- **Healthcare and Medical Diagnostics:**
  In healthcare, AIS can assist in diagnostic procedures by identifying patterns in patient data that are indicative of specific diseases or conditions.

- **Financial Modeling:**
  AIS can be applied in the financial sector for predictive modeling, risk assessment, and anomaly detection in financial transactions.

- **Control Systems:**
  They are used in adaptive control systems for dynamic and uncertain environments, such as climate control in buildings or adaptive cruise control in vehicles.


**Experiment done using AIS** : https://www.scirp.org/journal/paperinformation.aspx?paperid=97654


**Conclusion**
--------------
AIS stands at a promising juncture. As we continue to unravel more intricacies of the immune system, the potential for more sophisticated and nuanced AIS algorithms grows. Challenges such as scalability and integration with other AI paradigms remain, but they also present opportunities for innovative research and development. The future of AIS, thus, holds the promise of not only advancing our computational capabilities but also deepening our understanding of one of the most complex biological systems.

In summary, Artificial Immune Systems, with their unique blend of biology and computation, continue to offer a rich domain for exploration and innovation, holding the potential to address some of the most challenging problems in the field of artificial intelligence and beyond.