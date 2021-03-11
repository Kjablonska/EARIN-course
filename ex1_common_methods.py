import numpy as np

from ex1_Newton_method import newton_based_method
from ex1_gradient_based_method import gradient_based_method

def batch_mode_method(method, N, A, b, cur_x):
    sol = []
    if method == 'gradient':
        for i in range(N):
            sol.append(gradient_based_method(A, b, cur_x))

    if method == 'newton':
        for i in range(N):
            sol.append(newton_based_method(A, b, cur_x))

    print("=   Mean value of the result from", N, "iterations:", np.mean(sol))
    print("=   Standard deviation:", np.std(sol))


def matrix_j(x, A, b, c):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2


def is_symmetric(M):
    return M.transpose().all() == M.all()


def is_positive_definite(M):
    np.linalg.cholesky(M)
    return True

