# Basic Reference Example of Packaging a Python Application

This how to guide was taken from the following [reference](https://packaging.python.org/tutorials/installing-packages/).

python -m pip install --upgrade pip setuptools wheel


```bash
virtualenv <DIR>
source <DIR>/bin/activate
```

useful ref: (the main source of information for this project)
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

Make sure you have an account on [TestPyPI](https://test.pypi.org/)

Get an API Token

create the ```$HOME/.pypirc```

```bash
vim $HOME/.pypirc
```

Good quick reference for classes as well [here](https://en.wikibooks.org/wiki/A_Beginner%27s_Python_Tutorial/Classes)

make sure twine is updated

```bash
python3 -m pip install --user --upgrade twine
```

upload!

```bash
python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

e.g.

```bash
(poc) nsheridan@srv1:~/code/packaging/nikpack$ python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Enter your password: 
Uploading nik_motd_niksheridan-0.0.1-py3-none-any.whl
100%|██████████| 5.94k/5.94k [00:01<00:00, 3.60kB/s]
Uploading nik_motd-niksheridan-0.0.1.tar.gz
100%|██████████| 4.59k/4.59k [00:00<00:00, 4.89kB/s]

View at:
https://test.pypi.org/project/nik-motd-niksheridan/0.0.1/
(poc) nsheridan@srv1:~/code/packaging/nikpack$ 
```

* IMPORTANT * When changing the version for a new release make sure you delete the exiting files in the ```<project>/build/dist```folder
(see [reference link here](https://stackoverflow.com/questions/52700692/a-guide-for-updating-packages-on-pypi)), otherwise:

```bash
(poc) nsheridan@srv1:~/code/packaging/nikpack$ python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: __token__
Enter your password: 
Uploading nik_motd_niksheridan-0.0.1-py3-none-any.whl
100%|██████████| 5.88k/5.88k [00:00<00:00, 7.08kB/s]
NOTE: Try --verbose to see response content.
HTTPError: 400 Client Error: File already exists. See https://test.pypi.org/help/#file-name-reuse for url: https://test.pypi.org/legacy/
```


## Usage

```python
>>> import nik_motd.nik_motd as nik
>>> cat = nik.Banner('tester')
>>> cat.print_pretty_banner()
+==================================================+
tester
+==================================================+
>>> cat = nik.Banner('fish face')
>>> cat.print_pretty_banner()
+==================================================+
fish face
+==================================================+
>>>
```

Or

```bash
(test2) nsheridan@srv1:~$ python
Python 3.6.9 (default, Nov  7 2019, 10:44:02) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from nik_motd import nik_motd as nik
>>> cat = nik.Banner('fish face')
>>> cat.print_pretty_banner()
+==================================================+
fish face
+==================================================+
>>> 
```