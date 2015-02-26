from setuptools import setup

setup(
    name = "line_to_path",
    version = '0.0.1',
    description = "plugin that converts a file name and a line numer into a module path",
    url = "https://github.com/dmcaulay/line_to_path",
    author = "Dan McAulay",
    author_email = "dmcaulay@gmail.com",
    license = "MIT",
    packages = ["line_to_path"],
    scripts = ["bin/line_to_path"],
)
