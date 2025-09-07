#Test Case 3: Login User with incorrect email and password
import pytest
from time import sleep
from configs.config import Config
from pages.login_page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLogiIncorrectCredential:
    def test_login_with_incorrect_credential(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        
        login=LoginPage(self.driver)
        #Enter incorrect email address and password
        #Click 'login' button
        login.login_page("amit111@gmail.com",Config.PASSWORD)
        
        #. Verify error 'Your email or password is incorrect!' is visible
        msg=login.incorrect_msg()
        assert msg == "Your email or password is incorrect!"
        print("✅ Verify error 'Your email or password is incorrect!' is visible")
        sleep(2)