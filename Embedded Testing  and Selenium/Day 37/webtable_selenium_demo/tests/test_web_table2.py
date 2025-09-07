import pytest
from selenium.webdriver.common.by import By
from config.config import Config
from selenium import webdriver
from util.web_table_helper import WebTable

class TestWebTable2:
    
    def test_web_table2(self):
        driver=webdriver.Edge()
        driver.get(Config.BASE_URL)
        webtable=driver.find_element(By.ID,"productTable")
        table=WebTable(webtable)
        data=table.get_cell_data(2,2)
        print(data)
        