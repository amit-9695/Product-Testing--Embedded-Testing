import pytest
from selenium.webdriver.common.by import By
from config.config import Config
from selenium import webdriver


class TestWebTable3:
    
    def test_web_table(self):
        driver=webdriver.Edge()
        driver.get(Config.BASE_URL)
        webtable=driver.find_element(By.XPATH,"//table[@name='BookTable']")
        
        #locate row and columns
        rows=webtable.find_elements(By.TAG_NAME,"tr")
        print(f"Number of rows: {len(rows)}")
        
        for row in rows:
            #locate all colums in the current row
            columns=row.find_elements(By.TAG_NAME,"td")
            print(f"Number of Columns in this row: {len(columns)}")
            #print data from each column
            for column in columns:
                print(column.text, end=" | ")
        print()
            
   
