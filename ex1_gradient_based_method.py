import numpy as np
import time
import matplotlib.pyplot as plt
import sys

# Change it so as params are provided by the user.
A = np.asarray([[2, 0], [0, 2]])
b = np.asarray([1, 2])
c = 2
N = 10

def J(x,A,c):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def grad(x,A,b):
    return 2*np.dot(A, x) + b

def gradientBasedMethod(A,b):
    cur_x = np.random.uniform(1, 10, b.size)    # Staring point.
    rate = 0.01                                 # Learning rate.
    precision = 0.0000001                       # Precision of the solution.
    step_size = np.asarray([1])
    max_iter = 10000                           # Maximum number of iterations.
    iter = 0                                    # Iterations counter.
    max_exe_time = 10                           # Maximum computation time in seconds.
    exe_time = 0

    start_time = time.time()
    while max(step_size) > precision and iter < max_iter and exe_time < max_exe_time:
        prev_x = cur_x                                  # Storing value of current x as a prev.
        cur_x = cur_x - grad(prev_x, A, b) * rate
        step_size = abs(cur_x - prev_x)                 # Change in x
        iter = iter + 1
        exe_time = time.time() - start_time

    return cur_x

def batchMode(N, A, b):
    sol = []
    for i in range(N):
        sol.append(gradientBasedMethod(A, b))

    print("Mean value of the reult from", N, "iterations:", np.mean(sol))
    print("Standard deviation:", np.std(sol))