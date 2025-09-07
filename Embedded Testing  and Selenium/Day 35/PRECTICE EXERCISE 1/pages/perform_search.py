from selenium import webdriver
from config.config import Config
from pages.navigate_url import Navigate
from selenium.webdriver.common.by import By

class PerformSearch(Navigate):
    SEARCH_BAR_LOCATOR= (By.ID,'APjFqb') 
    SEARCH_BTN=(By.XPATH,"//input[@value='Google Search']")
    def search(self,enter_text):
        self.navigate_url()
        self.enter_text(self.SEARCH_BAR_LOCATOR,enter_text)
        self.click_element(self.SEARCH_BTN)
        