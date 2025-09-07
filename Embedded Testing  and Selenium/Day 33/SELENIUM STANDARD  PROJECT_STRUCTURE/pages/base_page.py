# In this we write comon operations that can be used across different pages

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        
    def open_url(self, url):
        """Open the specified URL in the browser."""
        self.driver.get(url)
        
        
    def find_element(self, locator):
        """Find an element on the page using the provided locator."""
        return self.driver.find_element(*locator)
    
    def enter_text(self, locator, text):
        """Enter text into an input field."""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        
    def click_element(self, locator):
        """Click on an element."""
        element = self.find_element(locator)
        self.actions.click(element).perform()
        