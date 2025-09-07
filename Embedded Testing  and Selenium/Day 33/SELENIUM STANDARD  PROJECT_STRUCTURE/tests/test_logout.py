from pages.logout_page import LogoutPage
from pages.login_page import LoginPage
from selenium import webdriver
import pytest
from config.config import Config
from time import sleep

@pytest.mark.usefixtures("init_driver")
class TestLogout:
    def test_login_logout(self):
        """Test case for successful logout."""
        # Initialize the login page and perform login
        login_page = LoginPage(self.driver)
        login_page.open_url(Config.BASE_URL)
        login_page.login("standard_user", "secret_sauce")
        sleep(2)
        # Initialize the logout page and perform logout
        logout_page = LogoutPage(self.driver)
        logout_page.logout()
        sleep(3)
        