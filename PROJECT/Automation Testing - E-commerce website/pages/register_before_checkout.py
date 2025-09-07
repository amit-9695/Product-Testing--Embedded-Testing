#Test Case 15: Place Order: Register before Checkout
from pages.regester_while_checkout import RegisterWhileCheckout
from selenium.webdriver.common.by import By

class RegisterBeforeCheckout(RegisterWhileCheckout):
    LOGIN_SIGNUP_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    
    #Click 'Signup / Login' button
    def click_signup_btn(self):
        self.click_operation(self.LOGIN_SIGNUP_BTN)
        
    #Fill all details in Signup and create account
