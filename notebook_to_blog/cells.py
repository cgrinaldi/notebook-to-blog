class Cell:
    def __init__(self, contents):
        self.contents = contents

    def convert(self):
        raise NotImplementedError("Cell should be subclassed.")


class MarkdownCell(Cell):
    def __init__(self, contents):
        super().__init__(contents)
