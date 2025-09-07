from selenium import webdriver
from drivers import browser_factory
import time
 
def test_swaglab_title():
    try:
        driver = browser_factory.get_driver("chrome")
        driver.get("https://www.saucedemo.com/")
        actual_title = driver.title
        expected_title = "Swag Labs"
        assert expected_title in actual_title
        print("Test case is passed")
    
        time.sleep(2)
    except:
        print("File not found")
        
    finally:
        driver.quit()
        
    