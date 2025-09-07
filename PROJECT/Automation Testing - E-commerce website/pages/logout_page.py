from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.regester_pages import RgesterPage
from pages.login_page import LoginPage
from configs.config import Config

class LogoutPage(RgesterPage,LoginPage,BasePage):
    LOGIN_AS=(By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[10]/a')
    def logout_login(self):
        #from login page
        self.login_page(Config.EMAIL,Config.PASSWORD)
        
    def logout_login_as(self):
        return self.find_web_element(self.LOGIN_AS).text
      
    def logout(self):
        #from regester page
        self.logout_account()