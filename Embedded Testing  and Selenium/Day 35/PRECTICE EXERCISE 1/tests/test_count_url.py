import pytest
from time import sleep
from pages.count_url_page import CountUrlPage

@pytest.mark.usefixtures("init_driver")
class TestCount:
    def test_count(self):
        count_obj=CountUrlPage(self.driver)
        count_obj.count_links()
        sleep(3)