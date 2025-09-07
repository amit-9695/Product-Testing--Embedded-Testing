from time import sleep
import pytest
from pages.login_page import LoginPage

@pytest.mark.usefixtures("init_driver")
class TestLogin():
    def test_login(self):
        login_obj=LoginPage(self.driver)
        login_obj.login("student","Password123")
        sleep(2)