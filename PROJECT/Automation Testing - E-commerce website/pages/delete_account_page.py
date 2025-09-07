from selenium import webdriver
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class DeleteAccountPage(BasePage):
    DELETE_ACCOUNT_BTN =(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    ACCOUNT_DELETED= (By.XPATH,'//*[@id="form"]/div/div/div/h2/b')
    CONTINUE_AFTER_DELETE = (By.XPATH,'//*[@id="form"]/div/div/div/div/a')
    
    def delete_account(self):
        self.click_operation(self.DELETE_ACCOUNT_BTN)
        self.click_operation(self.CONTINUE_AFTER_DELETE)