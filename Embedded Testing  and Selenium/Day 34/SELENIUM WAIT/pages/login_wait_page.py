from selenium.webdriver.common.by import By
from util.wait_utils import WaitUtils
from pages.base_page import BasePage
from selenium import webdriver
from config.config import Config

class LoginPageWait(BasePage):
    
    USERNAME_LOCATOR = (By.ID, "user-name")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    
        
    def load(self):
        self.driver.get(Config.BASE_URL)
        
    def login(self,username,password):
        self.enter_text(self.USERNAME_LOCATOR,username)
        self.enter_text(self.PASSWORD_LOCATOR,password)
        self.click_element(self.LOGIN_BUTTON_LOCATOR)
        
    
    