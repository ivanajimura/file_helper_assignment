# Test Instructions

Typically, one file would have all its tests in a single test file. To divide the tasks more easily, we are creating one file per method.
All tests must be within the folder test/ .
All test file names must begin with test_ or finish with \_test.py . We are going to use test_ as our standard.

# Preparation
It is recommended to create a virtual environment first:
>python -m venv venv
>source venv/bin/activate


Next, Python path must be set:
>export PYTHONPATH='/path/to/main/folder/'

You can check the path is correctly set by:
>echo $PYTHONPATH

Finally, you need to install the needed packages:
>make install-requirements

# Running Tests
You can run all tests in all test files with the following command in the terminal:
>make run-tests

You can run all tests in a single file with the following command in the terminal:
>make run-test-file path=path/to/file/filename.py

You can run a single test from a file with the following command in the terminal:
>make run-test-file path=path/to/file/filename.py method=test_name      # do not use () in the method

You can generate a report in xml format for all the tests:
>make save-test-report filename=filename        # do not use the extension

# Writing Tests
You need to import the file with the functions:
>from src.helper.file_helper import FileHelper

If fixtures are used, you also need to import pytest:
>import pytest

Test results are verified in the *assert* method. __True__ means pass, __False__ means fail.

A single test may have multiple asserts. All asserts must pass for a test to pass.