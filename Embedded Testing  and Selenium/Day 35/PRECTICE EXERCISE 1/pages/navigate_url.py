from selenium import webdriver
from config.config import Config
from pages.base_page import BasePage

class Navigate(BasePage):
    def navigate_url(self):
        self.open_url(Config.BASE_URL)
        