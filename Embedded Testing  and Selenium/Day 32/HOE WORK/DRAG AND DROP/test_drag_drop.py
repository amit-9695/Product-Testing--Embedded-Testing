from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_drag_drop_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/droppable/")
    driver.switch_to.frame(driver.find_element("xpath", "//iframe[@class='demo-frame']"))
    draggable = driver.find_element("id", "draggable")
    droppable = driver.find_element("id", "droppable")
    action = ActionChains(driver)
    action.drag_and_drop(draggable, droppable).perform()
    print("Drag and drop performed.")
    time.sleep(2)
    driver.quit()
