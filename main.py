import numpy as np
import ex2_roulette_selection as select
import ex2_crossover as crossover


dimensions = 3
d = 3
A = np.asarray([[-2, 1, 0], [1, -2, 1], [0, 1, -2]])
b = np.asarray([-14, 14, -2])
c = -23.5
population_size = 50
crossover_prob = 0.9
mutation_prob = 0.05
iterations = 1000

def main():
    population = select.generate_population(d, b)
    parents = select.roulette_selection()
    
    crossovered = crossover.crossover()
    print(crossover)


main()