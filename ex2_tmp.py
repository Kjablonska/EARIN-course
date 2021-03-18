import numpy as np
import ex2_genetic_alg as ga

dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9    # crossover_point
mutation_prob = 0.05    # random value
iterations = 1000
num_parents_mating = 4

def J_function(A, b, c, x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

# Fitness method for selecting the best individual.
# The higher the fitness value the higher the quality the solution.
current_x = np.random.uniform(low=-5.0, high=5.0, size=d)
current_population = J_function(A, b, c, np.asarray(current_x))

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
                                       offspring_size=(population_size-parents.shape[0], d))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
    print("Best result : ", np.max(np.sum(current_population*A*b*c, axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = ga.fitness(A, b, c, current_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = np.where(fitness == np.max(fitness))

print("Best solution : ", current_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])
