# Test Case 14: Place Order: Register while Checkout

from selenium.webdriver.common.by import By
from pages.regester_pages import RgesterPage

class RegisterWhileCheckout(RgesterPage):
    ADD_TO_CART=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a')
    VIEW_CART=(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    PROCEED_TO_CHECKOUT=(By.XPATH,'//*[@id="do_action"]/div[1]/div/div/a')
    REGISTER_LOGIN_BTN=(By.XPATH,'//*[@id="checkoutModal"]/div/div/div[2]/p[2]/a/u')
    
    CART_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    
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
    
    def add_product(self):
        self.click_operation(self.ADD_TO_CART)
        
    def view_cart(self):
        self.click_operation(self.VIEW_CART)
        
    def proceed_to_checkout(self):
        self.click_operation(self.PROCEED_TO_CHECKOUT)
        
    def click_register_login(self):
        self.click_operation(self.REGISTER_LOGIN_BTN)
        
    # Now using functios of register page to signup
    def signup(self):
        self.enter_signup_details("Amit Shukla","amitshukla15551@gmail.com")
        
        self.fill_account_info("Amit@123","1",'November','2001')
        
        self.address_info("first_name","last_name","company","address1","address2 of my","India","state","city",271201,9695230479)
        
        self.create_account()
        
    #Click 'Cart' button
    def click_cart(self):
        self.click_operation(self.CART_BTN)
    
    #Verify Address Details     
    def verify_address(self):
        return self.find_web_element(self.ADDRESS_DETAIL).text
    
    #Verify Review Your Order
    def verify_review(self):
        return self.find_web_element(self.REVIEW_ORDER).text
    
    #Enter description in comment text area and click 'Place Order'
    def place_order(self,msg):
        self.scrollTo_bottom_operation()
        self.enter_value_operation(self.MESSAGE,msg)
        self.click_operation(self.PLACE_ORDER)
    
    #. Enter payment details: Name on Card, Card Number, CVC, Expiration date    
    def payment(self,name,number,cvv,month,year):
        self.scroll_by_operation(0,350)
        self.enter_value_operation(self.CARD_NAME,name)
        self.enter_value_operation(self.CARD_NUMBER,number)
        self.enter_value_operation(self.CVV,cvv)
        self.enter_value_operation(self.EXP_MON,month)
        self.enter_value_operation(self.EXP_YEAR,year)
        
    #Click 'Pay and Confirm Order' button
    def click_and_pay(self):
        self.click_operation(self.PAY)
    
    #Verify success message 'Congratulations! Your order has been confirmed!'    
    def final_msg(self):
        return self.find_web_element(self.FINAL_MSG).text
    
    
    
    
    
    
    
        
    