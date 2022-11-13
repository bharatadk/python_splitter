import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_splitter",
    version="0.0.3",
    author="Bharat Adhikari",
    author_email="bharatadk.on@gmail.com",
    description="A package  that Splits Class_Folders to Train, Test, Val folders automatically by shuffling media for machine learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bharatadk/python_splitter",
        packages=setuptools.find_packages(),
    install_requires=['numpy'], 
    keywords=['folder','splitter'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)