Speedrun Optimization with Evolutionary Computation
===================================================

Introduction
------------

- **Definition**: Speedrunning is the practice of completing a video game as quickly as possible, with various categories and strategies.

- **Popularity**: Speedrunning has gained immense popularity on platforms like Twitch and YouTube.

- Different speedrun categories include Any%, 100%, and Glitchless, each with unique challenges and strategies. Techniques such as glitches, exploits, and sequence breaks are commonly employed.

- Optimizing speedruns is crucial due to the competitive nature of the community. Players constantly push boundaries to outperform each other, creating a sense of camaraderie and excitement.

Strategies
----------

The optimization of speedrun routes in video games often involves the application of evolutionary computation strategies. The choice of strategy depends on the specific characteristics and challenges posed by the game. Here are several evolutionary computation strategies that can be considered for optimizing speedrun routes:

- Genetic Algorithms (GA)

**Overview:**
    Genetic algorithms are a versatile optimization technique inspired by the process of natural selection. They involve evolving a population of potential solutions over several generations.

**Application:**
    GAs can be applied to optimize speedrun routes by representing routes as individual solutions. The genetic operators (crossover, mutation) can be used to explore and exploit different sequences of actions, improving the overall efficiency of the route.

- Ant Colony Optimization (ACO)

**Overview:**
    ACO is inspired by the foraging behavior of ants. It involves simulating the way ants leave pheromone trails to discover optimal paths to a food source.

**Application:**
    In the context of speedrunning, ACO can be adapted to represent paths or sequences of actions. Pheromones could represent the attractiveness of certain paths, guiding the algorithm to focus on more promising routes.

- Particle Swarm Optimization (PSO)

**Overview:**
    PSO is inspired by the social behavior of birds flocking or fish schooling. It involves a population of particles that explore the solution space by adjusting their positions based on their own experience and the experience of their neighbors.

**Application:**
    PSO can be applied to speedrunning by representing each particle as a potential speedrun route. The particles adjust their positions (routes) based on their success in reaching the goal quickly, and this information is shared with neighboring particles.

- Evolutionary Strategies (ES)

**Overview:**
    Evolutionary strategies are a family of optimization algorithms that focus on directly evolving the parameters of a solution.

**Application:**
    In speedrunning, ES could be used to evolve the parameters of a route directly. For example, it might evolve the timing and sequence of actions, allowing for a more direct optimization of the execution of the speedrun.

- Simulated Annealing

**Overview:**
    Simulated annealing is a probabilistic optimization algorithm inspired by the annealing process in metallurgy. It allows the algorithm to escape local optima by accepting less optimal solutions with a certain probability.

**Application:**
    Simulated annealing can be applied to speedrunning by representing routes as solutions. The algorithm explores the solution space and occasionally accepts less optimal routes, preventing it from getting stuck in local minima.

- Neuroevolution

**Overview:**
    Neuroevolution involves evolving neural networks to solve problems. In the context of speedrunning, it could be used to evolve controllers or decision-making mechanisms for the player character.

**Application:**
    The algorithm evolves neural networks that determine the actions of the player character in the game. This can lead to adaptive strategies that adjust to different in-game conditions.



Poly Bridge
-----------

    .. figure:: gifpb.gif
        :align: center


- Poly Bridge, a bridge-building simulation-puzzle game. The main goal is to create functional bridges for vehicles to cross. Using a 2D bridge model, players devise blueprints and strategically utilize given materials. Poly Bridge features a campaign mode with diverse scenarios, each presenting unique challenges and geographic elements. With over 100 levels, players must meet two criteria in each: stay within budget and ensure the bridge can withstand a specific number of cars.

\

- The game also offers a sandbox mode for unrestricted, parameter-adjustable building. Various vehicles, from fast and light motorcycles to slow and heavy dump trucks, add complexity as their different bodies and weights affect bridge stability. Obstacles like jumps and boats compel players to design creatively, and poorly constructed bridges may collapse under the weight of crossing vehicles.

