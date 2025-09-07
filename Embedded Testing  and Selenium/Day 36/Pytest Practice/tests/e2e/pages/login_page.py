from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.ID, "login-button")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    def open(self, base_url: str):
        self.visit(base_url)
    def login(self, username: str, password: str):
        self.type(self.USERNAME, username)
        self.type(self.PASSWORD, password)
        self.click(self.BTN_LOGIN)
    def error_text(self) -> str:
        return self.find(self.ERROR).text