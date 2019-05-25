import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="toy-robot",
    version="1.0.0",
    author="Sourabh Kumar",
    author_email="author@example.com",
    description="Toy robot coding challenge",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sourabh1983/toy-robot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
