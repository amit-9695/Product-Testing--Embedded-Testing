# Test Case 1: Register User
import pytest
import logging
from selenium import webdriver
from pages.regester_pages import RgesterPage
from pages.delete_account_page import DeleteAccountPage
from time import sleep
from configs.config import Config

@pytest.mark.usefixtures("init_driver")
class TestRegister:
    def test_regester_user(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        #Creating Instance of RegesterPage
        regester_page = RgesterPage(self.driver)
        regester_page.goto_singup_login()
        sleep(2)
    
        regester_page.enter_signup_details("AMIT SHUKLA","amitsuraj1221@gmail.com")
        sleep(2)
        
        regester_page.fill_account_info(Config.PASSWORD,"1",'November','2001')
        sleep(3)
        
        regester_page.address_info("first_name","last_name","company","address1","address2 of my","India","state","city",271201,9695230479)
        sleep(2)
        
        regester_page.create_account()
        sleep(2)
        
        res=regester_page.account_created_visible()
        assert res == "ACCOUNT CREATED!"
        print("✅ Verify that 'ACCOUNT CREATED!' is visible")
        
        regester_page.continue_after_create()
        sleep(2)
        
        logged_as=regester_page.logged_in_as_visible()
        assert logged_as == "Logged in as AMIT SHUKLA"
        print("✅ Verify that 'Logged in as username' is visible")
        
        
        #Click 'Delete Account' button
        regester_page.delete_account()
        sleep(2)
        
        #Verify that 'ACCOUNT DELETED!' is visible
        verify=regester_page.account_deleted_visible()
        assert verify == "ACCOUNT DELETED!"
        print("✅ Verify that 'ACCOUNT DELETED!' is visible")
        
        #click 'Continue' button
        regester_page.continue_after_delete()
        
        
    