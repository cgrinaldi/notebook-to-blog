import pytest

from notebook_to_blog.cells import Cell, MarkdownCell


@pytest.fixture
def cell():
    return Cell("cell contents")


def test_cell_has_contents(cell):
    assert hasattr(cell, "contents")


def test_cell_covert_is_not_implemented(cell):
    with pytest.raises(NotImplementedError):
        cell.convert()


class TestMarkdownCell:
    def setup_class(self):
        contents = {
            "cell_type": "markdown",
            "metadata": {},
            "source": ["this is\n", "\n", "markdown"],
        }
        self.markdown_cell = MarkdownCell(contents)

    def test_markdown_contents_is_list(self):
        expected_keys = ["cell_type", "metadata", "source"]
        assert isinstance(self.markdown_cell.contents, dict)
        assert set(self.markdown_cell.contents.keys()) == set(expected_keys)

    def test_convert_creates_string(self):
        actual = self.markdown_cell.convert()
        expected = "this is markdown"
        assert actual == expected
