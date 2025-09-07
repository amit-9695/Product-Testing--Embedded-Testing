from pages.login_wait_page import LoginPageWait
from selenium import webdriver
from time import sleep
from config.config import Config
import pytest
import time

@pytest.mark.usefixtures("init_driver")
class TestLoginWait:
    def test_loginwait(self):
       
        login_page = LoginPageWait(self.driver)
        login_page.load()
        login_page.login("standard_user","secret_sauce")
        time.sleep(2)
        
