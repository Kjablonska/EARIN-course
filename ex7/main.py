import numpy as np
import torch
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, TensorDataset
from common import LEARN_COEFF, EPOCHS, BATCH_SIZE, LIMIT, SAMPLES, function
from net import Net

def main():
    net = Net()
    optim = torch.optim.SGD(net.parameters(), lr=LEARN_COEFF, momentum=0.9)
    criterion = torch.nn.MSELoss()


    X = torch.from_numpy(np.linspace(LIMIT[0], LIMIT[1], SAMPLES)).float().unsqueeze(1)
    Y = function(X)

    dataloader = DataLoader(TensorDataset(X, Y), batch_size=BATCH_SIZE, shuffle=True)

    for epoch in range(EPOCHS):
        for batch, expected in dataloader:
            loss = criterion(net(batch), expected)
            optim.zero_grad()
            loss.backward()
            optim.step()

        if epoch % 100 == 0:
            print("epoch {}: {}".format(epoch, loss.item()))

    predict = net(X)

    x, y = X.detach().numpy(), Y.detach().numpy()
    plt.plot(x, y, label="factual data")
    plt.plot(x, predict.detach().numpy(), label="predicted data")
    plt.title("function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(fname="EARIN_ex7.png", figsize=[10, 10])
    plt.show()


main()