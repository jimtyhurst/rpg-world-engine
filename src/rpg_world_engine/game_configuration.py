import json


def load_configuration_file(filename):
    with open(filename, "r") as f:
        return json.load(f)
