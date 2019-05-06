# compileall2 Python module

Copy of `compileall` module from CPython source code with some new features, namely:

* compatibility with Python >= 3.4 & PyPy 3

* default recursion limit is now "unlimited" (actually limited by `sys.getrecursionlimit()`)

* `-s` and `-p` command line options for manipulation of the path baked into
  a compiled `*.pyc` file.

* the `-o` command line option can be specified multiple times to compile for 
  multiple optimization levels in one run

## Installation

* From [PyPI](https://pypi.org/project/compileall2/) via `pip install compileall2`

* RPMs will be available in [Fedora COPR](https://copr.fedorainfracloud.org/coprs/lbalhar/compileall2/)

## Usage

`compileall2` can be executed as a Python module or directly.

Example usage:

```shell
# Create some script (this one raises an exception to show tracebacks)
$ echo "1 / 0" > test.py

# Compile it
$ compileall2 test.py
Compiling 'test.py'...

# Try to execute compiled version directly
$ python __pycache__/test.cpython-37.pyc 
Traceback (most recent call last):
  File "test.py", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero

# Recompile it with changes path which will be visible in error message
$ compileall2 -f -p /foo/bar test.py
Compiling 'test.py'...
$ python __pycache__/test.cpython-37.pyc
Traceback (most recent call last):
  File "/foo/bar/test.py", line 1, in <module>
ZeroDivisionError: division by zero

# Same thing as above but executed as a Python module
$ python -m compileall2 -f -p /bar/baz test.py
Compiling 'test.py'...
$ python __pycache__/test.cpython-37.pyc
Traceback (most recent call last):
  File "/bar/baz/test.py", line 1, in <module>
ZeroDivisionError: division by zero
```

## Done

* ✓ Start project :)

* ✓ Make upstream tests running

* Make `compileall2` compatible with CPythons:

  * 3.8 ✓
  * 3.7 ✓
  * 3.6 ✓
  * 3.5 ✓
  * 3.4 ✓

* ✓ Make `compileall2` compatible with PyPy 3

* ✓ Remove maximum depth limit as described above

* ✓ Add possibility to strip some part of a path to an original file from compiled one

* ✓ Publish it to PyPI

* ✓ Make it available in Fedora COPR

## ToDo

* **[NEXT STEP]** Test it with Python packages in COPR

* Push it to Fedora rawhide

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

## License

[PSF license v2](LICENSE)
