from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time

def test_click_hold_element():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://jqueryui.com/selectable/")
    driver.switch_to.frame(driver.find_element("xpath", "//iframe[@class='demo-frame']"))
    item1 = driver.find_element("xpath", "//li[text()='Item 1']")
    item4 = driver.find_element("xpath", "//li[text()='Item 4']")
    action = ActionChains(driver)
    action.click_and_hold(item1).move_to_element(item4).release().perform()
    print("Click and hold performed.")
    time.sleep(3)
    driver.quit()
