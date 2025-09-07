from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogoutWait(BasePage):
    MENU_LOCATOR = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_BUTTON_LOCATOR = (By.ID, "logout_sidebar_link")
    
    def logout_wait(self):
        self.click_element(self.MENU_LOCATOR)
        self.click_element(self.LOGOUT_BUTTON_LOCATOR)