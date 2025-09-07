from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_mouse_hover_click():
    # Launch the browser and navigate to the page
    driver = webdriver.Chrome()
    
    # Load the page
    driver.get("https://jqueryui.com/selectable/")
    
    # maximize the window
    driver.maximize_window()
    
    # Finding the iframe using XPATH
    iframe_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
    # Switch to the iframe
    driver.switch_to.frame(iframe_element)
    
    # Finding the selectable items using iD
    item1 = driver.find_element(By.XPATH, "//ol[@id='selectable']/li[1]")
    item2 = driver.find_element(By.XPATH, "//ol[@id='selectable']/li[2]")
    
    # creating an instance of ActionChains
    actions = ActionChains(driver)
    # Perform click action on the first item
    actions.double_click(item1).context_click(item2).perform()
    
    
    # Wait for the submenu to appear
    time.sleep(2)
    
    driver.quit()