from torch.utils.data import DataLoader, TensorDataset
from torch import nn
# -------------------------------------------------------------------------------------
#   Two layer model
# -------------------------------------------------------------------------------------
class Net(nn.Module):
    # Constructor
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(1, 650),
            nn.ReLU(),
            nn.Linear(650, 1),
        )

    # Prediction
    def forward(self, X):
        return self.net(X)