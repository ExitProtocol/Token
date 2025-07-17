# exit_ai

import re
from transformers import pipeline

class ContractInterpreter:
    def __init__(self):
        
        self.classifier = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-contracts")

    def extract_logic_sections(self, contract_text):
        functions = re.findall(r'(function\s+\w+.*?{.*?})', contract_text, re.DOTALL)
        return functions

    def analyze_function(self, func_code):
        analysis = self.classifier(func_code[:512])
        return analysis

    def parse_contract(self, contract_text):
        results = []
        functions = self.extract_logic_sections(contract_text)
        for func in functions:
            result = self.analyze_function(func)
            results.append({
                "function": func.split('{')[0],
                "label": result[0]['label'],
                "score": round(result[0]['score'], 3)
            })
        return results
