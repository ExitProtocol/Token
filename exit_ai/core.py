# core.py
import logging

from .autoencoders import AutoencoderDetector
from .isolation_forest import IsolationForestDetector
from .gmm_detector import GMMDetector
from .rl_agent import PPOAgent
from .federated import FederatedLearning
from .nlpi import NLProtocolInterpreter


class EXITAI:
    def __init__(self, config):
        self.logger = logging.getLogger('EXITAI')
        self.logger.info("Initializing EXITAI system...")

        self.autoencoder = AutoencoderDetector(config.get('autoencoder', {}))
        self.isolation_forest = IsolationForestDetector(config.get('isolation_forest', {}))
        self.gmm = GMMDetector(config.get('gmm', {}))
        self.rl_agent = PPOAgent(config.get('rl_agent', {}))
        self.federated = FederatedLearning(config.get('federated', {}))
        self.nlpi = NLProtocolInterpreter(config.get('nlpi', {}))

        self.logger.info("EXITAI initialized successfully.")

    def detect_anomaly(self, transaction_data):
        self.logger.debug("Running anomaly detection...")
        ae_score = self.autoencoder.detect(transaction_data)
        if_score = self.isolation_forest.detect(transaction_data)
        gmm_score = self.gmm.detect(transaction_data)

        # Ensemble score with weighted average if needed
        scores = [ae_score, if_score, gmm_score]
        ensemble_score = sum(scores) / len(scores)

        self.logger.debug(f"Anomaly scores: AE={ae_score:.4f}, IF={if_score:.4f}, GMM={gmm_score:.4f}")
        self.logger.info(f"Ensemble anomaly score: {ensemble_score:.4f}")

        return ensemble_score

    def obfuscate_transaction(self, transaction):
        self.logger.debug("Obfuscating transaction path using RL agent...")
        obfuscated_transaction = self.rl_agent.obfuscate(transaction)
        self.logger.info("Transaction obfuscation complete.")
        return obfuscated_transaction

    def federated_update(self, local_model_updates):
        self.logger.debug("Updating federated learning global model...")
        update_result = self.federated.aggregate(local_model_updates)
        self.logger.info("Federated learning update finished.")
        return update_result

    def interpret_contract(self, contract_code):
        self.logger.debug("Parsing smart contract with NLPI...")
        analysis_result = self.nlpi.parse(contract_code)
        self.logger.info("Smart contract interpretation complete.")
        return analysis_result

    def analyze(self, transaction_data, contract_code):
        self.logger.info("Starting full EXITAI analysis pipeline...")
        anomaly_score = self.detect_anomaly(transaction_data)
        obfuscated_tx = self.obfuscate_transaction(transaction_data)
        contract_analysis = self.interpret_contract(contract_code)

        result = {
            "anomaly_score": anomaly_score,
            "obfuscated_transaction": obfuscated_tx,
            "contract_analysis": contract_analysis
        }

        self.logger.info("EXITAI analysis pipeline completed.")
        return result
