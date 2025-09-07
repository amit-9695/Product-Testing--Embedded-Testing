from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def test_login():
    USERNAME_LOCATOR = (By.ID, "user-name")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    
    # wait for usename field to be visible
    webdriver_wait=WebDriverWait(driver,timeout=10)
    user_name=webdriver_wait.until(EC.visibility_of_element_located(USERNAME_LOCATOR))
    user_name.send_keys("standard_user")
    password=webdriver_wait.until(EC.visibility_of_element_located(PASSWORD_LOCATOR))
    password.send_keys("secret_sauce")
    button=webdriver_wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_LOCATOR))
    button.click()