import pytest


def test_userProgram():
    msg = "Hello"
    assert msg == "Hi", "Test is failed as strings not matched!"


@pytest.mark.smoke
def test_creditProgram():
    a = 4
    b = 6
    assert a + 2 == 6, "Addition not matched."
