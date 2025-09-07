from selenium import webdriver
from config.config import Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_LOCATOR= (By.XPATH,"//input[@id='username']")
    PASSWORD_LOCATOR= (By.XPATH,"//input[@id='password']")
    SUBMIT_BTN=(By.XPATH,"//button[@id='submit']")
    def login(self,username,password):
        self.open_url(Config.LOGIN_URL)
        self.enter_text(self.USERNAME_LOCATOR,username)
        self.enter_text(self.PASSWORD_LOCATOR,password)
        self.click_element(self.SUBMIT_BTN)