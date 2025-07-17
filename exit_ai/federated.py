# exit_ai

import torch
import numpy as np
from cryptography.fernet import Fernet
from collections import defaultdict

class FederatedServer:
    def __init__(self, global_model):
        self.global_model = global_model
        self.client_updates = []
        self.reputations = defaultdict(lambda: 1.0)

    def receive_update(self, encrypted_update, node_id, encryption_key):
        try:
            f = Fernet(encryption_key)
            decrypted_bytes = f.decrypt(encrypted_update)
            local_weights = torch.load(decrypted_bytes)
            if self.is_valid_update(local_weights, node_id):
                self.client_updates.append((local_weights, self.reputations[node_id]))
        except Exception as e:
            print(f"[!] Decryption failed from {node_id}: {e}")

    def is_valid_update(self, weights, node_id):
        # Basit anomaly detection – zehirli güncellemeleri filtrele
        mean_abs = np.mean([w.abs().mean().item() for w in weights.values()])
        if mean_abs > 10:  # Heuristic threshold
            self.reputations[node_id] *= 0.5
            return False
        self.reputations[node_id] *= 1.05  # Trust score artır
        return True

    def aggregate_updates(self):
        if not self.client_updates:
            return self.global_model.state_dict()

        total_weight = sum(rep for _, rep in self.client_updates)
        aggregated = {}
        for key in self.global_model.state_dict().keys():
            aggregated[key] = sum(
                weights[key] * rep / total_weight for weights, rep in self.client_updates
            )
        self.global_model.load_state_dict(aggregated)
        self.client_updates = []
        return aggregated

class FederatedClient:
    def __init__(self, local_model, encryption_key):
        self.local_model = local_model
        self.key = encryption_key
        self.f = Fernet(self.key)

    def train_on_local_data(self, train_fn):
        train_fn(self.local_model)

    def encrypt_weights(self):
        model_bytes = torch.save(self.local_model.state_dict(), "_tmp.pt")
        with open("_tmp.pt", "rb") as f:
            encrypted = self.f.encrypt(f.read())
        return encrypted
