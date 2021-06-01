import numpy as np
import torch
from matplotlib import pyplot as plt
from torch.utils.data import DataLoader, TensorDataset
from common import LEARN_COEFF, EPOCHS, BATCH_SIZE, LIMIT, SAMPLES, function
from net import Net

def main():
    # -------------------------------------------------------------------------------------
    #   Stochastic gradient descent
    # -------------------------------------------------------------------------------------
    network = Net()
    optim = torch.optim.SGD(network.parameters(), lr=LEARN_COEFF, momentum=0.9)     # Create a optimizer with momentum
    criterion = torch.nn.MSELoss()                                                  # Mean Squared Error Loss

    X = torch.from_numpy(np.linspace(LIMIT[0], LIMIT[1], SAMPLES)).float().unsqueeze(1)
    Y = function(X)
    dataloader = DataLoader(TensorDataset(X, Y), batch_size=BATCH_SIZE, shuffle=True)

    # -------------------------------------------------------------------------------------
    #   Training algorithm
    # -------------------------------------------------------------------------------------
    loss_vals = []
    for epoch in range(EPOCHS):
        error = []
        for batch, expected in dataloader:
            # Feeding forward
            loss = criterion(network(batch), expected)
            optim.zero_grad()

            # Backward propagation
            loss.backward()
            optim.step()
            error.append(loss.detach().numpy())

        if epoch % 100 == 0:
            print("epoch {}: {}".format(epoch, loss.item()))

        loss_vals.append(np.mean(error))
    predict = network(X)

    # -------------------------------------------------------------------------------------
    #   Plot function and predicted values.
    # -------------------------------------------------------------------------------------
    x, y = X.detach().numpy(), Y.detach().numpy()
    plt.plot(x, y, label="function")
    plt.plot(x, predict.detach().numpy(), label="predicted")
    plt.title("function")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.savefig(fname="EARIN_ex7_prediction.png", figsize=[10, 10])
    plt.show()

    # -------------------------------------------------------------------------------------
    # Plot mean loss vs epoch.
    # -------------------------------------------------------------------------------------
    plt.plot(range(EPOCHS), loss_vals)
    plt.title("Mean loss")
    plt.xlabel("iterations")
    plt.ylabel("loss")
    plt.savefig(fname="EARIN_ex7_mean_loss.png", figsize=[10, 10])
    plt.show()


if __name__ == '__main__':
    main()