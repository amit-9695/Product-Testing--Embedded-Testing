from selenium import webdriver
from pages.google_page import GooglePage
from time import sleep

def test_google_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    google_page = GooglePage(driver)
    google_page.open_url()
    title = google_page.get_title_js()
    print(f"Google Page Title: {title}")
    assert "Google" in title
    sleep(2)  # Wait for a while to observe the page title
    driver.quit()