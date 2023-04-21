from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="charlogger",
    version="1.2",
    description="A logging library for Python.",
    url="https://github.com/chaarlottte/charlogger",
    author="chaarlottte",
    packages=[ "charlogger" ],
    install_requires=[ 
        "colorama"
    ],
    long_description=long_description,
    long_description_content_type="text/markdown"
)