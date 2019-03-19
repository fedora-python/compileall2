# compileall2 Python module

For now, this is just a copy of `compileall` module from CPython source code.

The goal is to make it compatible for Python >= 3.4 & PyPy 3 and add some features, namely:

* remove a limit of maximum depth limit when looking for files to compile

* add a possibility to strip some part of path to original file from a compiled one

## ToDo

* ✓ Start project :)

* ✓ Make upstream tests running

* Make `compileall2` compatible with CPythons:

  * 3.8 ✓
  * 3.7 ✓
  * 3.6
  * 3.5
  * 3.4

* Make `compileall2` compatible with PyPy 3

* Remove maximum depth limit as described above

* Add possibility to strip some part of a path to an original file from compiled one

* Publish it to PyPI

* Make it available in Fedora

* Test it in Fedora infrastructure with all Python packages

* ? Prepare patches for upstream CPython

## Testing

You can test it locally with tox or unittest directly:

```shell
$ python3 -m unittest test_compileall_original.py
............sss.......................sss.....................ss.................
----------------------------------------------------------------------
Ran 81 tests in 2.137s

OK (skipped=8)
```

but running in a Docker container might be better because the superuser has privileges to write to `sys.path` which lowers the number of skipped tests.

You can just build the prepared one:

```shell
$ docker build -t compileall2 .
Sending build context to Docker daemon 177.2 kB
Step 1/3 : FROM frenzymadness/fedora-python-tox:latest
 ---> 00f92ad0e1d3
... etc ...
```

and run tests in it:

```shell
$ docker run --rm -it -e TOXENV=py37 -v $PWD:/src:Z -w /src  compileall2
py37 create: /src/.tox/py37
py37 installdeps: pytest
py37 installed: atomicwrites==1.3.0,attrs==19.1.0,more-itertools==6.0.0,pluggy==0.9.0,py==1.8.0,pytest==4.3.1,six==1.12.0
py37 run-test-pre: PYTHONHASHSEED='519909491'
py37 runtests: commands[0] | pytest -v -s
========================================== test session starts ==========================================
platform linux -- Python 3.7.2, pytest-4.3.1, py-1.8.0, pluggy-0.9.0 -- /src/.tox/py37/bin/python
cachedir: .tox/py37/.pytest_cache
rootdir: /src, inifile:
collected 81 items

test_compileall_original.py::CompileallTestsWithSourceEpoch::test_compile_dir_pathlike PASSED
test_compileall_original.py::CompileallTestsWithSourceEpoch::test_compile_file_pathlike PASSED
test_compileall_original.py::CompileallTestsWithSourceEpoch::test_compile_file_pathlike_ddir PASSED
... etc ...
================================= 79 passed, 2 skipped in 5.15 seconds ==================================
________________________________________________ summary ________________________________________________
  py37: commands succeeded
  congratulations :)
```
