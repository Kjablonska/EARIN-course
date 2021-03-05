import numpy as np
import time
import matplotlib.pyplot as plt

A = np.asarray([[2, 0], [0, 2]])
b = np.asarray([1, 1])
c = 2

def J(x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def grad(x):
    grad = 2*np.dot(A, x) + b
    return grad

def grad2(x):
    grad = 2*A
    return grad

cur_x = np.random.uniform(1, 10, b.size)    # Staring point.
rate = 0.01                                 # Learning rate.
precision = 0.0000001                       # Precision of the solution.
step_size = np.asarray([1])
max_iter = 10                          # Maximum number of iterations.
iter = 0                                    # Iterations counter.
max_exe_time = 10                           # Maximum computation time in seconds.
exe_time = 0

start_time = time.time()
while max(step_size) > precision and iter < max_iter and exe_time < max_exe_time:
    prev_x = cur_x
    print("x", cur_x)
    div_grad =  np.dot(grad(prev_x), np.linalg.inv(grad2(prev_x)))
    cur_x = prev_x - div_grad
    step_size = abs(cur_x - prev_x)
    iter = iter + 1
    exe_time = time.time() - start_time

print("x", cur_x)
print("J", J(cur_x))
