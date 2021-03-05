import numpy as np
import time
import matplotlib.pyplot as plt

# Change it so as params are provided by the user.
A = np.asarray([[2, 0], [0, 2]])
b = np.asarray([1, 1])
c = 2

def J(x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def grad(x):
    return 2*np.dot(A, x) + b

# Change it so as cur_x can be also defined by the user.
cur_x = np.random.uniform(1, 10, b.size)    # Staring point.
rate = 0.01                                 # Learning rate.
precision = 0.0000001                       # Precision of the solution.
step_size = np.asarray([1])
max_iter = 10000                           # Maximum number of iterations.
iter = 0                                    # Iterations counter.
max_exe_time = 10                           # Maximum computation time in seconds.
exe_time = 0

# To delete. Helper for reult verification.
sol = []
sol_x = []

start_time = time.time()
while max(step_size) > precision and iter < max_iter and exe_time < max_exe_time:
    prev_x = cur_x                                  # Storing value of current x as a prev.
    cur_x = cur_x - grad(prev_x) * rate
    step_size = abs(cur_x - prev_x)                 # Change in x
    iter = iter + 1
    exe_time = time.time() - start_time

    # Helpers for plotting and verification of the result.
    sol.append(J(cur_x))
    sol_x.append(cur_x)

# To delete.
print("x", cur_x)
print("J", J(cur_x))
plt.plot(range(0, iter), sol_x)
plt.show()


# A = np.asarray([[1]])
# b = np.asarray([10])
# c = 25
