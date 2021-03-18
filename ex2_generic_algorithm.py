import numpy as np


# https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6


def J_function(A, b, c, x):
    return c + np.dot(b.transpose(), x) + np.dot(np.dot(x.transpose(), A), x)


weights = 3
solutions_per_population = 6
population_size = (solutions_per_population, weights)   # Number of solutions.

current_population = np.random.uniform(low=-5.0, high=5.0, size=population_size)


# Fitness method for selecting the best individual.
# The higher the fitness value the higher the quality the solution.


# Mating pool.
# Every two parents selected from the mating pool will generate two offspring (children). By just mating high-quality individuals, it is expected to get a better quality offspring than its parents. This will kill the bad individuals from generating more bad individuals.


# Crossover.
#  By mutating the old generation parents, the new generation offspring comes by carrying genes from both parents. The amount of genes carried from each parent is random.


# Mutation.
# For each offspring, select some genes and change its value. Mutation varies based on the chromosome representation but it is up to you to decide how to apply mutation.
# Without mutation the offspring will have all of its properties from its parents. To add new features to such offspring, mutation took place.
