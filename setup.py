from setuptools import setup, find_packages
import os


with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="mcscan",
    version="1.4",
    packages=find_packages(),
    install_requires=[
        "requests",
        "rich",
        "termcolor",
    ],
    entry_points={
        "console_scripts": [
            "mcscan=mc_server_status.main:cli_entry_point",
        ]
    },
    author="Moritz Maier",
    author_email="moritzmaier353@gmail.com",
    description="A cli application to fetch data from your favourite minecraft server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Moritz344/mcstatus-cli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

