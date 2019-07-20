import json


class Notebook:
    def __init__(self, path):
        self.path = path
        self.cells = []

        # load notebook and convert into dictionary
        with open(path, "r") as f:
            self.contents = json.loads(f.read())

    def convert(self):
        return ""
