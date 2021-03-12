import numpy as np
import time


def gradient_based_method(A, b, c, current_sol, choice):
    if choice == '2':
        current_sol = np.random.uniform(int(current_sol[0]), int(current_sol[1]), b.size)

    rate = 0.01                                 # Learning rate.
    precision = 1e-6                            # Precision of the solution.
    max_iter = 10000                            # Maximum number of iterations.
    iter = 0                                    # Iterations counter.
    max_exe_time = 10                           # Maximum computation time in seconds.
    exe_time = 0
    step_size = 1

    start_time = time.time()
    while step_size > precision and iter < max_iter and exe_time < max_exe_time:
        prev_x = current_sol
        current_sol = current_sol - grad(prev_x, A, b) * rate
        step_size = abs(J_function(A, b, c, current_sol) - J_function(A, b, c, prev_x))
        iter = iter + 1
        exe_time = time.time() - start_time

    return current_sol


def grad(x, A, b):
    return 2*np.dot(A, x) + b


def J_function(A, b, c, x):
    return c + np.dot(b.transpose(), x) + np.dot(np.dot(x.transpose(), A), x)