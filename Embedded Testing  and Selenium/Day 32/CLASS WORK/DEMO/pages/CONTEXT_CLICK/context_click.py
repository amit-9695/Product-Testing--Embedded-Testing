import pytest
from selenium.webdriver import ActionChains
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def test_click_element():
    driver = webdriver.Chrome()
    driver.get("http://demoqa.com/tabs")
    # Locate the element by its ID
    element = driver.find_element(By.XPATH, "//a[@id='demo-tab-origin']")
    
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Move to the element and click it
    actions.move_to_element(element).click().perform()
    time.sleep(2)  # Wait for 2 seconds to observe the click action
    driver.quit()