**Evolutionary Process**

In the context of Poly Bridge, the speedrun problem can be represented with variables like the placement and angles of bridge elements. Chromosomes in this scenario symbolize potential bridge designs.

Define a fitness function that quantifies the quality of a Poly Bridge speedrun. Metrics may include completion time, material efficiency, and structural stability.

1. **Initialization**: Generate an initial population of potential bridge designs.
2. **Selection**: Choose bridge designs based on their fitness in completing the level efficiently.
3. **Crossover**: Combine genetic material of two successful bridge designs to create new designs.
4. **Mutation**: Introduce small changes to bridge designs to explore new possibilities.
5. **Iteration**: Repeat the selection, crossover, and mutation steps for multiple generations.

    .. figure:: bridge.gif
        :align: center



Jump King
---------

- Developed by Nexile, "Jump King" has carved its niche by redefining the boundaries of difficulty and simplicity. "Jump King" introduces players to a minimalist world, where the protagonist's only ability is to jump. The simplicity of controls belies the intricate challenges that await, creating a gameplay experience that is easy to grasp but hard to master. This minimalist approach extends to the game's visual design, featuring a straightforward character and level designs.

- Game website: https://code-bullet.github.io/Jump-King/

    .. figure:: 1.png
        :align: center


1. **Initialization**: Generate an initial population of potential jump sequences.
2. **Selection**: Choose individuals based on their fitness in completing the speedrun efficiently.
3. **Crossover**: Combine genetic material of successful jump sequences to create new individuals.
4. **Mutation**: Introduce small changes to jump sequences to explore new possibilities.
5. **Iteration**: Repeat the selection, crossover, and mutation steps for multiple generations.


Elden Ring
----------

    .. figure:: Elden_Ring_Box_art.png
        :align: center

- "Elden Ring," a 2022 action RPG from FromSoftware, directed by Hidetaka Miyazaki with worldbuilding by George R. R. Martin. Released on February 25, the game follows a customizable character on a quest to restore the Elden Ring. With an open-world design, players explore six main areas on horseback, discover hidden dungeons, and utilize various weapons and magic. Fast travel checkpoints aid exploration, and an online multiplayer mode allows for cooperative play and PvP combat. Elden Ring received critical acclaim for its open world, gameplay, and setting, selling over 20 million copies in a year.

\

    .. figure:: Elden_Ring_gameplay.png
        :align: center


- Perrikaryal, who has a master degree in psychology, uses an electroencephalogram (EEG) to measure her brain functions. She then maps specific types of brain activity to various in-game Elden Ring actions. Simple tasks, like summoning allies and casting spells, are all done without touching a controller.

\

- Evolutionary computation, with its ability to handle complex optimization problems, is a valuable tool in the field of EEG research. By leveraging these techniques, researchers can extract meaningful information from EEG data, advancing our understanding of brain function and supporting the development of applications ranging from medical diagnosis to brain-computer interfaces.

Conclusion
----------


In conclusion, the integration of evolutionary computation in video game speedrunning has proven to be a fascinating and dynamic avenue, offering a unique blend of optimization, creativity, and adaptability. The application of evolutionary algorithms to speedrunning introduces innovative approaches to overcoming challenges, optimizing routes, and pushing the boundaries of what is achievable within the constraints of a game.


Q&A Session
------------

For questions and discussions.


.. [1] Poly Bridge (video game) : https://en.wikipedia.org/wiki/Poly_Bridge_(video_game)
.. [2] Jump King (video game): https://en.wikipedia.org/wiki/Jump_King
.. [3] Elden Ring (video game): https://en.wikipedia.org/wiki/Elden_Ring
.. [4] Perrikaryal : https://www.youtube.com/@perrikaryal/featured
.. [5] Code Bulltet: https://thebigcb.com/
.. [6] Poly Bridge Github: https://github.com/sam-astro/Genetic-Algorithm-Poly-Bridge