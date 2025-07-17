# exit_ai

import torch
import torch.nn as nn

class SimpleAutoencoder(nn.Module):
    def __init__(self, input_dim=64, latent_dim=16):
        super(SimpleAutoencoder, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, latent_dim),
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 32),
            nn.ReLU(),
            nn.Linear(32, input_dim),
        )

    def forward(self, x):
        z = self.encoder(x)
        return self.decoder(z)

def detect_anomalies(model, data, threshold=0.1):
    model.eval()
    with torch.no_grad():
        reconstructed = model(data)
        loss = torch.mean((reconstructed - data) ** 2, dim=1)
        return loss > threshold
