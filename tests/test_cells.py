import pytest
from notebook_to_blog.cells import Cell, MarkdownCell, CodeCell

GH_USERNAME = "abc"
GITHUB_URL = f"https://gist.github.com/{GH_USERNAME}"


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
        expected = "this is\n\nmarkdown"
        assert actual == expected


class TestCodeCell:
    def setup_class(self):
        self.contents = {
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
            "source": ["import numpy as np\n", "\n", "x = 10"],
        }
        self.code_cell = CodeCell(
            0, self.contents, gh_creds={"username": GH_USERNAME, "password": "123"}
        )

    def test_code_cell_has_outputdir(self):
        assert hasattr(self.code_cell, "output_dir")

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

    def test_convert_creates_string_stream_output(self):
        actual = self.code_cell.convert()
        expected = f"{GITHUB_URL}/a_uuid"
        expected += "\n\n```\n[-5.  -4]\n[ -5  -3]\n```"
        assert actual == expected

    def test_convert_creates_string_execute_result_output(self):
        contents = {
            "source": ["x = 10\n", "x"],
            "outputs": [
                {
                    "data": {"text/plain": ["10"]},
                    "execution_count": 2,
                    "metadata": {},
                    "output_type": "execute_result",
                }
            ],
        }
        actual = CodeCell(
            0, contents, gh_creds={"username": GH_USERNAME, "password": "123"}
        ).convert()
        expected = f"{GITHUB_URL}/a_uuid" + "\n\n```\n10\n```"
        assert actual == expected

    def test_convert_creates_string_display_data_output(self):
        contents = {
            "source": ["plt.scatter(x, y)"],
            "outputs": [
                {
                    "data": {"image/png": "<base64 encoded img>"},
                    "output_type": "display_data",
                }
            ],
        }
        actual = CodeCell(
            9, contents, gh_creds={"username": GH_USERNAME, "password": "123"}
        ).convert()
        expected = f"{GITHUB_URL}/a_uuid" + "\n\n" + "<INSERT img_09.png>"
        assert actual == expected
