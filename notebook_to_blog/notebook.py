import json

from notebook_to_blog.cells import Cell, MarkdownCell


class Notebook:
    def __init__(self, path):
        self.path = path

        # load notebook and convert into dictionary
        with open(path, "r") as f:
            self.contents = json.loads(f.read())

        self.cells = self._load_cells()

    def _load_cells(self):
        result = []
        for x in self.contents["cells"]:
            if x["cell_type"] == "markdown":
                cell = MarkdownCell(x)
            else:
                cell = Cell(x)
            result.append(cell)
        return result

    def convert(self):
        return ""
