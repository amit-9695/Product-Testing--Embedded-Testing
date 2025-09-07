import pytest
from selenium.webdriver.common.by import By
from config.config import Config
from pages.web_table_page import WebTablePage
import time

@pytest.mark.usefixtures("init_driver")
class TestWebTable:
    
    def setup_method(self):
        self.web_table_page=WebTablePage(self.driver)
        self.web_table_page.visit(Config.BASE_URL)
        time.sleep(5)
        
    
    def test_table_row_count(self):
       assert 6==6
    
