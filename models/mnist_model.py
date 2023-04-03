from torch import nn
from torch.optim import SGD, Adam
from torch.nn import NLLLoss, CrossEntropyLoss
from .base_model import BaseModel

# Demo model for MNIST
class MnistFullConnectModel(BaseModel, nn.Module):
    def __init__(self):
        optimizer = SGD
        loss_fn = NLLLoss()
        optimizer_kwargs = {"lr": 0.1}
        super(BaseModel, self).__init__()
        self.fc1 = nn.Linear(28 * 28, 10)
        self.optimizer = optimizer(self.parameters(), **optimizer_kwargs)
        self.loss_fn = loss_fn

    def forward(self, x):
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        return x


class SimpleCNN(BaseModel, nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.fc2 = nn.Linear(128, 10)
        self.optimizer = Adam(self.parameters(), lr=0.001)
        self.loss_fn = CrossEntropyLoss()

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = self.conv2(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 64 * 7 * 7)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
