import glob
import os
import pytest

from pathlib import Path

from notebook_to_blog.notebook import Notebook
from notebook_to_blog.cells import Cell, MarkdownCell, CodeCell
from notebook_to_blog.constants import PROJECT_DIR

OUTPUT_DIR = PROJECT_DIR / "tests/output/"
IMG_DIR = OUTPUT_DIR / "images"


def setup_module():
    OUTPUT_DIR.mkdir()
    IMG_DIR.mkdir()


def teardown_module():
    # remove all images
    for f in glob.glob(str(IMG_DIR) + "/*"):
        os.remove(f)

    # remove image directory
    IMG_DIR.rmdir()

    # remove other files
    for f in glob.glob(str(OUTPUT_DIR) + "/*"):
        os.remove(f)

    # remove test output directory
    OUTPUT_DIR.rmdir()


@pytest.fixture()
def notebook():
    gh_creds = {"username": "abc", "password": "123}"}
    return Notebook(PROJECT_DIR / "tests/test_notebook.ipynb", OUTPUT_DIR, gh_creds)


def test_notebook_has_path(notebook):
    assert isinstance(notebook.path, Path)


def test_notebook_has_contents(notebook):
    expected_keys = ["cells", "metadata", "nbformat", "nbformat_minor"]

    assert isinstance(notebook.contents, dict)
    assert set(notebook.contents.keys()) == set(expected_keys)


def test_notebook_has_output_dir(notebook):
    assert hasattr(notebook, "output_dir")
    assert isinstance(notebook.output_dir, Path)


def test_notebook_converts_to_string(notebook):
    assert isinstance(notebook.convert(), str)


def test_notebook_has_cells(notebook):
    cells = notebook.cells
    assert isinstance(cells, list)
    assert isinstance(cells[0], Cell)
    assert len(cells) == 5


def test_notebook_has_correct_count_markdown_cells(notebook):
    markdown_cells = [c for c in notebook.cells if isinstance(c, MarkdownCell)]
    assert len(markdown_cells) == 2


def test_notebook_has_correct_count_code_cells(notebook):
    code_cells = [c for c in notebook.cells if isinstance(c, CodeCell)]
    assert len(code_cells) == 3


def test_notebook_increments_figure_numbers(notebook):
    for i, c in enumerate(notebook.cells):
        if isinstance(c, CodeCell):
            assert c.idx == i


def test_notebook_writes_image(notebook):
    # converting the notebook should have side effect of writing images
    notebook.convert()

    # check that images have been written
    images = glob.glob(str(IMG_DIR) + "/*.png")
    assert len(images) > 0
