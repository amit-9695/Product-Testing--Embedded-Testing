""" from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    def __init__(self,driver,timeout=10):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,timeout)
        self.action=ActionChains(self.driver)
        
    def find(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def click(self,locator):
        ele=self.wait.until(EC.element_to_be_clickable(locator))
        self.action.click(ele).perform()
        
    def enter_value(self,locator,value):
        ele = self.find(locator)
        ele.clear()
        ele.send_keys(value)
        
    def get_text(self,locator):
        return self.find(locator).text """