from selenium import webdriver
from pages.aleart_page import AlertPage
from time import sleep

def test_simple_alert():
    driver = webdriver.Chrome()
    driver.maximize_window()
    alert_page = AlertPage(driver)
    alert_page.open_url()
    alert_page.click_simple_alert()
    sleep(2)  # Wait for a while to observe the alert handling
    alert_page.click_confirm_alert()
    sleep(2)
    alert_page.click_prompt_alert()
    sleep(2)
    alert_page.get_prompt_message()
    sleep(2)  # Wait for a while to observe the alert handling
    driver.quit()