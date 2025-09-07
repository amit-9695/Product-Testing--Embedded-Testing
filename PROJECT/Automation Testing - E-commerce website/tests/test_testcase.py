# Test Case 7: Verify Test Cases Page
from pages.check_testcase_page import CheckTestcasePage
from time import sleep
import pytest

@pytest.mark.usefixtures("init_driver")
class TestTestcasepage:
    def test_testcasepage(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        
        #Click on 'Test Cases' button
        test_case=CheckTestcasePage(self.driver)
        test_case.check_testcase_page()
        sleep(2)
        
        #. Verify user is navigated to test cases page successfully
        test_case_page_url='https://automationexercise.com/test_cases'
        current_page_url=self.driver.current_url
        assert test_case_page_url == current_page_url
        print("✅ Verify user is navigated to test cases page successfully")