import numpy as np
import time

from ex1_common_methods import grad


def newton_based_method(A, b, current_sol):
    current_sol = np.random.uniform(int(current_sol[0]), int(current_sol[1]), b.size)

    rate = 0.01                                 # Learning rate.
    precision = 0.0000001                       # Precision of the solution.
    step_size = np.asarray([1])
    max_iter = 10                               # Maximum number of iterations.
    iter = 0                                    # Iterations counter.
    max_exe_time = 10                           # Maximum computation time in seconds.
    exe_time = 0

    start_time = time.time()
    while max(step_size) > precision and iter < max_iter and exe_time < max_exe_time:
        prev_x = current_sol
        div_grad = np.dot(grad(prev_x, A, b), np.linalg.inv(grad2(A)))
        current_sol = prev_x - div_grad
        step_size = abs(current_sol - prev_x)
        iter = iter + 1
        exe_time = time.time() - start_time

    return current_sol


def grad2(A):
    grad = 2*A
    return grad
