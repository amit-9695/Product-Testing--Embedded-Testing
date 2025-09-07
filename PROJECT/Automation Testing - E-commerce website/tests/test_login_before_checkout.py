# Test Case 16: Place Order: Login before Checkout
from pages.login_before_checkout_page import LoginbeforePage
from time import sleep
import pytest
from configs.config import Config

@pytest.mark.usefixtures("init_driver")
class TestLoginbefore:
    def test_login_before(self):
        #Verify that home page is visible successfully
        home_page_url = "https://automationexercise.com/"
        current_url=self.driver.current_url
        assert home_page_url == current_url
        print("✅ Verify that home page is visible successfully")
        sleep(2)
        
        # creating instance
        obj=LoginbeforePage(self.driver)
        
        obj.login(Config.EMAIL,Config.PASSWORD)
        
        output=obj.login_as()
        assert output == 'Logged in as AMIT SHUKLA'
        print('✅ Verify - Logged in as AMIT SHUKLA')
        
        obj.add_product()
        obj.click_cart()
        
        cart_url=self.driver.current_url
        assert cart_url == "https://automationexercise.com/view_cart"
        
        print("✅ Verify - cart page")
        
        obj.proceed_to_checkout()
        
        address=obj.verify_address()
        assert address == "Address Details"
        print("✅ Verify Address Details")
        
        review=obj.verify_review()
        assert review == "Review Your Order"
        print("✅ verify - Review Your Order")
        
        obj.place_order("Proceed to payment")
        
        obj.payment("Amit",545584827424,423,11,2031)
        
        msg=obj.final_msg()
        assert msg == "Congratulations! Your order has been confirmed!"
        print("✅ Verify - Congratulations! Your order has been confirmed!")