# In his we define the fixtures for the Selenium tests
import pytest
from config.config import Config
from utils.driver_factory import driver_factory

@pytest.fixture(scope="class")
def init_driver(request):
    driver=driver_factory("edge")
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()
 