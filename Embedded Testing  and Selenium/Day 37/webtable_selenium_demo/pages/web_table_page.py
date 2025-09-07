from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from util.web_table_helper import WebTable

class WebTablePage(BasePage):
    TABLE_LOCATOR=(By.ID,"productTable")
    def __init__(self, driver):
        super().__init__(driver)
        table=self.find_web_element(self.TABLE_LOCATOR)
        print(table)
        self.web_table=  WebTable(table)
    def table_row_count(self):
        return self.web_table.get_row_count()
      
      
      
      
      
            
        
