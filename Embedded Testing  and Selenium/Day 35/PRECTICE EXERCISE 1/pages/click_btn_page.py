from config.config import Config
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

class ClickBtnPage(BasePage):
    CLICK_ME_BTN=(By.XPATH,"//button[text()='Click Me']")
    DOUBLE_CLICK_BTN=(By.XPATH,'//button[text()="Double Click Me"]')
    RIGHT_CLICK_BTN=(By.XPATH,'//button[text()="Right Click Me"]')
    def click_btn(self):
        self.open_url(Config.BUTTON_URL)
        self.double_click_element(self.DOUBLE_CLICK_BTN)
        sleep(2)
        self.right_click_element(self.RIGHT_CLICK_BTN)
        sleep(2)
        self.click_element(self.CLICK_ME_BTN)