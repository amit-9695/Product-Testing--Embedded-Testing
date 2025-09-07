# Test Case 2: Login User with correct email and password
import pytest
from time import sleep
from configs.config import Config
from pages.login_page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLoginPage:
    def test_login_page(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        login=LoginPage(self.driver)
        #Enter correct email address and password
        login.login_page(Config.EMAIL,Config.PASSWORD)
        sleep(2)