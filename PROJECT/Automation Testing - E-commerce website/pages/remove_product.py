#Test Case 17: Remove Products From Cart

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RemoveProduct(BasePage):
    ADD_PRODUCT=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[1]/div[1]/a')
    CART_BTN=(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    X_BTN=(By.XPATH,'//*[@id="product-1"]/td[6]/a/i')
    EMPTY=(By.XPATH,'//*[@id="empty_cart"]/p')
    
    #Add products to cart
    def add_product(self):
        self.click_operation(self.ADD_PRODUCT)
    
    # Click 'Cart' button    
    def open_cart(self):
        self.click_operation(self.CART_BTN)
       
     
    #Click 'X' button corresponding to particular product   
    def remove_product(self):
        self.click_operation(self.X_BTN)
     
    #Verify that product is removed from the cart   
    def veify_empty(self):
        return self.find_web_element(self.EMPTY).text