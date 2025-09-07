import pytest
from utils.diver_factory import driver_factory
from configs.config import Config

@pytest.fixture(scope="class")
def init_driver(request):
    driver = driver_factory('edge')
    
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    request.cls.driver=driver
    yield
    driver.save_screenshot("example.png")
    print("All Test cases Passed.")
    driver.quit()