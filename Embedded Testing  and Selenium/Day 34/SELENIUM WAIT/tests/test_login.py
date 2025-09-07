from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep
from config.config import Config
import pytest

@pytest.mark.usefixtures("init_driver")
class TestLogin:
    def test_login_success(self):
        """Test case for successful login."""
        # driver = webdriver.Chrome()
        # driver.maximize_window()
        
        # Using the fixture to get the driver , thats why we commented the above line number 12
        login_page = LoginPage(self.driver)
        login_page.open_url(Config.BASE_URL)
        login_page.login("standard_user", "secret_sauce")
        sleep(2)
    
    