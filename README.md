# cs4XX

CS 4XX: Evolutionary Computation

The course can be found [here](http://modsurski.com/csci340)

Class covering:

- General evolutionary computation things
- Problem-solving with evolutionary computation
- Genetic algorithms
- Genetic programming
- Swarm intelligence
- EC operators 
- Representations
- Selection strategies
- Fitness functions
- Multi-objective optimization 
- Current trends in EC

The course is designed to be an upper year undergraduate/graduate level course that assumes sufficient expertise in data 
structures and algorithms. Experience with AI, machine learning, and data analysis is an asset but not required. 


# Setup

## Windows

Have administrative privileges and run from cmd

```sh
python -m venv --clear --prompt cs340 venv
venv\Scripts\activate.bat
pip install --upgrade pip setuptools wheel
SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip install --editable .
```

## Bash

```sh
python3.10 -m venv --clear --prompt cs340 venv
. venv/bin/activate
pip install --upgrade pip setuptools wheel
SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip install --editable .
```

# Formatter

```sh
format # just type this
```

# Unit Tests

```sh
python -m unittest # May need python3
```

# Build

```sh
sphinx-build -b html "$SOURCEDIR" "$OUTPUTDIR"
```

# Contribute

Check out the [CONTRIBUTING](CONTRIBUTING.md) guidelines.
