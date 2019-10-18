import json

from notebook_to_blog.cells import CodeCell, MarkdownCell
from notebook_to_blog.constants import PROJECT_DIR


class Notebook:
    """
    Notebook class that is responsible for loading Jupyter notebook file
    contents and delegating conversion of cell type to the respective
    cell classes.

    Result of calling the .convert() method is a string representing
    the converted Notebook (which can then be written to a file).

    Currently, cell classes supported are:
    - MarkdownCell
    - CodeCell

    See notebook_to_blog.cells for implementation details.
    """

    def __init__(self, path, output_dir=None, gh_creds=None):
        """
        Args:
            path: str, path to Jupyter notebook to convert
            output_dir: str, path to directory to output files to
            gh_creds: str, path to file containing Github credentials
        """
        self.path = path
        self.output_dir = output_dir
        self.gh_creds = gh_creds

        # load notebook and convert into dictionary
        with open(path, "r") as f:
            self.contents = json.loads(f.read())

        self._load_cells()

    def _load_cells(self):
        """Helper method to load up all cells depending on cell_type."""
        self.cells = []
        for i, x in enumerate(self.contents["cells"]):
            if x["cell_type"] == "markdown":
                cell = MarkdownCell(x)
            elif x["cell_type"] == "code":
                cell = CodeCell(i, x, self.output_dir, self.gh_creds)
            else:
                raise TypeError("Unknown cell type.")
            self.cells.append(cell)
        return self.cells

    def convert(self):
        """Convert notebook by converting all of Notebook's cells."""
        return "\n\n".join([c.convert() for c in self.cells])


if __name__ == "__main__":
    notebook = Notebook(PROJECT_DIR / "tests/test_notebook.ipynb")
    result = notebook.convert()
    import pdb

    pdb.set_trace()
