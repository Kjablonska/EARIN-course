import numpy as np

# https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6

dimensions = 3
d = 3
A = [[-2, 1, 0], [1, -2, 1], [0, 1, -2]]
b = [-14, 14, -2]
c = -23.5
population_size = 50
crossover_prob = 0.9    # crossover_point
mutation_prob = 0.05    # random value
iterations = 1000

def J_function(A, b, c, x):
    return c + np.dot(b.transpose(), x) + np.dot(np.dot(x.transpose(), A), x)

# Fitness method for selecting the best individual.
# The higher the fitness value the higher the quality the solution.
current_x = np.random.uniform(low=-5.0, high=5.0, size=population_size)
current_population = J_function(A, b, c, current_x)

def fitness(A, b, c, current_population):
    fitness = np.sum(A * b * c * current_population, axis=1)    # Change to dot product.
    return fitness


# Mating pool.
# Every two parents selected from the mating pool will generate two offspring (children). By just mating high-quality individuals, it is expected to get a better quality offspring than its parents. This will kill the bad individuals from generating more bad individuals.

# Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
def mating_pool(current_population, fitness, parents):
    parents = np.empty((parents, current_population.shape[1]))

    for parent_num in range(current_population):
        max_fitness_idx = np.where(fitness == np.max(fitness))
        max_fitness_idx = max_fitness_idx[0][0]
        parents[parent_num, :] = current_population[max_fitness_idx, :]
        fitness[max_fitness_idx] = -99999999999

    return parents


# Crossover.
#  By mutating the old generation parents, the new generation offspring comes by carrying genes from both parents. The amount of genes carried from each parent is random.
def crossover(parents, offspring_size):
    offspring = np.empty(offspring_size)
    # The point at which crossover takes place between two parents. Usually it is at the center.
    # crossover_point = np.uint8(offspring_size[1]/2)

    for k in range(offspring_size[0]):
        # Index of the first parent to mate.
        parent1_idx = k%parents.shape[0]
        # Index of the second parent to mate.
        parent2_idx = (k+1)%parents.shape[0]
        # The new offspring will have its first half of its genes taken from the first parent.
        offspring[k, 0:crossover_prob] = parents[parent1_idx, 0:crossover_prob]
        # The new offspring will have its second half of its genes taken from the second parent.
        offspring[k, crossover_prob:] = parents[parent2_idx, crossover_prob:]
    return offspring


# Mutation.
# For each offspring, select some genes and change its value. Mutation varies based on the chromosome representation but it is up to you to decide how to apply mutation.
# Without mutation the offspring will have all of its properties from its parents. To add new features to such offspring, mutation took place.
def mutation(offspring_crossover):
    # Mutation changes a single gene in each offspring randomly.
    for idx in range(offspring_crossover.shape[0]):
        # The random value to be added to the gene.
        # random_value = np.random.uniform(-1.0, 1.0, 1)
        offspring_crossover[idx, 4] = offspring_crossover[idx, 4] + mutation_prob
    return offspring_crossover