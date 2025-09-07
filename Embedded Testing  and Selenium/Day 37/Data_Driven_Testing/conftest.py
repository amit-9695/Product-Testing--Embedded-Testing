import pytest
from util.driver_factory import get_driver
from config.config import Config

@pytest.fixture(scope="class")
def init_driver(request):
    driver=get_driver()
    request.cls.driver=driver
    yield 
    driver.quit()
    