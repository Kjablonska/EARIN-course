import torch
import numpy as np

LEARN_COEFF = 0.01
EPOCHS = 1000
NEUTRON_NO = 100
NO = 1
P = [1, 4]                      # 295814, Jablonska
LIMIT = [-10, 10]
TRAIN_DATA_SIZE = 4000
TEST_DATA_SIZE = 100

def function(x):                # Input function
    return torch.sin(x * np.sqrt(P[0] + 1)) + torch.cos(x * np.sqrt(P[1] + 1))