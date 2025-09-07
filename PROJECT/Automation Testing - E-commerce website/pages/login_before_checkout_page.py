from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginbeforePage(BasePage):
    LOGIN_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a')
    EMAIL=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[2]')
    PASSWORD=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/input[3]')
    LOGIN=(By.XPATH,'//*[@id="form"]/div/div/div[1]/div/form/button')
    LOGIN_AS=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    PRODUCT_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    ADD_TO_CART=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
    
    CART_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a/i')
    PROCEED_TO_CHECKOUT=(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a')
    ADDRESS_DETAIL=(By.XPATH,'//*[@id="cart_items"]/div/div[2]/h2')
    REVIEW_ORDER=(By.XPATH,'//*[@id="cart_items"]/div/div[4]/h2')
    MESSAGE=(By.XPATH,'//*[@id="ordermsg"]/textarea')
    PLACE_ORDER=(By.XPATH,'//*[@id="cart_items"]/div/div[7]/a')
    
    CARD_NAME=(By.XPATH,'//*[@id="payment-form"]/div[1]/div/input')
    CARD_NUMBER=(By.XPATH,'//*[@id="payment-form"]/div[2]/div/input')
    CVV=(By.XPATH,'//*[@id="payment-form"]/div[3]/div[1]/input')
    EXP_MON=(By.XPATH,'//*[@id="payment-form"]/div[3]/div[2]/input')
    EXP_YEAR=(By.XPATH,'//*[@id="payment-form"]/div[3]/div[3]/input')
    PAY=(By.XPATH,'//*[@id="submit"]')
    FINAL_MSG=(By.XPATH,'//*[@id="form"]/div/div/div/p')
    
    def login(self,email,password):
        self.click_operation(self.LOGIN_BTN)
        self.enter_value_operation(self.EMAIL,email)
        self.enter_value_operation(self.PASSWORD,password)
        self.click_operation(self.LOGIN)
        
    def login_as(self):
        return self.find_web_element(self.LOGIN_AS).text
    
    def add_product(self):
        self.click_operation(self.PRODUCT_BTN)
        self.scroll_by_operation(0,400)
        self.click_operation(self.ADD_TO_CART)
        
    def click_cart(self):
        self.click_operation(self.CART_BTN)
        
    def proceed_to_checkout(self):
        self.click_operation(self.PROCEED_TO_CHECKOUT)
        
    def verify_address(self):
        return self.find_web_element(self.ADDRESS_DETAIL).text
    
    def verify_review(self):
        return self.find_web_element(self.REVIEW_ORDER).text
    
    def place_order(self,msg):
        self.scrollTo_bottom_operation()
        self.enter_value_operation(self.MESSAGE,msg)
        self.click_operation(self.PLACE_ORDER)
        
    def payment(self,name,number,cvv,month,year):
        self.scroll_by_operation(0,350)
        self.enter_value_operation(self.CARD_NAME,name)
        self.enter_value_operation(self.CARD_NUMBER,number)
        self.enter_value_operation(self.CVV,cvv)
        self.enter_value_operation(self.EXP_MON,month)
        self.enter_value_operation(self.EXP_YEAR,year)
        self.click_operation(self.PAY)
        
    def final_msg(self):
        return self.find_web_element(self.FINAL_MSG).text
        