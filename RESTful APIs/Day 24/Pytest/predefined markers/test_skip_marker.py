# skip markrer- Skip a test unconditionally
import pytest

@pytest.mark.skip(reason="The test is not implemented yet")
def test_skip():
    assert 1==2   # This is a false test case, but it will be skipped