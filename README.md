# compileall2 Python module

Copy of `compileall` module from CPython source code with some new features, namely:

* compatibility with Python >= 3.6 & PyPy 3

The following features were first implemented in this project and then included
into the standard libraty of CPython.

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

* In Fedora Linux, compileall2.py is a part of python-srpm-macros RPM package.

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

## Testing

You can test it locally with tox or unittest directly:

```shell
$ python3 -m unittest test_compileall2.py
..............sss....ss.......................sss....ss.....................ss.............................----------------------------------------------------------------------
Ran 107 tests in 3.714s

OK (skipped=12)
```

but running in a container might be better because the superuser has privileges to write to `sys.path` which lowers the number of skipped tests.

## License

[PSF license v2](LICENSE)
