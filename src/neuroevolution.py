"""
2-input XOR example -- this is most likely the simplest possible example.
"""

import os

import neat
import visualize
import numpy as np
import csv

# [begin-read-data]
with open("site/student-projects/NeuroEvolution/pruned.csv", "r", encoding="utf8") as file:
    reader = csv.reader(file)

    data = np.array(list(reader)).astype(float)

    inputs = data[:, :-1]
    outputs = data[:, -1]
# [end-read-data]

# [begin-evaluation]
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        genome.fitness = float(len(outputs))
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(inputs, outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo) ** 2
# [end-evaluation]

# [begin-run]
def run(config_file):
    # Load configuration.
    config = neat.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_file,
    )

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    # Run for up to 300 generations.
    winner = p.run(eval_genomes, 300)

    # Display the winning genome.
    print("\nBest genome:\n{!s}".format(winner))

    # Show output of the most fit genome against training data.
    print("\nOutput:")
    winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
    for xi, xo in zip(inputs, outputs):
        output = winner_net.activate(xi)
        print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
    # [end-run]
    node_names = {
        -1: "char_freq_!",
        -2: "capital_run_length_longest",
        -3: "capital_run_length_average",
        -4: "word_freq_your",
        -5: "capital_run_length_total",
        -6: "char_freq_$",
        -7: "word_freq_free",
        -8: "word_freq_our",
        -9: "word_freq_you",
        -10: "word_freq_remove",
        0: "SPAM/NOT SPAM",
    }
    visualize.draw_net(
        config,
        winner,
        True,
        node_names=node_names,
        filename="site/student-projects/NeuroEvolution/Visuals/visualize",
    )
    visualize.draw_net(
        config,
        winner,
        True,
        node_names=node_names,
        show_disabled=False,
        prune_unused=True,
        filename="site/student-projects/NeuroEvolution/Visuals/visualize-pruned",
    )
    visualize.plot_stats(
        stats, ylog=False, view=True, filename="site/student-projects/NeuroEvolution/Visuals/avg_fitness.svg"
    )
    visualize.plot_species(stats, view=True, filename="site/student-projects/NeuroEvolution/Visuals/speciation.svg")


if __name__ == "__main__":
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    # local_dir = os.path.dirname(__file__)
    # config_path = os.path.join(local_dir, "config-feedforward")
    config_path = "site/student-projects/NeuroEvolution/config-feedforward"
    run(config_path)
