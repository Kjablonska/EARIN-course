import numpy as np
import time
import matplotlib.pyplot as plt

# Change it so as params are provided by the user.
A = np.asarray([[2, 0], [0, 2]])
b = np.asarray([1, 1])
c = 2

# Tests for symmetric matrix.
def isSymmetric(M):
    return M.transpose().all() == M.all()

# Test for positive-definite matrix.
def isPositiveDefinite(M):
    eigen_vals = np.linalg.eigvals(A)
    return all(i >= 0 for i in eigen_vals)         # Checking if all eigenvalues are positive.

def J(x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def grad(x):
    return 2*np.dot(A, x) + b

def gradientBasedMethod():
    # Change it so as cur_x (starting point) can be also defined by the user.
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
        cur_x = cur_x - grad(prev_x) * rate
        step_size = abs(cur_x - prev_x)                 # Change in x
        iter = iter + 1
        exe_time = time.time() - start_time
        return cur_x


def batchMode():
    N = 10
    sol = []
    for i in range(N):
        sol.append(gradientBasedMethod())

    print("Mean value of the reult from", N, "iterations:", np.mean(sol))
    print("Standard deviation:", np.std(sol))


batchMode()



# Helpers for plotting and verification of the result.
# sol.append(J(cur_x))
# sol_x.append(cur_x)

# To delete.
# print("x", cur_x)
# print("J", J(cur_x))
# plt.plot(range(0, iter), sol_x)
# plt.show()