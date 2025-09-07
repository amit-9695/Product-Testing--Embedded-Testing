import pytest
from pages.login_page import LoginPage
from config.config import Config
from util.data_provider import DataProvider

@pytest.mark.usefixtures("init_driver")
class TestSwagLabLogin:
    
    def setup_method(self):
        self.login_page=LoginPage(self.driver)
        self.login_page.load(Config.BASE_URL)
    
    @pytest.mark.parametrize("username,password",DataProvider.get_data_from_csv("data/test_data.csv"))
    def test_login_csv(self,username,password):
        self.login_page.login(username,password)
        