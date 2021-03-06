import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-jsend-response",
    version="0.0.2",
    author="AntLouiz",
    author_email="luizrodrigo46@hotmail.com",
    description="python-jsend-response is a simply python implementation of JSend.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntLouiz/pyjsend",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)
