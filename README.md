# Notebook to Blog

## Overview

**Notebook to Blog** is a Python CLI that makes it easy to go from a Jupyter Notebook to the following outputs:
- A .txt file containing blog text and placeholders
- Images of plots (saved locally)
- Github Gists

While not completely automated, this will make it much easier to create a blog post (e.g., Medium).

## Instructions

1. Install via `pip install notebook-to-blog`.
2. Store your Github username/password somewhere in your filesystem:

```
GITHUB_USER=<username>
GITHUB_PASSWORD=<password>
```
3. Run via `notebook_to_blog <path to Jupyter notebook> <path to output directory> <path to Github credentials>`

For example, running `notebook_to_blog my_notebook.ipynb output .env` will create the following files:

```
output/
  my_notebok.txt
  images/
    image_00.png
```

In addition, Github Gists will be created for each code block encountered.

**my_notebook.txt** looks like the following:

```
Whatever you wrote in Markdown will appear as regular text. Code blocks will cause Github Gists to be created, and a link to be inserted:

https://gist.github.com/cgrinaldi/1a11acbdc9006849323163e354955a31

Images will also be represented as placeholder text:

<INSERT img_04.png>
```
