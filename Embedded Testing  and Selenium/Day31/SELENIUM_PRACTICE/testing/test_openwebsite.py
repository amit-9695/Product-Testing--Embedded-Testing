import pytest
from selenium import webdriver


def test_open_website(capsys):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    # Capture the output of the current URL
    page_title = driver.title
    print(f"Page title is: {page_title}")
    
    # Close the driver
    driver.quit()