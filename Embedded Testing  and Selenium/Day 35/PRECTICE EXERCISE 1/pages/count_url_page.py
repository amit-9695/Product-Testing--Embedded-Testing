import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config

class CountUrlPage(BasePage):
    COUNT_LINLS = (By.TAG_NAME,"a")
    
    def count_links(self):
        self.open_url(Config.PYTHON_URL)
        tag = self.driver.find_elements(*self.COUNT_LINLS)
        print("Total Anchor Tag: ",len(tag))
        
    