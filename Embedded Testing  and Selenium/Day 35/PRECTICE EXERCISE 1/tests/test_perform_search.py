from pages.navigate_url import Navigate
from selenium import webdriver
import pytest
from config.config import Config
from time import sleep
from pages.perform_search import PerformSearch


@pytest.mark.usefixtures('init_driver')
class TestUrlNavigation():
    def test_navigation(self):
        per_search=PerformSearch(self.driver)
        per_search.search("Mahatma Gandhi")
        sleep(20)