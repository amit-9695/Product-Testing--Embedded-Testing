# skipif marker - Skip a test based on a condition
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (4, 8), reason="Python version is less than 3.8")
def test_skipif():
    assert 1 == 1  # This test will be skipped if Python version is less than 3.8