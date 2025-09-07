from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver

class SubscribeCartPage(BasePage):
    CART=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    SUBSCRIPTION_TEXT=(By.XPATH,'//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    EMAIL_INPUT=(By.XPATH,'//*[@id="susbscribe_email"]')
    ARROW=(By.XPATH,'//*[@id="subscribe"]')
    SUCCESS_MSG=(By.XPATH,'//*[@id="success-subscribe"]/div')
    
    def cart_page(self):
        self.click_operation(self.CART)
        
    def scroll_bottom(self):
        self.scrollTo_bottom_operation()
        
    def verify_subscribe_page(self):
        return self.find_web_element(self.SUBSCRIPTION_TEXT).text
        
    def subscribe_page(self,email):
        self.enter_value_operation(self.EMAIL_INPUT,email)
        self.click_operation(self.ARROW)
        
    def sucess_message_page(self):
        return self.find_web_element(self.SUCCESS_MSG).text
        
        