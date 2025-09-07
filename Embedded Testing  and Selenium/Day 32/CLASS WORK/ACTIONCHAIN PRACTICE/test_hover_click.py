from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_mouse_hover_click():
    # Launch the browser and navigate to the page
    driver = webdriver.Chrome()
    
    # Load the page
    driver.get("https://demoqa.com/menu")
    
    # maximize the window
    driver.maximize_window()
    
    # Finding the main menu using XPATH
    main_menu = driver.find_element(By.XPATH, "//a[text()='Main Item 2']")
    # Finding the submenu using XPATH
    submenu = driver.find_element(By.XPATH, "//a[text()='SUB SUB LIST »']")
    
    # Create an instance of ActionChains
    actions = ActionChains(driver)
    # Perform mouse hover action
    actions.move_to_element(main_menu).move_to_element(submenu).perform()
    
    # Wait for the submenu to appear
    time.sleep(2)
    
    driver.quit()