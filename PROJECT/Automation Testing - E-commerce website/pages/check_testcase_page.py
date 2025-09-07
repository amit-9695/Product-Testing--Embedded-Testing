from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver
class CheckTestcasePage(BasePage):
    TEST_CASE_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    
    def check_testcase_page(self):
        self.click_operation(self.TEST_CASE_BTN)