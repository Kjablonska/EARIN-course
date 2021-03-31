import numpy as np

from ex1_Newton_method import newton_based_method
from ex1_gradient_based_method import gradient_based_method

def batch_mode_method(method, N, A, b, c, current_sol, _choice):
    sol = []
    if method == 'gradient':
        for i in range(N):
            sol.append(gradient_based_method(A, b, c, current_sol, _choice))

    if method == 'newton':
        for i in range(N):
            sol.append(newton_based_method(A, b, c, current_sol, _choice))

    print("=   Results of", N, "iterations.")
    print("=   Mean value", np.mean(np.array(sol)[:, 0]), np.mean(np.array(sol)[:, 1]))
    print("=   Standard deviation:", np.std(np.array(sol)[:, 0]), np.std(np.array(sol)[:, 1]))

    return sol

def matrix_j(x, A, b, c):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2


def is_symmetric(A):
    return A.transpose().all() == A.all()

def is_positive_definite(A):
    np.linalg.cholesky(A)
    return True

def J_function(A, b, c, x):
    return c + np.dot(b.transpose(), x) + np.dot(np.dot(x.transpose(), A), x)