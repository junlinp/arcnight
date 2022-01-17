
import torch
from torch import nn


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()


        self.model = nn.Sequential(
                nn.Flatten()
                nn.Linear(3 * 1440 * 899, 512),
                nn.ReLU(),
                nn.Linear(512, 512)
                nn.ReLU(),
                nn.Linear(512, 3)
        )

    def forward(self, x):
        logits = self.model(x)
        return logits
