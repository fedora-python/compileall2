import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="compileall2",
    version="0.4.0",
    author="Lumír Balhar",
    author_email="frenzy.madness@gmail.com",
    description="Enhanced Python `compileall` module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frenzymadness/compileall2",
    py_modules=["compileall2"],
    entry_points='''
        [console_scripts]
        compileall2=compileall2:main
    ''',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Software Development :: Compilers",
    ],
)