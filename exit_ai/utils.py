# exit_ai

import numpy as np

def calculate_traceability_score(tx_path):
    # Dummy entropy-based traceability metric
    entropy = -np.sum([p*np.log2(p) for p in tx_path if p > 0])
    return entropy / len(tx_path)

def reward_function(trace_score, obfuscation_depth):
    return 1.0 / (1 + trace_score + obfuscation_depth)
