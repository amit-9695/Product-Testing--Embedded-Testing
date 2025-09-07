from selenium.webdriver.common.by import By
from selenium import webdriver
from pages.base_page import BasePage

class ContactPage(BasePage):
    CONTACT_BTN = (By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[8]/a')
    GET_IN_TOUCH = (By.XPATH,'//*[@id="contact-page"]/div[2]/div[1]/div/h2')
    NAME_INPUT=(By.XPATH,'//*[@id="contact-us-form"]/div[1]/input')
    EMAIL_INPUT = (By.XPATH,'//*[@id="contact-us-form"]/div[2]/input')
    SUBJECT_INPUT=(By.XPATH,'//*[@id="contact-us-form"]/div[3]/input')
    MESSAGE_INPUT=(By.XPATH,'//*[@id="message"]')
    FILE_UPLOAD_BTN=(By.XPATH,'//*[@id="contact-us-form"]/div[5]/input')
    SUBMIT_BTN=(By.XPATH,'//*[@id="contact-us-form"]/div[6]/input')
    SUCESS_MSG = (By.XPATH,'//*[@id="contact-page"]/div[2]/div[1]/div/div[2]')
    HOME_BTN = (By.XPATH,'//*[@id="form-section"]/a/span')
    def contact_page(self):
        self.click_operation(self.CONTACT_BTN)
    
    def get_in_touch(self):
        return self.find_web_element(self.GET_IN_TOUCH).text
    
    def enter_detail(self,name,email,subject,msg):
        self.enter_value_operation(self.NAME_INPUT,name)
        self.enter_value_operation(self.EMAIL_INPUT,email)
        self.enter_value_operation(self.SUBJECT_INPUT,subject)
        self.enter_value_operation(self.MESSAGE_INPUT,msg)
        
    def upload_file(self,file_path):
        self.find_web_element(self.FILE_UPLOAD_BTN).send_keys(file_path)
        
    def submit_form(self):
        self.click_operation(self.SUBMIT_BTN)
        
    def alert_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()
        
    def sucess_message(self):
        return self.find_web_element(self.SUCESS_MSG).text
    
    def return_home(self):
        self.click_operation(self.HOME_BTN)
        