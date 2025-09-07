from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
username_field = driver.find_element(By.XPATH, "//input[@id='user-name']")
username_field.send_keys("standard_user")
password_field = driver.find_element(By.XPATH, "//input[@id='password']")
password_field.send_keys

driver.quit()