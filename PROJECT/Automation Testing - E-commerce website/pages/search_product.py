from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver

class SearchProduct(BasePage):
    ALL_PRODUCT=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/h2')
    SEARH_INPUT=(By.XPATH,'//*[@id="search_product"]')
    SEARH_BTN=(By.XPATH,'//*[@id="submit_search"]')
    SEARCHED_ITEM_NAME=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/p')
    
    def all_product(self):
        return self.find_web_element(self.ALL_PRODUCT).text
    
    def search_product(self,product_name):
        self.enter_value_operation(self.SEARH_INPUT,product_name)
        self.click_operation(self.SEARH_BTN)
        
    def item_name(self):
        return self.find_web_element(self.SEARCHED_ITEM_NAME).text
    