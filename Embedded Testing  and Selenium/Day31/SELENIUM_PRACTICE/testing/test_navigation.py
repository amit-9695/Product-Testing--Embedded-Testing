#  In this program we navigating one website(google) to another website(youtube)
import pytest, time
from selenium import webdriver

def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    print("first page :", driver.title)
    time.sleep(2)  # Wait for 2 seconds to observe the first page
    driver.get("https://www.youtube.com/")
    print("second page :", driver.title)
    time.sleep(1)  # Wait for 1 seconds to observe the second page
    driver.quit()  # Close the browser
    