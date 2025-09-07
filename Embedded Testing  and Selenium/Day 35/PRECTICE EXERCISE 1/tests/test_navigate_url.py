from pages.navigate_url import Navigate
from selenium import webdriver
import pytest
from config.config import Config
from time import sleep
from pages.navigate_url import Navigate

@pytest.mark.usefixtures('init_driver')
class TestUrlNavigation():
    def test_navigation(self):
        nav=Navigate(self.driver)
        nav.navigate_url()
        expected_title = self.driver.title
        assert "Google" in expected_title
        print("Title",expected_title)
        sleep(3)