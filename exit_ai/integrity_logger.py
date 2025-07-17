# exit_ai

import hashlib
import json
import time
from pathlib import Path

# Simüle edilmiş IPFS yüklemesi
def simulate_ipfs_upload(model_path):
    with open(model_path, 'rb') as f:
        content = f.read()
    fake_ipfs_hash = hashlib.sha1(content).hexdigest()[:46]  # IPFS benzeri hash
    return f"ipfs://{fake_ipfs_hash}"

# SHA-256 hash oluştur
def generate_model_hash(model_path):
    with open(model_path, 'rb') as f:
        model_data = f.read()
    return hashlib.sha256(model_data).hexdigest()

# Hash + Timestamp + Metadata dosyası oluştur
def write_commitment_json(model_path, ipfs_uri, model_hash):
    commitment = {
        "timestamp": int(time.time()),
        "model_filename": Path(model_path).name,
        "model_hash": model_hash,
        "ipfs_uri": ipfs_uri,
        "commitment_scheme": "SHA-256 + IPFS reference",
        "version": "v1.0.0"
    }
    with open('exit_ai/model_commitment.json', 'w') as f:
        json.dump(commitment, f, indent=4)
    print("[✓] Commitment JSON generated at: exit_ai/model_commitment.json")

def commit_model_to_ipfs(model_path='exit_ai/model.bin'):
    print(f"[•] Uploading model: {model_path}")
    ipfs_uri = simulate_ipfs_upload(model_path)
    model_hash = generate_model_hash(model_path)
    write_commitment_json(model_path, ipfs_uri, model_hash)

if __name__ == '__main__':
    commit_model_to_ipfs()
