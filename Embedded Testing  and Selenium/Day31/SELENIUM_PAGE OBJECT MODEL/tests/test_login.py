import pytest
from selenium import webdriver
from pages.login_page import LoginPage

def test_valid_login():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    log_page = LoginPage(driver)
    log_page.login("standard_user", "secret_sauce")