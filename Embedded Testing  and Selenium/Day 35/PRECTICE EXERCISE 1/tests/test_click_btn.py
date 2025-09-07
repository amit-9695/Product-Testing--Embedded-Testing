import pytest
from time import sleep
from pages.click_btn_page import ClickBtnPage

@pytest.mark.usefixtures("init_driver")
class TestClickBtn():
    def test_click_btn(self):
        click_btn_obj=ClickBtnPage(self.driver)
        click_btn_obj.click_btn()
        sleep(3)