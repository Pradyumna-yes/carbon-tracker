import os
import requests

class EmissionCalculator:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("CLIMATIQ_API_KEY")  # Changed to os.getenv()
        if not self.api_key:
            raise ValueError("Missing Climatiq API key")

    def calculate_emissions(self, energy_kwh):
        """Calculate CO2 emissions using Climatiq API"""
        url = "https://api.climatiq.io/data/v1/estimate"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "emission_factor": {
                "activity_id": "electricity-supply_grid-source_residual_mix",
                "data_version": "^21"
            },
            "parameters": {
                "energy": energy_kwh,
                "energy_unit": "kWh"
            }
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raises exception for 4XX/5XX errors
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API Error: {str(e)}")
            return None