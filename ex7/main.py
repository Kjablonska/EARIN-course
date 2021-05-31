import numpy as np
import torch
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, TensorDataset
from torch import nn

from common import LEARN_COEFF, function, EPOCHS
from net import Net

if __name__ == "__main__":
    net = Net()
    # the optimizer - Adam is type of SDG
    optim = torch.optim.Adam(net.parameters(), lr=LEARN_COEFF)
    # mean square error loss function
    criterion = nn.MSELoss()

    # 1000 samples from [-10, 10], float32, shape (1000, 1)
    X = torch.from_numpy(np.linspace(-10, 10, 1000)).float().unsqueeze(1)
    Y = function(X)

    dataloader = DataLoader(TensorDataset(X, Y), batch_size=100, shuffle=True)

    for epoch in range(1, EPOCHS + 1):
        for batch, expected in dataloader:
            loss = criterion(net(batch), expected)
            optim.zero_grad()
            loss.backward()
            optim.step()

        if epoch % 100 == 0:
            print(f"epoch #{epoch}: {loss.item()}")

    predict = net(X)

    # Plot showing the difference between predicted and real data
    x, y = X.detach().numpy(), Y.detach().numpy()
    plt.plot(x, y, label="factual")
    plt.plot(x, predict.detach().numpy(), label="predicted")
    plt.title("function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(fname="result.png", figsize=[10, 10])
    plt.show()