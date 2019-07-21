from notebook_to_blog.cli import create_filename
from notebook_to_blog.constants import PROJECT_DIR


def test_create_filename():
    notebook_path = PROJECT_DIR / "tests/test_notebook.ipynb"
    actual = create_filename(notebook_path)
    expected = "test_notebook.txt"
    assert actual == expected
