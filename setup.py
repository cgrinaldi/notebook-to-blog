from setuptools import setup, find_packages

setup(
    name="notebook_to_blog",
    version="0.0.1",
    author_email="cgrinaldi@gmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=["Click"],
    entry_points={"console_scripts": ["notebook_to_blog = notebook_to_blog.cli:main"]},
)
