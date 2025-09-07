from selenium import webdriver
class GooglePage:
    URL = "https://www.google.com"
    
    def __init__(self, driver):
        self.driver = driver
        
    def open_url(self):
        self.driver.get(self.URL)
        
    def get_title_js(self):
        return self.driver.execute_script("return document.title;")
    
    