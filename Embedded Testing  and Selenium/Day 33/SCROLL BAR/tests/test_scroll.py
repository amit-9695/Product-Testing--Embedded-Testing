from util.scroll_helper import ScrollHelper
from selenium import webdriver
import time

def test_scroll_to_pixel():
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.com/?guccounter=1")
    
    scroll_helper = ScrollHelper(driver)
    scroll_helper.scroll_by_pixel(0,200)
    time.sleep(2)

    scroll_helper.scroll_to_bottom()
    time.sleep(2)
    
    scroll_helper.scroll_to_top()
    time.sleep(2)
    
    driver.quit()