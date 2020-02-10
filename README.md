# compileall2 Python module

Copy of `compileall` module from CPython source code with some new features, namely:

* compatibility with Python >= 3.4 & PyPy 3

* default recursion limit is now "unlimited" (actually limited by `sys.getrecursionlimit()`)

* `-s` and `-p` command line options for manipulation of the path baked into
  a compiled `*.pyc` file.

* the `-o` command line option can be specified multiple times to compile for 
  multiple optimization levels in one run

* the `-e` command line option for ignoring symlinks pointing outside a specific directory

* the `--hardlink-dupes` command line option which creates hardlinks between
  `.pyc` files with the same content

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

* ✓ Test it with Python packages in COPR

* Push it to Fedora rawhide

  * ✓ %py_byte_compile RPM macro uses `compileall2` (done in [python-rpm-macros](https://src.fedoraproject.org/rpms/python-rpm-macros/pull-request/25))
  * ✓ switch brp-python-bytecompile RPM script to `compileall2` (done in [redhat-rpm-config](https://src.fedoraproject.org/rpms/redhat-rpm-config/pull-request/64#))

* ✓ Test it in Fedora infrastructure with all Python packages (done in the mass rebuild for Fedora 31)

* ✓ Prepare patches for upstream CPython
    * [Pull request](https://github.com/python/cpython/pull/16012) merged and will be part of Python 3.9

* ✓ Changes from upstream CPython backported back

* ✓ Implemented important features for Fedora RPM build system

## Testing

You can test it locally with tox or unittest directly:

```shell
$ python3 -m unittest test_compileall2.py
..............sss....ss.......................sss....ss.....................ss.............................----------------------------------------------------------------------
Ran 107 tests in 3.714s

OK (skipped=12)
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
py37 installed: atomicwrites==1.3.0,attrs==19.3.0,compileall2==0.5.0,coverage==4.5.4,importlib-metadata==0.23,more-itertools==7.2.0,packaging==19.2,pluggy==0.13.0,py==1.8.0,pyparsing==2.4.5,pytest==5.2.3,six==1.13.0,wcwidth==0.1.7,zipp==0.6.0
py37 run-test-pre: PYTHONHASHSEED='1615314833'
py37 runtests: commands[0] | coverage run --append -m py.test
==================================== test session starts =====================================
platform linux -- Python 3.7.5, pytest-5.2.3, py-1.8.0, pluggy-0.13.0
cachedir: .tox/py37/.pytest_cache
rootdir: /src
collected 107 items
test_compileall2.py ............ss..................................................ss [ 61%]
..............................ss.........                                              [100%]

=============================== 101 passed, 6 skipped in 7.40s ===============================
py37 runtests: commands[1] | coverage report -i '--omit=.tox/*'
Name                  Stmts   Miss  Cover
-----------------------------------------
compileall2.py          232     48    79%
test_compileall2.py     621      8    99%
-----------------------------------------
TOTAL                   853     56    93%
__________________________________________ summary ___________________________________________
  py37: commands succeeded
  congratulations :)
```

## License

[PSF license v2](LICENSE)
