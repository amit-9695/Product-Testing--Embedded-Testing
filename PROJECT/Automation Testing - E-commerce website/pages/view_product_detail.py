from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium import webdriver

class ViewProductPage(BasePage):
    PRODUCTS_BTN=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[2]/a')
    FRIST_VIEW_PRODUCT=(By.XPATH,'/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a')
    PRODUCT_NAME=(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')
    CATEGORY =(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[1]')
    PRICE = (By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/span')
    AVAILABILITY=(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[2]')
    CONDITION=(By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[3]')
    BRAND = (By.XPATH,'/html/body/section/div/div/div[2]/div[2]/div[2]/div/p[4]')
    
    def click_product(self):
        self.click_operation(self.PRODUCTS_BTN)
        
    def view_first_product(self):
        self.scroll_by_operation(0,350)
        self.click_operation(self.FRIST_VIEW_PRODUCT)
        
        
    
    def first_product_detail(self):
        # 
        # li=(self.PRODUCT_NAME,self.CATEGORY,self.PRICE,self.AVAILABILITY,self.CONDITION,self.BRAND)
        # for locator in li:
        #    lo=str(locator)
        #    return self.find_multiple_web_element(lo).text
        return self.find_web_element(self.PRODUCT_NAME).text , self.find_web_element(self.CATEGORY).text , self.find_web_element(self.PRICE).text , self.find_web_element(self.AVAILABILITY).text , self.find_web_element(self.CONDITION).text , self.find_web_element(self.BRAND).text            
       