# Basic Reference Example of Packaging a Python Application

This how to guide was taken from the following [reference](https://packaging.python.org/tutorials/installing-packages/).

python -m pip install --upgrade pip setuptools wheel


```bash
virtualenv <DIR>
source <DIR>/bin/activate
```

useful ref:
https://docs.python.org/3/distributing/index.html

## Read this first

https://docs.python.org/3/tutorial/modules.html#packages


## Start with a Clean Environemnt

Ideally, to avoid any confusion, create a virtual environment, activate it, and install
the basic packages required:

```bash
python3 -m venv poc
source poc/bin/activate
python -m pip install setuptools wheel twine
```


Now run this command from the same directory where setup.py is located:

```bash
python3 setup.py sdist bdist_wheel
```

Good quick reference for classes as well [here](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Classes)