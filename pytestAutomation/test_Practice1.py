# Any pytest file should start with test_ or end with _test
# pytest method name should start with test
# Any codee should be wrapped in method only
# In pytest we can't declare method name same, if declare then it will override the previous method
# CMD for run all TC py.test -v -s
# CMD for run specific file py.test test_Practice1.py -v -s
# - k stands for method names execution, -s logs in output, -v stands for more metadata
# Run any specific method on a file ---> py.test -k test_firstProgram -v -s
# we can mark(tag) test @pytest.mark.some and then run with -m
# pytest.mark.xfail is used for not to show pass or failed status in reports

import pytest


@pytest.mark.xfail
def test_firstProgram():
    print("Hello 1")


@pytest.mark.skip
def test_secondProgram():
    print("Hello 2")
