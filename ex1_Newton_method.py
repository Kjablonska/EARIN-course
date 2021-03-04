import numpy as np
import time
import matplotlib.pyplot as plt

A = np.asarray([[1]])
b = np.asarray([10])
c = 25

def J(x):
    a1 = np.dot(b.transpose(), x)
    a2 = np.dot(np.dot(x.transpose(), A), x)
    return c + a1 + a2

def grad(x):
    return 2*np.dot(A, x) + b

def grad2(x):
    return 2*A

