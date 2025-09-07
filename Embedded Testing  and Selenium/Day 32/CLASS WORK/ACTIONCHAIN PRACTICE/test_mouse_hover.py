from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_mouse_hover():
    # Launch the browser and navigate to the page
    driver = webdriver.Chrome()
    
    # Load the page
    driver.get("https://demoqa.com/menu")
    
    # maximize the window
    driver.maximize_window()
    
    # Finding the element using XPATH
    menu_element = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    
    # Create an instance of ActionChains
    actions = ActionChains(driver)
    # Perform mouse hover action
    actions.move_to_element(menu_element).perform()
    
    # Wait for the submenu to appear
    time.sleep(2)
    
    driver.quit()