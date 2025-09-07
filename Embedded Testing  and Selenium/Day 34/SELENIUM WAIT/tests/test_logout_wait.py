from pages.logout_wait_page import LogoutWait
from pages.login_wait_page import LoginPageWait
from selenium import webdriver
from time import sleep
from config.config import Config
import pytest
import time

@pytest.mark.usefixtures("init_driver")
class TestLogoutWait:
    def test_logoutwait(self):
       
        login_page = LoginPageWait(self.driver)
        login_page.load()
        login_page.login("standard_user","secret_sauce")
        time.sleep(2)
        
        logout_page= LogoutWait(self.driver)
        logout_page.logout_wait()