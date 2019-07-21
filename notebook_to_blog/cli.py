import click
from pathlib import Path

from notebook_to_blog.notebook import Notebook


def create_filename(notebook_path):
    return notebook_path.name.split(".")[0] + ".txt"


@click.command()
@click.argument("notebook_path")
@click.argument("output_dir")
def main(notebook_path, output_dir):
    # pull in notebook
    notebook_path = Path(notebook_path)
    notebook = Notebook(notebook_path)

    # convert notebook and save to desired location
    output_filename = create_filename(notebook_path)
    with open(Path(output_dir) / output_filename, "w") as f:
        f.write(notebook.convert())
