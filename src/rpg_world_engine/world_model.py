import json

def load_world_model(filename):
    with open(filename, 'r') as f:
        return json.load(f)
