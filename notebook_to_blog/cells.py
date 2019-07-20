class Cell:
    def __init__(self, contents):
        self.contents = contents

    def convert(self):
        raise NotImplementedError("Cell should be subclassed.")


class MarkdownCell(Cell):
    def __init__(self, contents):
        super().__init__(contents)

    def convert(self):
        # with_spaces = [" " if x == "\n" else x for x in self.contents["source"]]
        # return "".join([x.replace("\n", "") for x in with_spaces])
        return "".join(self.contents["source"])


class CodeCell(Cell):
    def __init__(self, contents):
        super().__init__(contents)

    def convert(self):
        return "```\n" + "".join(self.contents["source"]) + "\n```"
