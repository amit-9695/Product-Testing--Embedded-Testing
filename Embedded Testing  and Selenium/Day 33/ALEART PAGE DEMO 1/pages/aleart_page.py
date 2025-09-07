from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
import time


class AlertPage:
    URL = "https://selenium08.blogspot.com/2019/07/alert-test.html"
    SIMPLE_ALERT_LOCATOR = (By.ID, "simple")
    CONFIRM_ALERT_LOCATOR = (By.ID, "confirm")
    PROMPT_ALERT_LOCATOR = (By.ID, "prompt")
    PROMPT_MESSAGE_LOCATOR = (By.ID, "prompt_demo")
    
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(driver)
        
    def open_url(self):
        self.driver.get(self.URL)
        
        
    def click_simple_alert(self):
        self.driver.find_element(*self.SIMPLE_ALERT_LOCATOR).click()
        
        # switchfrom webpage to alert
        alert = self.driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()  # Accept the alert to close it
        
    def click_confirm_alert(self):
        confirm_button = self.driver.find_element(*self.CONFIRM_ALERT_LOCATOR)
        self.actions.click(confirm_button).perform()
        # switch from webpage to alert
        alert = self.driver.switch_to.alert
        print(f"Alert text: {alert.text}")
        alert.accept()
        
        
    def click_prompt_alert(self):
        prompt_button = self.driver.find_element(*self.PROMPT_ALERT_LOCATOR)
        self.actions.click(prompt_button).perform()
        
        # switch from webpage to alert
        alert = self.driver.switch_to.alert
        alert.send_keys("Amit Shukla")
        print(f"Alert text: {alert.text}")
        # using .accept() to close the alert
        alert.accept()
        time.sleep(2)
        
    def get_prompt_message(self):
        msg= self.driver.find_element(*self.PROMPT_MESSAGE_LOCATOR)
        print(f"Prompt message: {msg.text}")