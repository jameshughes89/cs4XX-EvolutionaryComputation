# Genetic Algorithm for the Travelling Salesperson Problem (TSP)

## Overview
This project implements a Genetic Algorithm (GA) to solve the Travelling Salesperson Problem (TSP).  
It supports multiple datasets (small, medium, and large TSP instances from TSPLIB) and includes:
- Baseline heuristic (Nearest Neighbor).
- Genetic Algorithm with tournament selection, crossover, mutation, and elitism.
- Convergence plots and route visualizations.
- Statistical analysis across multiple runs (mean, std. dev., best, worst).

---

## Requirements
Make sure you have **Python 3.8+** and install dependencies:

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

```bash
python3 -m venv venv
```

On Linux / MacOs
```bash
source venv/bin/activate
```

On Windows
```bash
venv\Scripts\Activate
```
Then open new terminal and run: 
```bash
pip install pandas
pip install matplotlib
pip install numpy
```