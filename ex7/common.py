import torch
import numpy as np

LEARN_COEFF = 0.001
EPOCHS = 3000
P = [1, 4]                      # 295814
LIMIT = [-10, 10]
BATCH_SIZE = 1000
SAMPLES = 10000


def function(x):
    return torch.sin(x * np.sqrt(P[0] + 1)) + torch.cos(x * np.sqrt(P[1] + 1))