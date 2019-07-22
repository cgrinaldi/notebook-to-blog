import base64


def save_image(img_data, img_num, output_dir=None):
    """Save image base64 data as image with suffix {img_num}."""
    if output_dir:
        # setup the image directory
        img_dir = output_dir / "images/"
        img_dir.mkdir(parents=True, exist_ok=True)

        # save image file to image dir
        filepath = img_dir / f"image_{img_num}.png"
        with open(filepath, "wb") as f:
            f.write(base64.decodebytes(bytes(img_data, "utf-8")))


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
    def __init__(self, idx, contents, output_dir=None):
        super().__init__(contents)
        self.idx = idx
        self.output_dir = output_dir

    def convert(self):
        return self._convert_source() + "\n\n" + self._convert_outputs()

    def _convert_source(self):
        return "```\n" + "".join(self.contents["source"]) + "\n```"

    def _convert_outputs(self):
        result = []
        for o in self.contents["outputs"]:
            result.append(self._convert_output(o))
        return "\n\n".join(result)

    def _convert_output(self, output):
        if output["output_type"] == "stream":
            return "```\n" + "".join(output["text"]) + "```"
        elif output["output_type"] == "execute_result":
            return "```\n" + "".join(output["data"]["text/plain"]) + "\n```"
        # TODO: Save images to file system (in a figures directory)
        elif output["output_type"] == "display_data":
            save_image(output["data"]["image/png"], self.idx, self.output_dir)
            return f"<INSERT img_{self.idx}.png>"
        else:
            return
