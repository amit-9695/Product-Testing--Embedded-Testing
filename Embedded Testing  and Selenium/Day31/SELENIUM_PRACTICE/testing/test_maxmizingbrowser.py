import pytest
from selenium import webdriver


def test_maximizing_browser():
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    # Maximize the browser window
    driver.maximize_window()
    
    # invoke the window manager