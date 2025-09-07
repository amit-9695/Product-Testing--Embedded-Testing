# In this we write comon operations that can be used across different pages

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait= WebDriverWait(driver,timeout=10)
        
    def open_url(self, url):
        """Open the specified URL in the browser."""
        
        self.driver.get(url)
        
        
    def find_element(self, locator):
        """Find an element on the page using the provided locator."""
        return self.driver.find_element(*locator)
    
    def enter_text(self, locator, text):
        """Enter text into an input field."""
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        
    def click_element(self, locator):
        """Click on an element."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()
        