import pytest

from pathlib import Path

from notebook_to_blog.notebook import Notebook
from notebook_to_blog.cells import Cell
from notebook_to_blog.constants import PROJECT_DIR


@pytest.fixture()
def notebook():
    return Notebook(PROJECT_DIR / "tests/test_notebook.ipynb")


def test_notebook_has_path(notebook):
    assert isinstance(notebook.path, Path)


def test_notebook_has_contents(notebook):
    expected_keys = ["cells", "metadata", "nbformat", "nbformat_minor"]

    assert isinstance(notebook.contents, dict)
    assert set(notebook.contents.keys()) == set(expected_keys)


def test_notebook_converts_to_string(notebook):
    assert isinstance(notebook.convert(), str)


def test_notebook_has_cells(notebook):
    cells = notebook.cells
    assert isinstance(cells, list)
    assert isinstance(cells[0], Cell)
    assert len(cells) == 3
