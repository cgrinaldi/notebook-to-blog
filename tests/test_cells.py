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
        self.markdown_cell = MarkdownCell(["this is\n", "\n", "markdown"])

    def test_markdown_contents_is_list(self):
        assert isinstance(self.markdown_cell.contents, list)
