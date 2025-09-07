from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
    
    def visit(self,url):
        self.driver.get(url)
    
    def find(self,locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    
    def click(self,locator):
        self.find(locator).click()
    
    def enter_text(self,locator,text):
        self.find(locator).send_keys(text)
    
    def is_visisble(self,locator):
        try:
            return self.find(locator).is_displayed()
        except:
            return False
    
    def current_url_contains(self,text):
        return text in self.driver.current_url