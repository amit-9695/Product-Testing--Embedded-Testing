from selenium.webdriver.common.by import By
from base.base_page import BasePage
class LoginPage(BasePage):
    
    USER_NAME=(By.ID,"user-name")
    PASSWORD=(By.ID,"password")
    LOGIN_BUTTON=(By.ID,"login-button")
    ERROR_MESSAGE=(By.CSS_SELECTOR,"h3[data-test='error']")

    def __init__(self,driver):
        super().__init__(driver)
    
    def load(self,url):
        self.visit(url)
    
    def login(self,username,password):
        self.enter_text(self.USER_NAME,username)
        self.enter_text(self.PASSWORD,password)
        self.click(self.LOGIN_BUTTON)
    
    def is_login_successful(self):
        return self.current_url_contains("inventory")
    
    def is_login_failed(self):
        return self.is_visisble(self.ERROR_MESSAGE)