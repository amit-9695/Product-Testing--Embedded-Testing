from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """Page object for the login page of the application."""
    USERNAME_LOCATOR = (By.ID, "user-name")
    PASSWORD_LOCATOR = (By.ID, "password")
    LOGIN_BUTTON_LOCATOR = (By.ID, "login-button")
    
    def login(self, username, password):
        """Perform login action with the provided username and password."""
        self.enter_text(self.USERNAME_LOCATOR, username)
        self.enter_text(self.PASSWORD_LOCATOR, password)
        self.click_element(self.LOGIN_BUTTON_LOCATOR)