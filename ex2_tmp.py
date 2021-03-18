import numpy as np
import ex2_generic_algorithm as ga

dimensions = 3
d = 3
A = [[-2, 1, 0], [1, -2, 1], [0, 1, -2]]
b = [-14, 14, -2]
c = -23.5
population_size = 50
crossover_prob = 0.9    # crossover_point
mutation_prob = 0.05    # random value
iterations = 1000
num_parents_mating = 4

def J_function(A, b, c, x):
    return c + np.dot(b.transpose(), x) + np.dot(np.dot(x.transpose(), A), x)

# Fitness method for selecting the best individual.
# The higher the fitness value the higher the quality the solution.
current_x = np.random.uniform(low=-5.0, high=5.0, size=population_size)
current_population = J_function(A, b, c, current_x)

def fitness(A, b, c, current_population):
    fitness = np.sum(A * b * c * current_population, axis=1)    # Change to dot product.
    return fitness

num_generations = 5
for generation in range(num_generations):
    print("Generation : ", generation)
    # Measing the fitness of each chromosome in the population.
    fitness = fitness(A, b, c, current_population)

    # Selecting the best parents in the population for mating.
    parents = ga.mating_pool(current_population, fitness, num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], num_weights))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
    print("Best result : ", numpy.max(numpy.sum(new_population*equation_inputs, axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = ga.cal_pop_fitness(equation_inputs, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = numpy.where(fitness == numpy.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])
