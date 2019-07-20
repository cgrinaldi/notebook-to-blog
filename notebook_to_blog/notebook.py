import json

from notebook_to_blog.cells import Cell


class Notebook:
    def __init__(self, path):
        self.path = path

        # load notebook and convert into dictionary
        with open(path, "r") as f:
            self.contents = json.loads(f.read())

        self.cells = self._load_cells()

    def _load_cells(self):
        result = []
        for c in self.contents["cells"]:
            result.append(Cell(c))
        return result

    def convert(self):
        return ""
