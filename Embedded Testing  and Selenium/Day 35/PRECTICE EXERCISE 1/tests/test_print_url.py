from time import sleep
import pytest
from pages.print_url_page import PrintUrl

@pytest.mark.usefixtures("init_driver")
class TestPrintUrl():
    def test_print_url(self):
        printurl_obj=PrintUrl(self.driver)
        printurl_obj.print_url()
        # To finding the cureent url we use "current_url" keyword
        expected_url=self.driver.current_url
        print("Current URL : ",expected_url)
        sleep(3)