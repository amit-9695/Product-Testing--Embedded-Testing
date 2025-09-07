from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SubscriptionPage(BasePage):
    SUBSCRIIPTION=(By.XPATH,'//*[@id="footer"]/div[1]/div/div/div[2]/div/h2')
    EMAIL_INPUT=(By.XPATH,'//*[@id="susbscribe_email"]')
    ARROW_BTN=(By.XPATH,'//*[@id="subscribe"]')
    ALERT=(By.XPATH,'//*[@id="success-subscribe"]/div')
    def scroll_botton(self):
        self.scrollTo_bottom_operation()
        
    def scroll_top(self):
        self.scrollTo_Top_operation()
        
    def verify_subscription(self):
        return self.find_web_element(self.SUBSCRIIPTION).text
    
    def subscribe(self,email):
        self.enter_value_operation(self.EMAIL_INPUT,email)
        self.click_operation(self.ARROW_BTN)
    
    def get_alert_text(self):
        return  self.find_web_element(self.ALERT).text