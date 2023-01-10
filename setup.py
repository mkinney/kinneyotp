import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

with open("README.md", "r") as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="kinneyotp",
    version="0.0.15",
    description="One Time Pad (aka Vernam Cipher) encoding and decoding.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Mike Kinney",
    author_email="mike.kinney@gmail.com",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["kinneyotp"],
    include_package_data=True,
    install_requires=[],
    extras_require={},
    python_requires='>=3.7',
    entry_points={
    },
)
