from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_mouse_hover_click():
    # Launch the browser and navigate to the page
    driver = webdriver.Chrome()
    
    # Load the page
    driver.get("https://jqueryui.com/droppable/")
    
    # maximize the window
    driver.maximize_window()
    
    # Finding the iframe using XPATH
    iframe_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
    # Switch to the iframe
    driver.switch_to.frame(iframe_element)
    
    # Finding the draggable and droppable elements using ID
    # Note: Ensure the IDs match the actual elements in the iframe
    draggable_element=driver.find_element(By.ID, "draggable")
    droppable_element=driver.find_element(By.ID, "droppable")
    
    # creating an instance of ActionChains
    actions = ActionChains(driver)
    
    # Perform drag and drop action
    actions.drag_and_drop(draggable_element, droppable_element).perform()
    
    
    # Wait for the submenu to appear
    time.sleep(2)
    
    driver.quit()