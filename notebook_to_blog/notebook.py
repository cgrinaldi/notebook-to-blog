import json

from notebook_to_blog.cells import CodeCell, MarkdownCell
from notebook_to_blog.constants import PROJECT_DIR


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
            elif x["cell_type"] == "code":
                cell = CodeCell(x)
            else:
                raise TypeError("Unknown cell type.")
            result.append(cell)
        return result

    def convert(self):
        return "\n\n".join([c.convert() for c in self.cells])


if __name__ == "__main__":
    notebook = Notebook(PROJECT_DIR / "tests/test_notebook.ipynb")
    result = notebook.convert()
