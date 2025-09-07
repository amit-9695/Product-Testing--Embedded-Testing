from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium import webdriver
import time

def test_mouse_hover_click():
    driver = webdriver.Chrome()  # Initialize the WebDriver
    driver.get("http://demoqa.com/tabs")
      # Locate the element by its ID
    element = driver.find_element(By.XPATH, "//a[@id = 'demo-tab-origin']")
    # Create an ActionChains object
    actions = ActionChains(driver)
    # Move to the element and click it
    actions.move_to_element(element).click().perform()
    time.sleep(2)  # Wait for 2 seconds to observe the click action
    driver.quit()