from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver import ActionChains

def test_move_to_element():
    # Launch the browser and navigate to the page
    driver = webdriver.Chrome()
    # Load the page
    driver.get("https://demoqa.com/menu")
    
    # Locate the element to move to
    element_to_hover = driver.find_element(By.XPATH, "//a[text() = 'Main Item 1']")
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Move to the element
    actions.move_to_element(element_to_hover).perform()
    
    print("Moved to the element successfully.")
    
    # Wait for a few seconds to observe the action
    time.sleep(3)
    # Close the browser
    driver.quit()