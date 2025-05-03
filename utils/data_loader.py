import json
import os

def load_registration_data():
    file_path = os.path.join(os.path.dirname(__file__), '../test_data/registration_data.json')
    with open(file_path, 'r') as file:
        return json.load(file)

def load_login_data():
    file_path = os.path.join(os.path.dirname(__file__), '../test_data/login_data.json')
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find login_data.json at {file_path}")