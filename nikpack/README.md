# Nik MOTD

This package is not intended for use, but rather as an exercise in 
packaging.

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
sheridan@srv1:~$ python3 -m venv test2
nsheridan@srv1:~$ source test2/bin/activate
(test2) nsheridan@srv1:~$ pip install -i https://test.pypi.org/simple/ nik-motd-niksheridan
Collecting nik-motd-niksheridan
  Downloading https://test-files.pythonhosted.org/packages/2a/72/b6252ad0fd4a2a6cd7e102ee06611a3a0c0b5b872c6fa7cb085c7bfd5ea5/nik_motd_niksheridan-0.0.1-py3-none-any.whl
Installing collected packages: nik-motd-niksheridan
Successfully installed nik-motd-niksheridan-0.0.1
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