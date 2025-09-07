from time import sleep
from util.scroll_helper import ScrollHelper
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_scroll_to_element():
    driver = webdriver.Chrome()
    driver.get("https://selenium08.blogspot.com/2020/02/vertical-scroll.html")
    driver.maximize_window()
    scroll_helper = ScrollHelper(driver)
    element = driver.find_element(By.XPATH, "//a[text()='Health']")   
    scroll_helper.scroll_to_element(element)
    sleep(3)
    driver.quit()