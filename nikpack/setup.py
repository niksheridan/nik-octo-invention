import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nik_motd-niksheridan", # Replace with your own username
    version="0.0.2",
    author="Nik Sheridan",
    author_email="nik.sheridan@gmail.com",
    description="A test package used to obtain familiarity with packaging and not intended for real use.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/niksheridan/nik-octo-invention",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
