from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self,driver):
        self.driver=driver
    
    def visit(self,url):
        self.driver.get(url)
        self.driver.maximize_window ()
        
    def find_web_element(self,locator):
        return self.driver.find_element(*locator)
    
    def enter_text(self,locator,text):
        element=self.find_web_element(locator)
        element.send_keys(text)
    
    def click(self,locator):
        element=self.find_web_element(locator)
        element.click()
        
    def select_option(self,locator,option_text):
        dropdown_element=self.find_web_element(locator)
        #Create a Select object
        select=Select(dropdown_element)
        #Select by visisble text
        select.select_by_visible_text(option_text)
        
    
    
    