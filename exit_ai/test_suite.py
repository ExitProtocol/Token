# exit_ai

import time
import random
import numpy as np
from exit_ai.threat_engine import ThreatDetectionEngine
from exit_ai.obfuscation_agent import ObfuscationAgent
from exit_ai.federated_learner import FederatedLearner
from exit_ai.nlp_parser import ContractInterpreter

def test_threat_detection():
    engine = ThreatDetectionEngine()
    injected_patterns = engine.synthetic_attack_patterns
    true_positive = 0

    for pattern in injected_patterns:
        result = engine.detect_threat(pattern)
        if result["is_threat"]:
            true_positive += 1

    precision = true_positive / len(injected_patterns)
    print(f"[Threat Detection] Precision: {round(precision * 100, 2)}%")

def test_obfuscation_latency():
    agent = ObfuscationAgent()
    start_time = time.time()
    for _ in range(10000):
        state = {
            "network_stress": random.random(),
            "traceability_score": random.random()
        }
        agent.obfuscate(state)
    duration = time.time() - start_time
    avg_latency = duration / 10000 * 1000
    print(f"[Obfuscation Agent] Avg. Inference Latency: {round(avg_latency, 2)} ms")

def test_nlp_parser():
    parser = ContractInterpreter()
    malicious_contract = """
    function drainFunds(address to) public {
        require(msg.sender == admin);
        payable(to).transfer(address(this).balance);
    }
    """
    results = parser.parse_contract(malicious_contract)
    print(f"[NLP Parser] Results: {results}")

def test_federated_learning_integrity():
    learner = FederatedLearner()
    initial_model = learner.model
    learner.aggregate_updates()
    updated_model = learner.model

    drift = np.mean(np.abs(np.array(updated_model) - np.array(initial_model)))
    print(f"[Federated Learning] Model Drift After Aggregation: {round(drift, 4)}")

def main():
    print("== EXIT//AI Test Suite ==")
    test_threat_detection()
    test_obfuscation_latency()
    test_nlp_parser()
    test_federated_learning_integrity()
    print("== All tests completed ==")

if __name__ == "__main__":
    main()
