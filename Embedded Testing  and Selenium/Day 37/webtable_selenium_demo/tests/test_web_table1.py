import pytest
from selenium.webdriver.common.by import By
from config.config import Config
from selenium import webdriver


class TestWebTable1:
    
    def test_web_table1(self):
        driver=webdriver.Edge()
        driver.get(Config.BASE_URL)
        webtable=driver.find_element(By.ID,"productTable")
        
        rows=webtable.find_elements(By.TAG_NAME,"tr")
        
        print(f"Number of rows: {len(rows)-1}") #Exclude header row
        
        for row in rows[1:]: # skip the header row
            columns=row.find_elements(By.TAG_NAME,"td")
            input=columns[-1].find_element(By.TAG_NAME,"input")
            input.click()
            print("Checkbox clicked")
       