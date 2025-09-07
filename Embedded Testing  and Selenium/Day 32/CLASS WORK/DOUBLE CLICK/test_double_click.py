from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_double_click_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://api.jquery.com/dblclick/")
    driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))
    box = driver.find_element(By.CSS_SELECTOR, "div")
    action = ActionChains(driver)
    action.double_click(box).perform()
    print("Double-click performed.")
    time.sleep(2)
    driver.quit() 
