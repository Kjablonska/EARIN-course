import numpy as np

# https://towardsdatascience.com/genetic-algorithm-implementation-in-python-5ab67bb124a6

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9    # crossover_point
mutation_prob = 0.05    # random value
iterations = 1000


population_arr = []
species_not_crossovered = []
species_to_crossover = []
crossovered_species = []
parents = []


def J_function(A, b, c, x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

# Fitness method for selecting the best individual.
# The higher the fitness value the higher the quality the solution.
current_x = np.random.uniform(low=-5.0, high=5.0, size=d)
current_population = np.random.uniform(low=-4.0, high=4.0, size=population_size)

def generate_population(d, b):
    population_arr = []

    for i in population_size:
        pow = np.power(2, d)
        x = np.random.uniform(i - pow, pow, b.size())
        population_arr.append(x)

    return population_size


def fitness(A, b, c, current_x):
    fitness = J_function(A, b, c, current_x)
    return fitness

# Mating pool.
# Every two parents selected from the mating pool will generate two offspring (children). By just mating high-quality individuals, it is expected to get a better quality offspring than its parents. This will kill the bad individuals from generating more bad individuals.

# Selecting the best individuals in the current generation as parents for producing the offspring of the next generation.
def mating_pool():
    mating_arr = []
    parents_number = 2

    for i in population_arr:
        curr_fitness = fitness(A, b, c, i)
        mating_arr.append(curr_fitness)

    for i in parents_number:
        max = np.max(mating_arr)
        parents.append(max)
        mating_arr.remove(max)

    return parents


def choose_chromosomes_to_crossover(population_arr, species_not_crossovered, species_to_crossover):
    # We need to remove parents from population_arr before finding spieces to crossover.
    population_arr.remove(parents)
    for chromosome in population_arr:
        if np.random.uniform(0, 1) < crossover_prob:
            species_to_crossover.append(chromosome)
        else:
            species_not_crossovered.append(chromosome)


def crossover_population():
    mating_pool()
    for crossover in species_to_crossover:
        child_a, child_b = crossover_chromosomes(crossover)
        crossovered_species.append(child_a)
        crossovered_species.append(child_b)
    return crossovered_species


#   Crossover.
#  By mutating the old generation parents, the new generation offspring comes by carrying genes from both parents. The amount of genes carried from each parent is random.
def crossover_chromosomes():
    p1 = parents[0]
    p2 = parents[1]
    p1_bin = list(np.binary_repr(p1))
    p2_bin = list(np.binary_repr(p2))
    # p_bin = list(np.binary_repr(parent))
    crossover_point = p1_bin.len() / 2

    for i in range(crossover_point):
        


def create_crossover_tuples(species_not_crossovered, species_to_crossover):
    crossover_tuples = []
    species_to_crossover = list(enumerate(species_to_crossover))
    while species_to_crossover:
        chromosome_to_crossover_index, chromosome_to_crossover = species_to_crossover.pop()

        if not species_to_crossover:
            species_not_crossovered.append(chromosome_to_crossover)
            break

        crossover_buddy_index, crossover_buddy = np.random.choice(species_to_crossover)
        species_to_crossover = list(filter(lambda value: value[0] != crossover_buddy_index, species_to_crossover))
        crossover_tuples.append((chromosome_to_crossover, crossover_buddy))
    return crossover_tuples

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