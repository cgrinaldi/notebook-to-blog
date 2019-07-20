import pytest

from notebook_to_blog.notebook import Notebook


@pytest.fixture()
def notebook():
    return Notebook("my-path")


def test_notebook_has_path(notebook):
    assert notebook.path == "my-path"


def test_notebook_converts_to_string(notebook):
    assert isinstance(notebook.convert(), str)


def test_notebook_has_cells(notebook):
    assert isinstance(notebook.cells, list)
