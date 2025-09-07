# filterwarnings marker -Control warning messages during test execution
import pytest
import warnings
@pytest.mark.filterwarnings("ignore:.*deprecated.*")
def test_filterwarnings():
    # This test will ignore any warnings that match the specified pattern
    warnings.warn("This is a deprecated warning", DeprecationWarning)
    assert True
    
