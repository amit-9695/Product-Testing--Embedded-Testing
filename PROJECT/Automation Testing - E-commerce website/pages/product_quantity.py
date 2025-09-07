from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductQuantityPage(BasePage):
    VIEW_PRODUCT_BTN=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div[1]/div[2]/div/div[2]/ul/li/a')
    QUANTITY_INPUT=(By.XPATH,'//*[@id="quantity"]')
    ADD_CART_BTN=(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button')
    VIEW_CART_BTN=(By.XPATH,'//*[@id="cartModal"]/div/div/div[2]/p[2]/a/u')
    PRODUCT_QTY_CART=(By.XPATH,'//*[@id="product-1"]/td[4]/button')
    
    def view_product(self):
        self.scroll_by_operation(0,350)
        self.click_operation(self.VIEW_PRODUCT_BTN)
        
    def increase_qty(self,qty):
        self.scroll_by_operation(0,220)
        self.enter_value_operation(self.QUANTITY_INPUT,qty)
        
    def add_cart(self):
        self.click_operation(self.ADD_CART_BTN)
        
    def view_cart(self):
        self.click_operation(self.VIEW_CART_BTN)
        
    def product_qty_cart(self):
        return self.find_web_element(self.PRODUCT_QTY_CART).text
        