from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddProductPage(BasePage):
    PRODUCT_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    FIRST_ADD_CART=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/a')
    CONTINUE_BTN=(By.XPATH,'//*[@id="cartModal"]/div/div/div[3]/button')
    SECOND_ADD_CART=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[3]/div/div[1]/div[1]/a')
    VIEW_CART_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    
    PRODUCT_ROW=(By.XPATH,'//*[@id="product-1"] | //*[@id="product-2"]')
    PRODUCT_NAME=(By.XPATH,"//td[@class='cart_description']/h4/a")
    PRODUCT_PRICE=(By.XPATH,"//td[@class='cart_price']/p")
    PRODUCT_QUANTITIES=(By.XPATH,"//*[@class='cart_quantity']/button")
    PRODUCT_TOTAL=(By.XPATH,"//*[@class='cart_total']/p")
    
    def add_cart(self):
        #Click 'Products' button
        self.click_operation(self.PRODUCT_BTN)
        self.scroll_by_operation(0,400)
        self.click_operation(self.FIRST_ADD_CART)
        self.scrollTo_Top_operation()
        #Click 'Continue Shopping' button
        self.click_operation(self.CONTINUE_BTN)
        self.scroll_by_operation(0,400)
        self.click_operation(self.SECOND_ADD_CART)
        self.scrollTo_Top_operation()
        self.click_operation(self.CONTINUE_BTN)
        
        self.scroll_by_operation(0,400)
        self.click_operation(self.SECOND_ADD_CART)
        self.scrollTo_Top_operation()
        self.click_operation(self.CONTINUE_BTN)
     
    #Click 'View Cart' button   
    def view_cart(self):
        self.click_operation(self.VIEW_CART_BTN)
        
    #Verify their prices, quantity and total price
    
    def product_name(self):
        elements=self.find_multiple_web_element(self.PRODUCT_NAME)
        return [e.text for e in elements]
    
    def product_PRICE(self):
        elements=self.find_multiple_web_element(self.PRODUCT_PRICE)
        return [e.text for e in elements]
    
    def product_quantity(self):
        elements=self.find_multiple_web_element(self.PRODUCT_QUANTITIES)
        return [e.text for e in elements]
    
    def product_total_price(self):
        elements=self.find_multiple_web_element(self.PRODUCT_TOTAL)
        return [e.text for e in elements]
    
        
        
        