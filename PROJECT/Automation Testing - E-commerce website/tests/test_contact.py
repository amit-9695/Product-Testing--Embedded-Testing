# Test Case 6: Contact Us Form
from pages.contact_page import ContactPage
from time import sleep
import pytest
from os import path

@pytest.mark.usefixtures("init_driver")
class TestContact:
    def test_contact(self):
        #finding the title of home page after launching the website
        title=self.driver.title
        assert title == "Automation Exercise"
        print("✅ Verify - home page is visible successfully")
        sleep(2)
        
        # contact us
        contact=ContactPage(self.driver)
        contact.contact_page()
        sleep(2)
        
        #Verify 'GET IN TOUCH' is visible
        touch=contact.get_in_touch()
        assert touch == "GET IN TOUCH"
        print("✅ Verify - 'GET IN TOUCH' is visible")
        
        # entering basic details
        contact.enter_detail("Amit Shukla","amit123@gmail.com","Product enquiry","I want to know about some products that is for only male")
        
        #uploading the 
        file_path = path.abspath(r"C:\Users\amit8\OneDrive\Documents\PROJECT\example.txt")
        contact.upload_file(file_path)
        sleep(2)
        
        # submit the contact form
        contact.submit_form()
        
        # accept the alert
        contact.alert_accept()
        sleep(2)
        
        #Verify success message 'Success! Your details have been submitted successfully.' is visible
        msg=contact.sucess_message()
        assert msg == "Success! Your details have been submitted successfully."
        print("✅ Verify success message 'Success! Your details have been submitted successfully.' is visible")
        
        # Click 'Home' button and verify that landed to home page successfully
        contact.return_home()
        current_url = self.driver.current_url
        assert current_url == "https://automationexercise.com/"
        print("✅ verify that landed to home page successfully")
        sleep(2)
        
        
        
        
        