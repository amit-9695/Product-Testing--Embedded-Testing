# Test Case 4: Logout User
from pages.logout_page import LogoutPage
from time import sleep
import pytest 
@pytest.mark.usefixtures("init_driver")
class TestLogout:
    def test_logout(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        
        obj=LogoutPage(self.driver)
        obj.logout_login()
        
        output=obj.logout_login_as()
        assert output == 'Logged in as AMIT SHUKLA'
        print('✅ Verify - Logged in as AMIT SHUKLA')
        obj.logout()
        sleep(2)