# Test Case -2 
from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage

class LoginPage(BasePage):
    SIGNUP_LOGIN_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    LOGIN_EMAIL = (By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    LOGIN_PASSWORD=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    LOGIN_BTN = (By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/button')
    INCORRECT_MSG=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/p')
    
    def login_page(self,email,password):
        self.click_operation(self.SIGNUP_LOGIN_BTN)
        self.enter_value_operation(self.LOGIN_EMAIL,email)
        self.enter_value_operation(self.LOGIN_PASSWORD,password)
        self.click_operation(self.LOGIN_BTN)
        
    def incorrect_msg(self):
        return self.find_web_element(self.INCORRECT_MSG).text