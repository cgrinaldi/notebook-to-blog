import pytest

from notebook_to_blog.cells import Cell, MarkdownCell, CodeCell


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

    def test_markdown_contents_is_dict(self):
        expected_keys = ["cell_type", "metadata", "source"]
        assert isinstance(self.markdown_cell.contents, dict)
        assert set(self.markdown_cell.contents.keys()) == set(expected_keys)

    def test_convert_creates_string(self):
        actual = self.markdown_cell.convert()
        expected = "this is markdown"
        assert actual == expected


class TestCodeCell:
    def setup_class(self):
        contents = {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {
                "ExecuteTime": {
                    "end_time": "2019-07-20T20:01:11.222265Z",
                    "start_time": "2019-07-20T20:01:09.506208Z",
                }
            },
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": ["[-5.  -4]\n", "[ -5  -3]\n"],
                }
            ],
            "source": [
                "import numpy as np\n",
                "\n",
                "x = np.arange(-5, 5, .1)\n",
                "y = 2 * x + np.random.normal(loc=0, scale=2, size=len(x))\n",
                "\n",
                "print(x[:5])\n",
                "print(y[:5])",
            ],
        }
        self.code_cell = CodeCell(contents)

    def test_code_cell_contents_is_dict(self):
        expected_keys = [
            "cell_type",
            "execution_count",
            "metadata",
            "outputs",
            "source",
        ]
        assert isinstance(self.code_cell.contents, dict)
        assert set(self.code_cell.contents.keys()) == set(expected_keys)
