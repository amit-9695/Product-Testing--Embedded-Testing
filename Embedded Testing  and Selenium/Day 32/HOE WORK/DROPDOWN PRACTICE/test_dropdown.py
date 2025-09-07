from selenium import webdriver
from select_menu_page import SelectMenuPage
import time

def test_dropdown():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selenium08.blogspot.com/2019/11/dropdown.html")
    page= SelectMenuPage(driver)
    page.select_text("India")
    time.sleep(2)
    
    print("Selected option:", page.get_selected_option())
