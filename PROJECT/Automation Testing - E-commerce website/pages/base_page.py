from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os


class BasePage:
    def __init__(self,driver,timeout=50):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout)
        self.actions=ActionChains(self.driver)

    def find_web_element(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_multiple_web_element(self,locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def presence_of_element_operation(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click_operation(self,locator):
        btn=self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(btn).perform()
        
    def double_click_operation(self,locator):
        btn= self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.double_click(btn).perform()
        
    def context_click_operation(self,locator):
        btn=self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.context_click(btn).perform()

    def enter_value_operation(self,locator,text):
        element=self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(element).send_keys(text).perform()
        
    
    def scroll_by_operation(self,x=0,y=100):
        self.driver.execute_script(f"window.scrollBy({x}, {y})")
        
    def scrollTo_bottom_operation(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    def scrollTo_Top_operation(self):
        self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
        
    def upload_file_operation(self,locator):
        btn=self.wait.until(EC.element_to_be_clickable(locator))
        self.actions.click(btn).send_keys(self.upload).perform()
        
        
        
        
    
        