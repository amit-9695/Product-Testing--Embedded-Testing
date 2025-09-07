# xfail marker - Mark a test as expected to fail
import pytest

@pytest.mark.xfail(reason="This test is expected to fail")
def test_xfail():
    assert 1 == 2  # This test will be marked as expected to fail