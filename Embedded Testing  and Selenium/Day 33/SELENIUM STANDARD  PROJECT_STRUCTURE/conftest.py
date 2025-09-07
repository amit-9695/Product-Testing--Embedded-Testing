# In his we define the fixtures for the Selenium tests
import pytest
from config.config import Config
from util.driver_factory import get_driver

@pytest.fixture(scope="class")
def init_driver(request):
    driver=get_driver("chrome")
    request.cls.driver=driver
    yield
    driver.quit()
 