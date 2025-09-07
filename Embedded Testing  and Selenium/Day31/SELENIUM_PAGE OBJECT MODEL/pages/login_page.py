from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, "//input[@id='user-name']")
        self.password_input = (By.XPATH, "//input[@id='password']")
        self.login_button = (By.XPATH, "//input[@id='login-button']")
        
    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
    
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()
            