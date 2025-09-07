# Write the code for achiving the explicit wait functionality in Selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtils:
    def __init__(self,driver,timeout=10):  # here we set a default timeout as 10, in feture you want you can change and give your own value
        self.driver=driver
        self.timeout=timeout
    
    # Creating method to wait until an element is not found in the WebDriver
    def wait_for_visibility(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.visibility_of_element_located(locator))
    
    
    # Creating method to wait until an element is not clickable 
    def wait_for_clickable(self,locator):
        WebDriverWait(self.driver,self.timeout).until(EC.element_to_be_clickable(locator))
        
    # Creating method to wait until an element is not present in the WebDriver
    def wait_for_presence(self,locator):
        return WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located(locator))
    
    # Creating method to wait until the url not loaded
    def wait_for_url(self,url):
        return WebDriverWait(self.driver,self.timeout).until(EC.url_contains(url))