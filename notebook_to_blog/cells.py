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
        return self._convert_source() + "\n\n" + self._convert_outputs()

    def _convert_source(self):
        return "```\n" + "".join(self.contents["source"]) + "\n```"

    def _convert_outputs(self):
        result = []
        for o in self.contents["outputs"]:
            result += self._convert_output(o)
        return "".join(result)

    def _convert_output(self, output):
        if output["output_type"] == "stream":
            return "```\n" + "".join(output["text"]) + "```"
        elif output["output_type"] == "execute_result":
            return "```\n" + "".join(output["data"]["text/plain"]) + "\n```"
        elif output["output_type"] == "display_data":
            return "<INSERT IMG_01>"
        else:
            return
